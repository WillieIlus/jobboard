import { defineStore } from 'pinia'

const BASE_URL = 'http://127.0.0.1:8000';

export const useAccountsStore = defineStore({
  'id':'user',
  state: () => ({
    user: {
      isAuthenticated: false,
      username: 'null',
      email: 'null',
      token: 'null',
    },
    errors: [],

  }),
  getters: {
    getUser: (state) => {
      return state.user;
    }
  },
  actions: {
    initStore() {
      this.user.isAuthenticated = false;
      if (localStorage.getItem('user.token')) {
        this.user.token = localStorage.getItem('user.token');
        this.user.username = localStorage.getItem('user.username');
        this.user.isAuthenticated = true;

        console.log('initStore: ', this.user, this.user.isAuthenticated, this.user.token);
      }
    },
    // setToken(token, username) {
    //   this.user.token = token;
    //   this.user.username = username;
    //   this.user.isAuthenticated = true;

    //   localStorage.setItem('user.token', token);
    //   localStorage.setItem('user.username', username);
    // },
    // removeToken() {
    //   this.user.token = null;
    //   this.user.username = null;
    //   this.user.isAuthenticated = false;

    //   localStorage.removeItem('user.token', '');
    //   localStorage.removeItem('user.username', '');
    // },
    async login(user) {
      try {
        const response = await fetch(`${BASE_URL}/accounts/auth/token/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(user),
        })
        if (response.status === 401) {
          console.log(response) 
        }
        if (!response.ok) {
          throw new Error('Invalid credentials');
        }
        const data = await response.json();
        console.log('login: ', data);
        if (data.access) {
          this.setToken(data.access, username);
        }
        return data;
      } catch (error) {
        console.log(error);
      }
    },
    async register(username, email, password){ //, re_password) {
      try {
        const response = await fetch('http://127.0.0.1:8000/accounts/auth/users/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ username, email, password,}),// re_password }),
        });
        const data = await response.json();
        console.log('register: ', data);
        
        if (data.access) {
          this.setToken(data.access, username);
        }
        return data;
      } catch (error) {
        console.log(error);

      }
    },
    async getUserInfo() {
      try {
        const response = await fetch(`${BASE_URL}/accounts/auth/users/me`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${this.user.token}`
          },
        });
        const data = await response.json();
        console.log('getUserInfo: ', data);
        return data;
      } catch (error) {
        // console.log(error);
      }
    },
    async logout() {
      try {
        const response = await fetch(`${BASE_URL}/accounts/auth/token/logout/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ token: this.user.token })
        });
        const data = await response.json();
        console.log('logout: ', data);
        if (data.detail === 'Successfully logged out.') {
          this.removeToken();
        }
        return data;
      }
      catch (error) {

      }
    },
  }
})