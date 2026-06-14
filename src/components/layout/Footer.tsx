import { BarChart3, Github, Mail } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <footer className="bg-space-800/50 border-t border-neon-blue/10 py-12 mt-20">
      <div className="container mx-auto px-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="col-span-1 md:col-span-2">
            <Link to="/" className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-neon-blue to-neon-purple flex items-center justify-center">
                <BarChart3 className="w-6 h-6 text-white" />
              </div>
              <span className="font-mono font-bold text-lg text-white">
                PyData<span className="text-neon-blue">AI</span>
              </span>
            </Link>
            <p className="text-gray-400 text-sm leading-relaxed max-w-md">
              PyData AI Trainer 是一款专为数据分析学习者设计的AI辅助训练平台。
              通过10个循序渐进的项目，帮助你掌握从基础统计到机器学习的核心技能。
            </p>
          </div>

          <div>
            <h4 className="font-mono font-semibold text-white mb-4">快速链接</h4>
            <ul className="space-y-2">
              <li>
                <Link to="/projects" className="text-gray-400 hover:text-neon-blue transition-colors text-sm">
                  训练项目
                </Link>
              </li>
              <li>
                <Link to="/ai-tutor" className="text-gray-400 hover:text-neon-blue transition-colors text-sm">
                  AI导师
                </Link>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="font-mono font-semibold text-white mb-4">联系我们</h4>
            <div className="flex gap-4">
              <a href="#" className="text-gray-400 hover:text-neon-blue transition-colors">
                <Github className="w-5 h-5" />
              </a>
              <a href="#" className="text-gray-400 hover:text-neon-blue transition-colors">
                <Mail className="w-5 h-5" />
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-neon-blue/10 mt-8 pt-8 text-center">
          <p className="text-gray-500 text-sm">
            © 2024 PyData AI Trainer. 为数据分析师而生。
          </p>
        </div>
      </div>
    </footer>
  );
}
