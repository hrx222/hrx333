import { useParams, Link } from 'react-router-dom';
import { ArrowLeft, Bot, ClipboardList } from 'lucide-react';
import { projects } from '../data/projects';
import { useStore } from '../store/useStore';
import ProjectInfo from '../components/detail/ProjectInfo';
import CodeBlock from '../components/detail/CodeBlock';
import AIChat from '../components/detail/AIChat';
import QuizSection from '../components/detail/QuizSection';
import Button from '../components/common/Button';

export default function ProjectDetail() {
  const { id } = useParams<{ id: string }>();
  const project = projects.find((p) => p.id === id);
  const setSelectedProject = useStore((state) => state.setSelectedProject);

  if (!project) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-white mb-4">项目未找到</h2>
          <Link to="/projects">
            <Button variant="secondary">返回项目列表</Button>
          </Link>
        </div>
      </div>
    );
  }

  setSelectedProject(project);

  return (
    <div className="min-h-screen pt-20">
      <div className="container mx-auto px-6 py-12">
        <Link
          to="/projects"
          className="inline-flex items-center gap-2 text-gray-400 hover:text-white transition-colors mb-8"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>返回项目列表</span>
        </Link>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
          <div className="lg:col-span-2 space-y-12">
            <ProjectInfo project={project} />

            {/* Theory section */}
            <div className="bg-space-800/30 rounded-xl p-6 border border-neon-blue/10">
              <h2 className="text-xl font-semibold text-white mb-4">理论知识</h2>
              <div className="prose prose-invert max-w-none">
                {project.content.theory.split('\n\n').map((paragraph, index) => (
                  <p key={index} className="text-gray-300 leading-relaxed mb-4">
                    {paragraph}
                  </p>
                ))}
              </div>
            </div>

            {/* Code example */}
            <div>
              <h2 className="text-xl font-semibold text-white mb-4">代码示例</h2>
              <CodeBlock
                code={project.content.codeExample.code}
                language={project.content.codeExample.language}
              />
            </div>

            {/* Quiz section */}
            {project.quiz && project.quiz.length > 0 && (
              <div>
                <div className="flex items-center gap-3 mb-4">
                  <ClipboardList className="w-5 h-5 text-neon-purple" />
                  <h2 className="text-xl font-semibold text-white">训练测验</h2>
                </div>
                <QuizSection questions={project.quiz} projectTitle={project.title} />
              </div>
            )}
          </div>

          {/* AI Chat sidebar */}
          <div className="lg:col-span-1">
            <div className="lg:sticky lg:top-24">
              <div className="flex items-center gap-3 mb-4">
                <Bot className="w-5 h-5 text-neon-blue" />
                <h2 className="text-xl font-semibold text-white">AI 导师</h2>
              </div>
              <AIChat />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
