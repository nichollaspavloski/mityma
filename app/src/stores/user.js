import { defineStore } from 'pinia';
import { LocalStorage } from 'quasar';

const actors = [
  { user: 'admin', id: 1 },
  { user: 'produtor', id: 2 },
  { user: 'mentor', id: 3 },
  { user: 'comsumidor', id: 4 },
];

export const useUserStore = defineStore('user', {
  state: () => ({
    user: { user: null, id: null },
  }),

  getters: {
    getUsers() {
      return actors;
    },
    getUser(state) {
      if (!state.user.id) {
        const user = LocalStorage.getItem('user');
        if (!user) return { user: null, id: null };
        return user;
      }
      return state.user;
    },
  },

  actions: {
    setUser(user) {
      LocalStorage.set('user', user);
      this.user = user;
    },
  },
});
