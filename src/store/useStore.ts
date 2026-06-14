import { create } from 'zustand';
import { Project, ChatMessage } from '../data/projects';

interface AppState {
  selectedProject: Project | null;
  chatMessages: ChatMessage[];
  filterDifficulty: string | null;
  filterTag: string | null;
  setSelectedProject: (project: Project | null) => void;
  addChatMessage: (message: ChatMessage) => void;
  clearChatMessages: () => void;
  setFilter: (difficulty: string | null, tag: string | null) => void;
}

export const useStore = create<AppState>((set) => ({
  selectedProject: null,
  chatMessages: [],
  filterDifficulty: null,
  filterTag: null,

  setSelectedProject: (project) => set({ selectedProject: project }),

  addChatMessage: (message) =>
    set((state) => ({
      chatMessages: [...state.chatMessages, message],
    })),

  clearChatMessages: () => set({ chatMessages: [] }),

  setFilter: (difficulty, tag) =>
    set({
      filterDifficulty: difficulty,
      filterTag: tag,
    }),
}));
