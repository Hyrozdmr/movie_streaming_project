import React from 'react';
import { useNavigate } from 'react-router-dom';
import useWatchlist from '../hooks/useWatchlist';

const MovieCard = ({ movie }) => {
    const navigate = useNavigate();
    const { addToWatchlist, removeFromWatchlist, watchlist} = useWatchlist();

    const isInWatchlist = watchlist.some((m) => m.id === movie.id);

    const handleWatchlistClick = () => {
        if (isInWatchlist) {
            removeFromWatchlist(movie);
        } else {
            addToWatchlist(movie);
        }
    };

    return (
        <div className='movie-card'>
            <img src={movie.poster_path} alt={movie.title} />
            <h3>{movie.title}</h3>
            <p>{movie.overview}</p>
            <button onClick={() => navigate(`/movie/${movie.id}`)}>View Details</button>
            <button onClick={handleWatchlistClick}>
                {isInWatchlist ? 'remove from Watchlist' : 'Add to Watchlist'}
            </button>
        </div>
    );
};

export default MovieCard;