import { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, Sparkles } from 'lucide-react';
import { useStore } from '../../store/useStore';
import { getAIResponse, simulateTypingEffect } from '../../utils/aiTutor';
import { ChatMessage } from '../../data/projects';

export default function AIChat() {
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [displayedText, setDisplayedText] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const { chatMessages, addChatMessage } = useStore();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [chatMessages, displayedText]);

  const handleSend = async () => {
    if (!input.trim() || isTyping) return;

    const userMessage: ChatMessage = {
      id: Date.now().toString(),
      role: 'user',
      content: input.trim(),
      timestamp: new Date(),
    };

    addChatMessage(userMessage);
    setInput('');
    setIsTyping(true);

    const response = getAIResponse(input);
    setDisplayedText('');

    simulateTypingEffect(
      response.content,
      (char) => {
        setDisplayedText((prev) => prev + char);
      },
      () => {
        const aiMessage: ChatMessage = {
          id: (Date.now() + 1).toString(),
          role: 'ai',
          content: response.content,
          timestamp: new Date(),
        };
        addChatMessage(aiMessage);
        setIsTyping(false);
      }
    );
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="bg-space-800/50 rounded-2xl border border-neon-blue/20 h-[500px] flex flex-col">
      <div className="flex items-center gap-3 px-6 py-4 border-b border-neon-blue/10">
        <div className="w-10 h-10 rounded-full bg-gradient-to-br from-neon-blue to-neon-purple flex items-center justify-center">
          <Sparkles className="w-5 h-5 text-white" />
        </div>
        <div>
          <h3 className="font-semibold text-white">AI 导师</h3>
          <p className="text-xs text-gray-400">随时为你解答问题</p>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {chatMessages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-center">
            <Bot className="w-16 h-16 text-gray-600 mb-4" />
            <h4 className="text-lg font-semibold text-gray-400 mb-2">开始提问吧</h4>
            <p className="text-gray-500 text-sm max-w-xs">
              可以问我关于 Pandas、Matplotlib、Scikit-learn 等任何数据分析问题
            </p>
          </div>
        )}

        {chatMessages.map((message) => (
          <div
            key={message.id}
            className={`flex gap-3 ${
              message.role === 'user' ? 'flex-row-reverse' : 'flex-row'
            }`}
          >
            <div
              className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
                message.role === 'user'
                  ? 'bg-neon-purple/20 text-neon-purple'
                  : 'bg-neon-blue/20 text-neon-blue'
              }`}
            >
              {message.role === 'user' ? (
                <User className="w-4 h-4" />
              ) : (
                <Bot className="w-4 h-4" />
              )}
            </div>

            <div
              className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                message.role === 'user'
                  ? 'bg-neon-purple/20 text-white'
                  : 'bg-space-700/50 text-gray-200'
              }`}
            >
              <div className="prose prose-sm max-w-none whitespace-pre-wrap">
                {message.content}
              </div>
            </div>
          </div>
        ))}

        {isTyping && displayedText && (
          <div className="flex gap-3">
            <div className="w-8 h-8 rounded-full bg-neon-blue/20 text-neon-blue flex items-center justify-center">
              <Bot className="w-4 h-4" />
            </div>
            <div className="bg-space-700/50 rounded-2xl px-4 py-3">
              <div className="prose prose-sm max-w-none whitespace-pre-wrap text-gray-200">
                {displayedText}
                <span className="typing-cursor text-neon-blue" />
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <div className="p-4 border-t border-neon-blue/10">
        <div className="flex gap-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="输入你的问题..."
            className="flex-1 bg-space-700/50 border border-neon-blue/20 rounded-xl px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-neon-blue/50 transition-colors"
            disabled={isTyping}
          />
          <button
            onClick={handleSend}
            disabled={!input.trim() || isTyping}
            className="px-4 py-3 bg-gradient-to-r from-neon-blue to-neon-purple rounded-xl text-white hover:shadow-[0_0_20px_rgba(0,212,255,0.5)] transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
}
