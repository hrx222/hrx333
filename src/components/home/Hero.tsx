import { Link } from 'react-router-dom';
import { ArrowRight, Sparkles } from 'lucide-react';
import Button from '../common/Button';

export default function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden grid-bg">
      {/* Floating data elements */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        {[...Array(20)].map((_, i) => (
          <div
            key={i}
            className="absolute w-2 h-2 bg-neon-blue/30 rounded-full animate-float"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 6}s`,
              animationDuration: `${4 + Math.random() * 4}s`,
            }}
          />
        ))}
      </div>

      {/* Gradient orbs */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-neon-blue/20 rounded-full blur-[120px] animate-pulse" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-neon-purple/20 rounded-full blur-[120px] animate-pulse" style={{ animationDelay: '1s' }} />

      <div className="container mx-auto px-6 relative z-10">
        <div className="max-w-4xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-neon-blue/10 border border-neon-blue/30 text-neon-blue text-sm font-medium mb-8 animate-fade-in">
            <Sparkles className="w-4 h-4" />
            <span>AI驱动的数据分析学习平台</span>
          </div>

          <h1 className="text-5xl md:text-7xl font-mono font-bold mb-6 animate-slide-up">
            <span className="bg-gradient-to-r from-white via-neon-blue to-neon-purple bg-clip-text text-transparent">
              Python数据分析
            </span>
            <br />
            <span className="text-white">AI训练平台</span>
          </h1>

          <p className="text-xl text-gray-400 mb-10 max-w-2xl mx-auto leading-relaxed animate-slide-up" style={{ animationDelay: '0.2s' }}>
            通过10个循序渐进的学习项目，从探索性数据分析到机器学习，
            配合AI智能导师，让你在实践中掌握数据分析核心技能。
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center animate-slide-up" style={{ animationDelay: '0.4s' }}>
            <Link to="/projects">
              <Button size="lg" className="w-full sm:w-auto">
                开始学习
                <ArrowRight className="w-5 h-5" />
              </Button>
            </Link>
            <Link to="/ai-tutor">
              <Button variant="secondary" size="lg" className="w-full sm:w-auto">
                <Sparkles className="w-5 h-5" />
                AI导师
              </Button>
            </Link>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-3 gap-8 mt-16 pt-16 border-t border-neon-blue/10 animate-fade-in" style={{ animationDelay: '0.6s' }}>
            <div className="text-center">
              <div className="text-4xl font-mono font-bold text-neon-blue mb-2">10</div>
              <div className="text-gray-400 text-sm">训练项目</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-mono font-bold text-neon-purple mb-2">6+</div>
              <div className="text-gray-400 text-sm">核心技能</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-mono font-bold text-neon-green mb-2">24/7</div>
              <div className="text-gray-400 text-sm">AI辅导</div>
            </div>
          </div>
        </div>
      </div>

      {/* Scroll indicator */}
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
        <div className="w-6 h-10 rounded-full border-2 border-neon-blue/50 flex items-start justify-center p-2">
          <div className="w-1 h-3 bg-neon-blue rounded-full animate-pulse" />
        </div>
      </div>
    </section>
  );
}
