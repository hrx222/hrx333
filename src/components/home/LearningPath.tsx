import { Link } from 'react-router-dom';
import { projects } from '../../data/projects';
import { Badge } from '../common/Tag';
import { CheckCircle } from 'lucide-react';

export default function LearningPath() {
  return (
    <section className="py-20 relative">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-mono font-bold text-white mb-4">
            学习路径
          </h2>
          <p className="text-gray-400 max-w-2xl mx-auto">
            从入门到高级，10个项目带你系统掌握数据分析技能
          </p>
        </div>

        <div className="relative">
          {/* Timeline line */}
          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-1 h-full bg-gradient-to-b from-neon-blue via-neon-purple to-neon-green opacity-30 rounded-full hidden lg:block" />

          <div className="space-y-8">
            {projects.map((project, index) => (
              <div
                key={project.id}
                className={`flex items-center gap-8 ${
                  index % 2 === 0 ? 'lg:flex-row' : 'lg:flex-row-reverse'
                } flex-col lg:flex-row`}
              >
                {/* Timeline node */}
                <div className="hidden lg:flex flex-col items-center">
                  <div className="w-4 h-4 rounded-full bg-neon-blue shadow-[0_0_15px_rgba(0,212,255,0.8)] z-10" />
                  {index < projects.length - 1 && (
                    <div className="w-0.5 h-16 bg-gradient-to-b from-neon-blue/50 to-transparent" />
                  )}
                </div>

                {/* Content card */}
                <Link
                  to={`/projects/${project.id}`}
                  className={`flex-1 group ${
                    index % 2 === 0 ? 'lg:text-right' : 'lg:text-left'
                  }`}
                >
                  <div className="bg-space-800/50 backdrop-blur-sm border border-neon-blue/20 rounded-2xl p-6 hover:border-neon-blue/50 hover:shadow-[0_0_30px_rgba(0,212,255,0.15)] transition-all duration-300 card-hover">
                    <div className={`flex items-center gap-3 mb-3 ${
                      index % 2 === 0 ? 'lg:justify-end' : 'lg:justify-start'
                    }`}>
                      <span className="text-neon-blue font-mono text-sm">
                        项目 {index + 1}
                      </span>
                      <Badge difficulty={project.difficulty} />
                    </div>

                    <h3 className="text-xl font-bold text-white group-hover:text-neon-blue transition-colors mb-2">
                      {project.title}
                    </h3>

                    <p className="text-gray-400 text-sm mb-4 line-clamp-2">
                      {project.description}
                    </p>

                    <div className={`flex flex-wrap gap-2 ${
                      index % 2 === 0 ? 'lg:justify-end' : 'lg:justify-start'
                    }`}>
                      {project.techStack.slice(0, 3).map((tech) => (
                        <span
                          key={tech}
                          className="px-2 py-1 bg-space-700/50 rounded text-xs text-gray-300 font-mono"
                        >
                          {tech}
                        </span>
                      ))}
                    </div>
                  </div>
                </Link>

                {/* Empty space for alternating layout */}
                <div className="hidden lg:block flex-1" />
              </div>
            ))}
          </div>

          {/* Completion node */}
          <div className="flex flex-col items-center mt-8">
            <div className="w-0.5 h-8 bg-gradient-to-b from-neon-green/50 to-transparent" />
            <div className="flex items-center gap-2 text-neon-green">
              <CheckCircle className="w-6 h-6" />
              <span className="font-mono font-semibold">完成全部项目</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
