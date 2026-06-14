import ProjectCard from '../home/ProjectCard';
import { Project } from '../../data/projects';
import { BarChart3 } from 'lucide-react';

interface ProjectGridProps {
  projects: Project[];
}

export default function ProjectGrid({ projects }: ProjectGridProps) {
  if (projects.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-20 text-center">
        <BarChart3 className="w-16 h-16 text-gray-600 mb-4" />
        <h3 className="text-xl font-semibold text-gray-400 mb-2">没有找到匹配的项目</h3>
        <p className="text-gray-500">尝试调整筛选条件</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {projects.map((project, index) => (
        <div
          key={project.id}
          className="animate-slide-up"
          style={{ animationDelay: `${index * 0.1}s` }}
        >
          <ProjectCard project={project} />
        </div>
      ))}
    </div>
  );
}
