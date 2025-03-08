import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const authApi = {
  login: async (email, password) => {
    const response = await axios.post(`${API_URL}/users/login/`, { email, password });
    return response.data;
  },

  logout: async () => {
    await axios.post(`${API_URL}/users/logout/`);
  },

  register: async (username, email, password) => {
    const response = await axios.post(`${API_URL}/users/register/`, { username, email, password });
    return response.data;
  },

  getCurrentUser: async () => {
    const response = await axios.get(`${API_URL}/users/me/`);
    return response.data;
  },
};