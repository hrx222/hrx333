import { X } from 'lucide-react';
import { difficultyColors } from '../../data/projects';

interface ProjectFilterProps {
  selectedDifficulty: string | null;
  selectedTech: string | null;
  onDifficultyChange: (difficulty: string | null) => void;
  onTechChange: (tech: string | null) => void;
  difficulties: string[];
  techs: string[];
}

export default function ProjectFilter({
  selectedDifficulty,
  selectedTech,
  onDifficultyChange,
  onTechChange,
  difficulties,
  techs,
}: ProjectFilterProps) {
  const clearFilters = () => {
    onDifficultyChange(null);
    onTechChange(null);
  };

  const hasFilters = selectedDifficulty || selectedTech;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-mono font-semibold text-white">筛选条件</h3>
        {hasFilters && (
          <button
            onClick={clearFilters}
            className="flex items-center gap-1 text-sm text-gray-400 hover:text-white transition-colors"
          >
            <X className="w-4 h-4" />
            清除筛选
          </button>
        )}
      </div>

      <div>
        <h4 className="text-sm text-gray-400 mb-3">难度等级</h4>
        <div className="flex flex-wrap gap-2">
          {difficulties.map((diff) => {
            const isSelected = selectedDifficulty === diff;
            const colors = difficultyColors[diff];
            return (
              <button
                key={diff}
                onClick={() => onDifficultyChange(isSelected ? null : diff)}
                className={`px-4 py-2 rounded-lg text-sm font-medium border transition-all duration-300 ${
                  isSelected
                    ? `${colors} shadow-[0_0_15px_rgba(0,212,255,0.3)]`
                    : 'bg-space-800/50 border-neon-blue/20 text-gray-400 hover:text-white hover:border-neon-blue/50'
                }`}
              >
                {diff}
              </button>
            );
          })}
        </div>
      </div>

      <div>
        <h4 className="text-sm text-gray-400 mb-3">技术栈</h4>
        <div className="flex flex-wrap gap-2">
          {techs.map((tech) => {
            const isSelected = selectedTech === tech;
            return (
              <button
                key={tech}
                onClick={() => onTechChange(isSelected ? null : tech)}
                className={`px-4 py-2 rounded-lg text-sm font-mono border transition-all duration-300 ${
                  isSelected
                    ? 'bg-neon-blue/20 text-neon-blue border-neon-blue shadow-[0_0_15px_rgba(0,212,255,0.3)]'
                    : 'bg-space-800/50 border-neon-blue/20 text-gray-400 hover:text-white hover:border-neon-blue/50'
                }`}
              >
                {tech}
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
