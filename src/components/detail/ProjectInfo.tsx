import { Clock, Target, BookOpen, Layers } from 'lucide-react';
import { Project } from '../../data/projects';
import { Badge, Tag } from '../common/Tag';

interface ProjectInfoProps {
  project: Project;
}

export default function ProjectInfo({ project }: ProjectInfoProps) {
  return (
    <div className="space-y-8">
      <div>
        <div className="flex items-center gap-4 mb-4">
          <Badge difficulty={project.difficulty} />
          <div className="flex items-center gap-1 text-gray-400">
            <Clock className="w-4 h-4" />
            <span>{project.duration}</span>
          </div>
        </div>

        <h1 className="text-4xl font-mono font-bold text-white mb-4">
          {project.title}
        </h1>
        <p className="text-gray-400 text-lg">{project.titleEn}</p>
      </div>

      <div className="bg-space-800/30 rounded-xl p-6 border border-neon-blue/10">
        <h2 className="text-xl font-semibold text-white mb-4">项目描述</h2>
        <p className="text-gray-300 leading-relaxed">{project.description}</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-space-800/30 rounded-xl p-6 border border-neon-blue/10">
          <div className="flex items-center gap-3 mb-4">
            <Target className="w-5 h-5 text-neon-green" />
            <h2 className="text-xl font-semibold text-white">学习目标</h2>
          </div>
          <ul className="space-y-3">
            {project.objectives.map((obj, index) => (
              <li key={index} className="flex items-start gap-3 text-gray-300">
                <span className="w-6 h-6 rounded-full bg-neon-green/20 text-neon-green text-sm flex items-center justify-center flex-shrink-0 mt-0.5">
                  {index + 1}
                </span>
                <span>{obj}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="bg-space-800/30 rounded-xl p-6 border border-neon-blue/10">
          <div className="flex items-center gap-3 mb-4">
            <BookOpen className="w-5 h-5 text-neon-orange" />
            <h2 className="text-xl font-semibold text-white">前置知识</h2>
          </div>
          <ul className="space-y-3">
            {project.prerequisites.map((pre, index) => (
              <li key={index} className="flex items-start gap-3 text-gray-300">
                <span className="w-6 h-6 rounded-full bg-neon-orange/20 text-neon-orange text-sm flex items-center justify-center flex-shrink-0">
                  {index + 1}
                </span>
                <span>{pre}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div className="bg-space-800/30 rounded-xl p-6 border border-neon-blue/10">
        <div className="flex items-center gap-3 mb-4">
          <Layers className="w-5 h-5 text-neon-purple" />
          <h2 className="text-xl font-semibold text-white">技术栈</h2>
        </div>
        <div className="flex flex-wrap gap-2">
          {project.techStack.map((tech) => (
            <Tag key={tech}>{tech}</Tag>
          ))}
        </div>
      </div>
    </div>
  );
}
