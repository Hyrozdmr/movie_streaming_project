import React, { useState, useEffect } from 'react';
import { tmdbApi } from '../api/tmdb';
import MovieCard from '../components/MovieCard';

const HomePage = () => {
  const [activeTab, setActiveTab] = useState('movie');
  const [category, setCategory] = useState('popular');
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await tmdbApi.fetchMovies(category);
      setMovies(data.results);
    };
    fetchData();
  }, [category, activeTab]);

  return (
    <div className="bg-gray-900 min-h-screen">
      <div className="container mx-auto">
        <div className="flex space-x-4 p-4">
          <button
            className={`px-4 py-2 rounded ${
              activeTab === 'movie' ? 'bg-yellow-500' : 'bg-gray-700'
            }`}
            onClick={() => setActiveTab('movie')}
          >
            Movies
          </button>
          <button
            className={`px-4 py-2 rounded ${
              activeTab === 'tv' ? 'bg-yellow-500' : 'bg-gray-700'
            }`}
            onClick={() => setActiveTab('tv')}
          >
            TV Shows
          </button>
        </div>

        <div className="flex space-x-4 p-4">
          {['popular', 'now_playing', 'upcoming'].map((cat) => (
            <button
              key={cat}
              className={`px-4 py-2 rounded ${
                category === cat ? 'bg-yellow-500' : 'bg-gray-700'
              }`}
              onClick={() => setCategory(cat)}
            >
              {cat.replace('_', ' ').toUpperCase()}
            </button>
          ))}
        </div>

        <MovieCard movies={movies} />
      </div>
    </div>
  );
};

export default HomePage;