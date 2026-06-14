import { useState } from 'react';
import { CheckCircle, XCircle, ChevronRight, Trophy } from 'lucide-react';
import { QuizQuestion } from '../../data/projects';
import { Highlight, themes } from 'prism-react-renderer';

interface QuizSectionProps {
  questions: QuizQuestion[];
  projectTitle: string;
}

interface QuestionState {
  selectedAnswer: string | null;
  isSubmitted: boolean;
  isCorrect: boolean;
}

export default function QuizSection({ questions, projectTitle }: QuizSectionProps) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [questionStates, setQuestionStates] = useState<Record<string, QuestionState>>({});
  const [showResults, setShowResults] = useState(false);

  const currentQuestion = questions[currentIndex];
  const state = questionStates[currentQuestion.id] || {
    selectedAnswer: null,
    isSubmitted: false,
    isCorrect: false,
  };

  const correctCount = Object.values(questionStates).filter((s) => s.isCorrect).length;
  const totalAnswered = Object.keys(questionStates).filter(
    (id) => questionStates[id].isSubmitted
  ).length;

  const handleSelectAnswer = (answer: string) => {
    if (state.isSubmitted) return;
    setQuestionStates((prev) => ({
      ...prev,
      [currentQuestion.id]: {
        ...prev[currentQuestion.id],
        selectedAnswer: answer,
        isSubmitted: false,
        isCorrect: false,
      },
    }));
  };

  const handleSubmit = () => {
    if (!state.selectedAnswer) return;
    const isCorrect = state.selectedAnswer === currentQuestion.correctAnswer;
    setQuestionStates((prev) => ({
      ...prev,
      [currentQuestion.id]: {
        ...prev[currentQuestion.id],
        isSubmitted: true,
        isCorrect,
      },
    }));
  };

  const handleNext = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setShowResults(true);
    }
  };

  const handleReset = () => {
    setCurrentIndex(0);
    setQuestionStates({});
    setShowResults(false);
  };

  if (showResults) {
    const percentage = Math.round((correctCount / questions.length) * 100);
    const isPassing = percentage >= 60;

    return (
      <div className="bg-space-800/50 rounded-2xl border border-neon-blue/20 p-8">
        <div className="text-center">
          <div
            className={`w-20 h-20 rounded-full mx-auto mb-6 flex items-center justify-center ${
              isPassing
                ? 'bg-neon-green/20 text-neon-green'
                : 'bg-neon-orange/20 text-neon-orange'
            }`}
          >
            <Trophy className="w-10 h-10" />
          </div>
          <h3 className="text-2xl font-bold text-white mb-2">
            {isPassing ? '恭喜通过！' : '继续加油！'}
          </h3>
          <p className="text-gray-400 mb-6">
            {projectTitle} - 训练测验结果
          </p>
          <div className="text-5xl font-bold mb-4">
            <span className={isPassing ? 'text-neon-green' : 'text-neon-orange'}>
              {percentage}%
            </span>
          </div>
          <p className="text-gray-400 mb-2">
            正确 {correctCount} / 总共 {questions.length} 题
          </p>
          <div className="flex justify-center gap-4 mb-8">
            <div className="px-4 py-2 rounded-lg bg-neon-green/20 text-neon-green">
              答对 {correctCount} 题
            </div>
            <div className="px-4 py-2 rounded-lg bg-neon-orange/20 text-neon-orange">
              答错 {questions.length - correctCount} 题
            </div>
          </div>
          <button
            onClick={handleReset}
            className="px-6 py-3 bg-gradient-to-r from-neon-blue to-neon-purple rounded-xl text-white font-medium hover:shadow-[0_0_25px_rgba(0,212,255,0.5)] transition-all"
          >
            重新测验
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-space-800/50 rounded-2xl border border-neon-blue/20 overflow-hidden">
      {/* Header */}
      <div className="bg-space-900/50 px-6 py-4 border-b border-neon-blue/10">
        <div className="flex items-center justify-between">
          <h3 className="text-lg font-semibold text-white">训练测验</h3>
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-400">
              第 {currentIndex + 1} / {questions.length} 题
            </span>
            <span className="text-sm text-gray-400">
              已答 {totalAnswered} 题
            </span>
          </div>
        </div>
        {/* Progress bar */}
        <div className="mt-3 h-2 bg-space-700 rounded-full overflow-hidden">
          <div
            className="h-full bg-gradient-to-r from-neon-blue to-neon-purple transition-all duration-300"
            style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }}
          />
        </div>
      </div>

      {/* Question content */}
      <div className="p-6">
        {/* Question type badge */}
        <div className="mb-4">
          <span
            className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium ${
              currentQuestion.type === 'choice'
                ? 'bg-neon-blue/20 text-neon-blue'
                : 'bg-neon-purple/20 text-neon-purple'
            }`}
          >
            {currentQuestion.type === 'choice' ? '选择题' : '代码连题'}
          </span>
        </div>

        {/* Question */}
        <h4 className="text-lg text-white mb-6">{currentQuestion.question}</h4>

        {/* Code snippet for code questions */}
        {currentQuestion.type === 'code' && currentQuestion.codeSnippet && (
          <div className="mb-6 rounded-xl overflow-hidden border border-neon-blue/20">
            <div className="bg-space-900/80 px-4 py-2 border-b border-neon-blue/10">
              <span className="text-xs text-gray-400 font-mono">代码片段</span>
            </div>
            <Highlight theme={themes.nightOwl} code={currentQuestion.codeSnippet} language="python">
              {({ className, style, tokens, getLineProps, getTokenProps }) => (
                <pre
                  className={`${className} overflow-x-auto p-4 text-sm`}
                  style={{ ...style, background: 'transparent' }}
                >
                  {tokens.map((line, i) => (
                    <div key={i} {...getLineProps({ line })}>
                      <span className="inline-block w-8 text-gray-600 select-none text-right mr-4">
                        {i + 1}
                      </span>
                      {line.map((token, key) => (
                        <span key={key} {...getTokenProps({ token })} />
                      ))}
                    </div>
                  ))}
                </pre>
              )}
            </Highlight>
          </div>
        )}

        {/* Options */}
        <div className="space-y-3">
          {(currentQuestion.type === 'choice' ? currentQuestion.options : currentQuestion.codeOptions)?.map(
            (option, index) => {
              const isSelected = state.selectedAnswer === option;
              const isCorrectOption = option === currentQuestion.correctAnswer;
              const showCorrect = state.isSubmitted && isCorrectOption;
              const showIncorrect = state.isSubmitted && isSelected && !isCorrectOption;

              return (
                <button
                  key={index}
                  onClick={() => handleSelectAnswer(option)}
                  disabled={state.isSubmitted}
                  className={`w-full text-left p-4 rounded-xl border transition-all duration-300 ${
                    showCorrect
                      ? 'border-neon-green bg-neon-green/20 text-neon-green'
                      : showIncorrect
                      ? 'border-neon-orange bg-neon-orange/20 text-neon-orange'
                      : isSelected
                      ? 'border-neon-blue bg-neon-blue/10 text-white'
                      : 'border-space-600 bg-space-700/30 text-gray-300 hover:border-neon-blue/50 hover:bg-neon-blue/5'
                  } ${state.isSubmitted ? 'cursor-default' : 'cursor-pointer'}`}
                >
                  <div className="flex items-center justify-between">
                    <span className="font-mono text-sm">{option}</span>
                    {showCorrect && <CheckCircle className="w-5 h-5 text-neon-green" />}
                    {showIncorrect && <XCircle className="w-5 h-5 text-neon-orange" />}
                  </div>
                </button>
              );
            }
          )}
        </div>

        {/* Feedback */}
        {state.isSubmitted && (
          <div
            className={`mt-6 p-4 rounded-xl border ${
              state.isCorrect
                ? 'border-neon-green/50 bg-neon-green/10'
                : 'border-neon-orange/50 bg-neon-orange/10'
            }`}
          >
            <div className="flex items-start gap-3">
              {state.isCorrect ? (
                <CheckCircle className="w-6 h-6 text-neon-green flex-shrink-0 mt-0.5" />
              ) : (
                <XCircle className="w-6 h-6 text-neon-orange flex-shrink-0 mt-0.5" />
              )}
              <div>
                <p className={`font-semibold mb-2 ${state.isCorrect ? 'text-neon-green' : 'text-neon-orange'}`}>
                  {state.isCorrect ? '回答正确！' : '回答错误'}
                </p>
                <p className="text-gray-300 text-sm leading-relaxed">
                  {currentQuestion.explanation}
                </p>
                {!state.isCorrect && (
                  <p className="text-neon-green text-sm mt-2">
                    正确答案: <span className="font-mono">{currentQuestion.correctAnswer}</span>
                  </p>
                )}
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Footer */}
      <div className="px-6 py-4 border-t border-neon-blue/10 bg-space-900/30 flex justify-between items-center">
        <button
          onClick={() => setCurrentIndex(Math.max(0, currentIndex - 1))}
          disabled={currentIndex === 0}
          className="px-4 py-2 text-gray-400 hover:text-white disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        >
          上一题
        </button>

        {!state.isSubmitted ? (
          <button
            onClick={handleSubmit}
            disabled={!state.selectedAnswer}
            className="px-6 py-2 bg-gradient-to-r from-neon-blue to-neon-purple rounded-xl text-white font-medium disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-[0_0_20px_rgba(0,212,255,0.4)] transition-all"
          >
            提交答案
          </button>
        ) : (
          <button
            onClick={handleNext}
            className="flex items-center gap-2 px-6 py-2 bg-gradient-to-r from-neon-blue to-neon-purple rounded-xl text-white font-medium hover:shadow-[0_0_20px_rgba(0,212,255,0.4)] transition-all"
          >
            {currentIndex < questions.length - 1 ? (
              <>
                下一题
                <ChevronRight className="w-4 h-4" />
              </>
            ) : (
              '查看结果'
            )}
          </button>
        )}
      </div>
    </div>
  );
}
