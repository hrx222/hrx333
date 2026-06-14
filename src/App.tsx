import { HashRouter, Routes, Route } from 'react-router-dom';
import Header from './components/layout/Header';
import Footer from './components/layout/Footer';
import Home from './pages/Home';
import Projects from './pages/Projects';
import ProjectDetail from './pages/ProjectDetail';
import AITutor from './pages/AITutor';
import CodePlayground from './components/common/CodePlayground';

function App() {
  return (
    <HashRouter>
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/projects/:id" element={<ProjectDetail />} />
            <Route path="/ai-tutor" element={<AITutor />} />
          </Routes>
        </main>
        <Footer />
        <CodePlayground />
      </div>
    </HashRouter>
  );
}

export default App;
