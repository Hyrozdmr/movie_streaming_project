import React, { useEffect, useState } from 'react';
import axios from 'axios';
import MovieCard from '../components/MovieCard';

const PopularPage = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchPopular = async () => {
      const response = await axios.get(`/popular/`, {
        params: { type: 'movie' },
      });
      setMovies(response.data);
    };
    fetchPopular();
  }, []);

  return (
    <div>
      <h1>Popular Movies</h1>
      <div className="movie-card">
        {movies.map((movie) => (
          <MovieCard key={movie.id} {...movie} />
        ))}
      </div>
    </div>
  );
};

export default PopularPage;
