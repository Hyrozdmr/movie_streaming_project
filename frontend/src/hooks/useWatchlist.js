import { useContext, useState, useEffect } from 'react';
import axios from 'axios';
import { AuthContext } from '../contexts/AuthContext';

const useWatchlist = () => {
  const { user } = useContext(AuthContext);
  const [watchlist, setWatchlist] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWatchlist = async () => {
      if (!user) return;
      setIsLoading(true);
      setError(null);
      try {
        const response = await axios.get('/api/users/watchlist/', {
          headers: { Authorization: `Bearer ${user.token}` },
        });
        setWatchlist(response.data);
      } catch (err) {
        setError('Error fetching watchlist.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchWatchlist();
  }, [user]);

  const addToWatchlist = async (item) => {
    if (watchlist.some((i) => i.id === item.id)) return;
    try {
      await axios.post('/api/users/watchlist/', { item_id: item.id });
      setWatchlist([...watchlist, item]);
    } catch (err) {
      setError('Error adding to watchlist.');
    }
  };

  const removeFromWatchlist = async (id) => {
    try {
      await axios.delete(`/api/users/watchlist/${id}/`);
      setWatchlist(watchlist.filter((item) => item.id !== id));
    } catch (err) {
      setError('Error removing from watchlist.');
    }
  };

  return { watchlist, isLoading, error, addToWatchlist, removeFromWatchlist };
};

export default useWatchlist;
