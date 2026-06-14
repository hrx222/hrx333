import { useState, useRef, useEffect } from 'react';
import { Code2, Play, X, Minus, RotateCcw, Trash2 } from 'lucide-react';

declare global {
  interface Window {
    Sk: any;
  }
}

export default function CodePlayground() {
  const [isOpen, setIsOpen] = useState(true);
  const [isMinimized, setIsMinimized] = useState(false);
  const [position, setPosition] = useState({ x: 20, y: 0 });

  // 设置初始位置到屏幕底部
  useEffect(() => {
    setPosition({ x: 20, y: Math.max(window.innerHeight - 460, 20) });
  }, []);
  const [code, setCode] = useState('# 在这里编写你的Python代码\n# 点击运行按钮执行\n\nprint("Hello, World!")\n');
  const [output, setOutput] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [skulptLoaded, setSkulptLoaded] = useState(false);
  const [dragState, setDragState] = useState({
    isDragging: false,
    startX: 0,
    startY: 0,
    origX: 0,
    origY: 0,
  });
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // 加载Skulpt
  useEffect(() => {
    if (window.Sk) {
      setSkulptLoaded(true);
      return;
    }

    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/skulpt@1.2.0/dist/skulpt.min.js';
    script.async = true;
    script.onload = () => {
      const docScript = document.createElement('script');
      docScript.src = 'https://cdn.jsdelivr.net/npm/skulpt@1.2.0/dist/skulpt-stdlib.js';
      docScript.async = true;
      docScript.onload = () => setSkulptLoaded(true);
      document.body.appendChild(docScript);
    };
    document.body.appendChild(script);
  }, []);

  // 拖拽功能
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (dragState.isDragging) {
        const newX = dragState.origX + (e.clientX - dragState.startX);
        const newY = dragState.origY + (e.clientY - dragState.startY);
        const maxX = window.innerWidth - 100;
        const maxY = window.innerHeight - 100;
        setPosition({
          x: Math.max(0, Math.min(newX, maxX)),
          y: Math.max(0, Math.min(newY, maxY)),
        });
      }
    };

    const handleMouseUp = () => {
      if (dragState.isDragging) {
        setDragState({ ...dragState, isDragging: false });
      }
    };

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, [dragState]);

  const startDrag = (e: React.MouseEvent) => {
    if (isMinimized) return;
    e.preventDefault();
    setDragState({
      isDragging: true,
      startX: e.clientX,
      startY: e.clientY,
      origX: position.x,
      origY: position.y,
    });
  };

  const runCode = () => {
    setIsRunning(true);
    setOutput('▶ 运行中...\n');

    if (!window.Sk || !skulptLoaded) {
      setOutput('⏳ Python解释器正在加载，请稍候再试...');
      setIsRunning(false);
      return;
    }

    try {
      const Sk = window.Sk;
      let outputText = '';

      Sk.configure({
        output: (text: string) => {
          outputText += text;
        },
        read: (x: string) => {
          if (Sk.builtinFiles === undefined || Sk.builtinFiles['files'][x] === undefined) {
            throw new Error("File not found: '" + x + "'");
          }
          return Sk.builtinFiles['files'][x];
        },
        __future__: Sk.python3,
      });

      const myPromise = Sk.misceval.asyncToPromise(() =>
        Sk.importMainWithBody('<stdin>', false, code, true)
      );

      myPromise.then(
        () => {
          setOutput(outputText || '(无输出 - 代码运行成功)');
          setIsRunning(false);
        },
        (err: any) => {
          setOutput('❌ 错误:\n' + err.toString());
          setIsRunning(false);
        }
      );
    } catch (err: any) {
      setOutput('❌ 运行时错误:\n' + err.toString());
      setIsRunning(false);
    }
  };

  const clearCode = () => {
    setCode('');
    if (textareaRef.current) {
      textareaRef.current.focus();
    }
  };

  const clearOutput = () => {
    setOutput('');
  };

  const insertExample = () => {
    const examples = [
      '# 计算1到10的和\nsum = 0\nfor i in range(1, 11):\n    sum += i\nprint("1到10的和:", sum)\n',
      '# 列表操作\nnumbers = [3, 1, 4, 1, 5, 9, 2, 6]\nprint("原始列表:", numbers)\nprint("排序后:", sorted(numbers))\nprint("最大值:", max(numbers))\nprint("最小值:", min(numbers))\nprint("长度:", len(numbers))\n',
      '# 字典操作\nstudent = {"name": "张三", "age": 20, "score": 95}\nprint("学生信息:", student)\nprint("姓名:", student["name"])\nstudent["grade"] = "A"\nprint("添加后:", student)\n',
      '# 函数定义\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nfor i in range(1, 8):\n    print(f"{i}! = {factorial(i)}")\n',
      '# 字符串处理\ntext = "Hello, Python!"\nprint("原始:", text)\nprint("大写:", text.upper())\nprint("小写:", text.lower())\nprint("长度:", len(text))\nprint("切片:", text[0:5])\n',
      '# 条件判断\nscore = 85\nif score >= 90:\n    print("优秀")\nelif score >= 80:\n    print("良好")\nelif score >= 60:\n    print("及格")\nelse:\n    print("不及格")\n',
    ];
    const randomExample = examples[Math.floor(Math.random() * examples.length)];
    setCode(randomExample);
  };

  // 折叠状态的浮窗按钮
  if (!isOpen) {
    return (
      <button
        onClick={() => setIsOpen(true)}
        className="fixed bottom-6 left-6 z-50 w-14 h-14 rounded-full bg-gradient-to-br from-neon-blue to-neon-purple shadow-[0_0_30px_rgba(0,212,255,0.4)] hover:scale-110 transition-all duration-300 flex items-center justify-center"
        title="打开代码练习"
      >
        <Code2 className="w-6 h-6 text-white" />
      </button>
    );
  }

  return (
    <div
      className="fixed z-50 shadow-2xl rounded-xl border border-neon-blue/30 overflow-hidden bg-space-900/95 backdrop-blur-xl"
      style={{
        left: position.x,
        top: position.y,
        width: isMinimized ? 180 : 480,
        height: isMinimized ? 'auto' : 420,
      }}
    >
      {/* Header */}
      <div
        className="flex items-center justify-between px-4 py-2 bg-gradient-to-r from-neon-blue/20 to-neon-purple/20 border-b border-neon-blue/30 cursor-move select-none"
        onMouseDown={startDrag}
      >
        <div className="flex items-center gap-2">
          <Code2 className="w-4 h-4 text-neon-blue" />
          <span className="text-sm font-semibold text-white">代码练习</span>
        </div>
        <div className="flex items-center gap-1">
          <button
            onClick={() => setIsMinimized(!isMinimized)}
            className="p-1.5 text-gray-400 hover:text-white hover:bg-white/10 rounded transition-colors"
            title={isMinimized ? '展开' : '最小化'}
          >
            <Minus className="w-3.5 h-3.5" />
          </button>
          <button
            onClick={() => setIsOpen(false)}
            className="p-1.5 text-gray-400 hover:text-red-400 hover:bg-red-400/10 rounded transition-colors"
            title="关闭"
          >
            <X className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      {!isMinimized && (
        <div className="flex flex-col h-[calc(100%-40px)]">
          {/* 快捷按钮栏 */}
          <div className="flex items-center gap-1.5 px-3 py-2 border-b border-neon-blue/10 bg-space-800/50">
            <button
              onClick={runCode}
              disabled={isRunning || !skulptLoaded}
              className="flex items-center gap-1.5 px-3 py-1.5 bg-neon-blue/20 hover:bg-neon-blue/30 text-neon-blue text-sm font-medium rounded-lg transition-colors disabled:opacity-40"
            >
              <Play className="w-3.5 h-3.5" />
              {skulptLoaded ? '运行' : '加载中'}
            </button>
            <button
              onClick={insertExample}
              className="flex items-center gap-1.5 px-3 py-1.5 bg-neon-purple/15 hover:bg-neon-purple/25 text-neon-purple text-sm font-medium rounded-lg transition-colors"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              示例
            </button>
            <div className="flex-1" />
            <button
              onClick={clearCode}
              className="flex items-center gap-1 px-2.5 py-1.5 text-gray-500 hover:text-gray-300 text-xs rounded-lg transition-colors"
              title="清空代码"
            >
              <Trash2 className="w-3 h-3" />
              代码
            </button>
            <button
              onClick={clearOutput}
              className="flex items-center gap-1 px-2.5 py-1.5 text-gray-500 hover:text-gray-300 text-xs rounded-lg transition-colors"
              title="清空输出"
            >
              <Trash2 className="w-3 h-3" />
              输出
            </button>
          </div>

          {/* 代码编辑区 */}
          <div className="flex-1 flex flex-col min-h-0">
            <textarea
              ref={textareaRef}
              value={code}
              onChange={(e) => setCode(e.target.value)}
              spellCheck={false}
              className="flex-1 bg-space-950/80 text-green-300 font-mono text-sm p-3 resize-none leading-relaxed focus:outline-none border-b border-neon-blue/10"
              placeholder="# 在这里编写你的Python代码..."
            />
          </div>

          {/* 输出区域 */}
          <div className="px-3 py-2 text-xs font-mono bg-space-950/50 border-t border-neon-blue/10 text-gray-300 overflow-y-auto" style={{ maxHeight: 140 }}>
            <pre className="whitespace-pre-wrap break-words">{output || '(点击"运行"查看结果)'}</pre>
          </div>

          {/* 底部状态栏 */}
          <div className="flex items-center justify-between px-3 py-1.5 border-t border-neon-blue/10 bg-space-800/50 text-xs">
            <span className="text-gray-500">
              {skulptLoaded ? (
                <span className="text-neon-green">● Python解释器就绪</span>
              ) : (
                <span className="text-yellow-500 animate-pulse">○ 正在加载解释器...</span>
              )}
            </span>
            <span className="text-gray-600">{code.split('\n').length} 行 · {code.length} 字符</span>
          </div>
        </div>
      )}
    </div>
  );
}
