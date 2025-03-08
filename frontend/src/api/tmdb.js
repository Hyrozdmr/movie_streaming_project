import axios from 'axios';


const API_BASE_URL = 'http://localhost:8000/api';

export const tmdbAPi = {
    fetchMovies: async (category) => {
        const response = await axios.get(`${API_BASE_URL}/movies/${category}/`);
        return response.data;
    },

    searchMedia: async (query) => {
        const response = await axios.get(`${API_BASE_URL}/search/?query=${query}`);
        return response.data;
    },

    addToWatchlist: async (mediaData) => {
        const response = await axios.post(`${API_BASE_URL}/watchlist/`, mediaData);
        return response.data;
    }
};