import React, { useEffect, useState } from 'react';
import axios from 'axios';
import MovieCard from '../components/MovieCard';

const NowPlaying = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchNowPlaying = async () => {
      const response = await axios.get(`/nowplaying/`, {
        params: { type: 'movie' },
      });
      setMovies(response.data);
    };
    fetchNowPlaying();
  }, []);

  return (
    <div>
      <h1>Now Playing Movies</h1>
      <div className="movie-card">
        {movies.map((movie) => (
          <MovieCard key={movie.id} {...movie} />
        ))}
      </div>
    </div>
  );
};

export default NowPlaying;
