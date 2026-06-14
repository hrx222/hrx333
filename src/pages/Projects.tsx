import { useState, useMemo } from 'react';
import { useStore } from '../store/useStore';
import { projects, allTechStack } from '../data/projects';
import ProjectFilter from '../components/projects/ProjectFilter';
import ProjectGrid from '../components/projects/ProjectGrid';
import { BookOpen } from 'lucide-react';

const difficulties = ['入门', '初级', '中级', '高级'];

export default function Projects() {
  const { filterDifficulty, filterTag, setFilter } = useStore();
  const [showFilters, setShowFilters] = useState(false);

  const filteredProjects = useMemo(() => {
    return projects.filter((project) => {
      if (filterDifficulty && project.difficulty !== filterDifficulty) {
        return false;
      }
      if (filterTag && !project.techStack.includes(filterTag)) {
        return false;
      }
      return true;
    });
  }, [filterDifficulty, filterTag]);

  return (
    <div className="min-h-screen pt-20">
      <div className="container mx-auto px-6 py-12">
        <div className="text-center mb-12">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-neon-blue/10 border border-neon-blue/30 text-neon-blue text-sm font-medium mb-6">
            <BookOpen className="w-4 h-4" />
            <span>10个训练项目</span>
          </div>
          <h1 className="text-4xl md:text-5xl font-mono font-bold text-white mb-4">
            训练项目
          </h1>
          <p className="text-gray-400 max-w-2xl mx-auto">
            从探索性数据分析到机器学习，循序渐进掌握数据分析核心技能
          </p>
        </div>

        <div className="lg:flex lg:gap-12">
          {/* Mobile filter toggle */}
          <button
            onClick={() => setShowFilters(!showFilters)}
            className="lg:hidden w-full mb-6 px-4 py-3 bg-space-800/50 border border-neon-blue/20 rounded-xl text-white"
          >
            {showFilters ? '隐藏筛选' : '显示筛选'}
          </button>

          {/* Sidebar filter */}
          <aside
            className={`lg:w-64 flex-shrink-0 ${
              showFilters ? 'block' : 'hidden lg:block'
            }`}
          >
            <div className="lg:sticky lg:top-24">
              <ProjectFilter
                selectedDifficulty={filterDifficulty}
                selectedTech={filterTag}
                onDifficultyChange={(d) => setFilter(d, filterTag)}
                onTechChange={(t) => setFilter(filterDifficulty, t)}
                difficulties={difficulties}
                techs={allTechStack}
              />
            </div>
          </aside>

          {/* Project grid */}
          <main className="flex-1">
            <div className="mb-6 text-gray-400 text-sm">
              共找到 <span className="text-neon-blue font-semibold">{filteredProjects.length}</span> 个项目
            </div>
            <ProjectGrid projects={filteredProjects} />
          </main>
        </div>
      </div>
    </div>
  );
}
