import { Link } from 'react-router-dom';
import { Clock, ArrowRight } from 'lucide-react';
import { Project } from '../../data/projects';
import { Badge, Tag } from '../common/Tag';

interface ProjectCardProps {
  project: Project;
}

export default function ProjectCard({ project }: ProjectCardProps) {
  return (
    <Link to={`/projects/${project.id}`} className="group block">
      <div className="bg-space-800/50 backdrop-blur-sm border border-neon-blue/20 rounded-2xl p-6 h-full hover:border-neon-blue/50 transition-all duration-300 card-hover gradient-border">
        <div className="flex items-start justify-between mb-4">
          <Badge difficulty={project.difficulty} />
          <div className="flex items-center gap-1 text-gray-500 text-sm">
            <Clock className="w-4 h-4" />
            <span>{project.duration}</span>
          </div>
        </div>

        <h3 className="text-xl font-bold text-white group-hover:text-neon-blue transition-colors mb-2 line-clamp-2">
          {project.title}
        </h3>

        <p className="text-gray-400 text-sm mb-4 line-clamp-3">
          {project.description}
        </p>

        <div className="flex flex-wrap gap-2 mb-4">
          {project.techStack.slice(0, 3).map((tech) => (
            <Tag key={tech}>{tech}</Tag>
          ))}
        </div>

        <div className="flex items-center gap-2 text-neon-blue text-sm font-medium opacity-0 group-hover:opacity-100 transition-opacity">
          <span>查看详情</span>
          <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
        </div>
      </div>
    </Link>
  );
}
