import { defineStore } from 'pinia';
import { LocalStorage } from 'quasar';

const actors = [
  { user: 'admin', id: 1 },
  { user: 'producer', id: 2 },
  { user: 'mentor', id: 3 },
  { user: 'purchaser', id: 4 },
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
