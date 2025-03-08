import React, { useEffect, useState } from 'react';
import axios from 'axios';
import MovieCard from './MovieCard';
import TVShowCard from './TVShowCard';

const Watchlist = () => {
  const [watchlist, setWatchlist] = useState([]);

  useEffect(() => {
    const fetchWatchlist = async () => {
      const token = localStorage.getItem('authToken'); // Assume token is stored
      const response = await axios.get('/watchlist/', {
        headers: { Authorization: `Bearer ${token}` },
      });
      setWatchlist(response.data);
    };
    fetchWatchlist();
  }, []);

  return (
    <div>
      <h2>My Watchlist</h2>
      {watchlist.length === 0 ? (
        <p>No items in your watchlist.</p>
      ) : (
        <div className="watchlist-grid">
          {watchlist.map((item) =>
            item.media_type === 'movie' ? (
              <MovieCard key={item.id} {...item} />
            ) : (
              <TVShowCard key={item.id} {...item} />
            )
          )}
        </div>
      )}
    </div>
  );
};

export default Watchlist;