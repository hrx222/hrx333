import { difficultyColors } from '../../data/projects';

interface TagProps {
  children: React.ReactNode;
  className?: string;
}

export function Tag({ children, className = '' }: TagProps) {
  return (
    <span className={`inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium bg-neon-blue/10 text-neon-blue border border-neon-blue/30 ${className}`}>
      {children}
    </span>
  );
}

interface BadgeProps {
  difficulty: '入门' | '初级' | '中级' | '高级';
  className?: string;
}

export function Badge({ difficulty, className = '' }: BadgeProps) {
  const colors = difficultyColors[difficulty] || difficultyColors['入门'];

  return (
    <span className={`inline-flex items-center px-3 py-1 rounded-lg text-sm font-medium border ${colors} ${className}`}>
      {difficulty}
    </span>
  );
}
