import { Sparkles, BookOpen, Code, Lightbulb } from 'lucide-react';
import AIChat from '../components/detail/AIChat';
import { Link } from 'react-router-dom';
import Button from '../components/common/Button';

const quickQuestions = [
  { icon: BookOpen, text: 'Pandas 如何进行数据清洗？' },
  { icon: Code, text: 'Matplotlib 如何绘制折线图？' },
  { icon: Lightbulb, text: 'Scikit-learn 常用算法有哪些？' },
  { icon: Sparkles, text: '如何处理缺失值？' },
];

export default function AITutor() {
  const { addChatMessage } = require('../store/useStore').useStore.getState();

  const handleQuickQuestion = (question: string) => {
    const userMessage = {
      id: Date.now().toString(),
      role: 'user' as const,
      content: question,
      timestamp: new Date(),
    };
    addChatMessage(userMessage);
  };

  return (
    <div className="min-h-screen pt-20">
      <div className="container mx-auto px-6 py-12">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-12">
            <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gradient-to-br from-neon-blue to-neon-purple mb-6">
              <Sparkles className="w-8 h-8 text-white" />
            </div>
            <h1 className="text-4xl md:text-5xl font-mono font-bold text-white mb-4">
              AI 导师
            </h1>
            <p className="text-gray-400 max-w-2xl mx-auto">
              有任何数据分析相关的问题都可以问我，我会尽力帮你解答
            </p>
          </div>

          {/* Quick questions */}
          <div className="mb-8">
            <h3 className="text-lg font-semibold text-white mb-4">快捷问题</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {quickQuestions.map((q, index) => (
                <button
                  key={index}
                  onClick={() => handleQuickQuestion(q.text)}
                  className="flex items-center gap-3 px-4 py-3 bg-space-800/50 border border-neon-blue/20 rounded-xl text-left hover:border-neon-blue/50 hover:bg-neon-blue/5 transition-all duration-300"
                >
                  <q.icon className="w-5 h-5 text-neon-blue flex-shrink-0" />
                  <span className="text-gray-300 text-sm">{q.text}</span>
                </button>
              ))}
            </div>
          </div>

          {/* Chat interface */}
          <AIChat />

          {/* Help section */}
          <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-space-800/30 rounded-xl p-6 border border-neon-blue/10">
              <BookOpen className="w-8 h-8 text-neon-blue mb-4" />
              <h4 className="font-semibold text-white mb-2">概念解释</h4>
              <p className="text-gray-400 text-sm">
                解释数据分析中的核心概念和术语
              </p>
            </div>
            <div className="bg-space-800/30 rounded-xl p-6 border border-neon-blue/10">
              <Code className="w-8 h-8 text-neon-purple mb-4" />
              <h4 className="font-semibold text-white mb-2">代码帮助</h4>
              <p className="text-gray-400 text-sm">
                帮你理解代码逻辑，调试错误
              </p>
            </div>
            <div className="bg-space-800/30 rounded-xl p-6 border border-neon-blue/10">
              <Lightbulb className="w-8 h-8 text-neon-green mb-4" />
              <h4 className="font-semibold text-white mb-2">学习建议</h4>
              <p className="text-gray-400 text-sm">
                提供学习路径和实践建议
              </p>
            </div>
          </div>

          {/* CTA to projects */}
          <div className="mt-12 text-center bg-gradient-to-r from-neon-blue/10 to-neon-purple/10 rounded-2xl p-8 border border-neon-blue/20">
            <h3 className="text-xl font-semibold text-white mb-3">
              准备好开始实战了吗？
            </h3>
            <p className="text-gray-400 mb-6">
              结合具体项目学习，效果更佳
            </p>
            <Link to="/projects">
              <Button>
                浏览训练项目
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
