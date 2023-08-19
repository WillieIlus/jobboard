import { defingStore } from 'pinia';

export const useUserStore = defingStore({
  id: 'user',
  state: () => ({
    user: {
      isAuthenticated: false,
      email: null,
      token: null,
      username: null,
    },
  }),
  actions: {
    initStore() {
      this.user.isAuthenticated = false;
      if (localStorage.getItem('user.token')) {
        this.user.isAuthenticated = true;
        this.user.token = localStorage.getItem('user.token');
        this.user.email = localStorage.getItem('user.email');
        this.user.username = localStorage.getItem('user.username');
        console.log('Initialized user:', this.user);
      }
    },
    setToken(token, username) {
      console.log('SetToken:', token, username);
      this.user.isAuthenticated = true;
      this.user.token = token;
      this.user.username = username;

      localStorage.setItem('user.token', token);
      localStorage.setItem('user.email', this.user.email);
      localStorage.setItem('user.username', this.user.username);
    },
    removeToken() {
      console.log('Removing token');
      this.user.isAuthenticated = false;
      this.user.token = null;
      this.user.email = null;
      this.user.username = null;

      localStorage.removeItem('user.token');
      localStorage.removeItem('user.email');
      localStorage.removeItem('user.username');


    }
  }
})

