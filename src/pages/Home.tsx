import Hero from '../components/home/Hero';
import LearningPath from '../components/home/LearningPath';
import ProjectCard from '../components/home/ProjectCard';
import { projects } from '../data/projects';

export default function Home() {
  const featuredProjects = projects.slice(0, 6);

  return (
    <div className="min-h-screen">
      <Hero />
      <LearningPath />

      <section className="py-20 bg-space-800/30">
        <div className="container mx-auto px-6">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-mono font-bold text-white mb-4">
              热门项目
            </h2>
            <p className="text-gray-400 max-w-2xl mx-auto">
              从入门到高级，选择适合你的学习项目开始数据分析之旅
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {featuredProjects.map((project, index) => (
              <div
                key={project.id}
                className="animate-slide-up"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <ProjectCard project={project} />
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
