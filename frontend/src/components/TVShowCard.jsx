import React from 'react';
import { useNavigate } from 'react-router-dom';
import useWatchlist from '../hooks/useWatchlist';

const TVShowCard = ({ tvShow }) => {
    const navigate = useNavigate();
    const { addToWatchlist, removeFromWatchlist, watchlist} = useWatchlist();

    const isInWatchlist = watchlist.some((show) => show.id === tvShow.id);

    const handleWatchlistClick = () => {
        if (isInWatchlist) {
            removeFromWatchlist(tvShow);
        } else {
            addToWatchlist(tvShow);
        }
    };

    return (
        <div className='tv-show-card'>
            <img src={tvShow.poster_path} alt={tvShow.title} />
            <h3>{tvShow.title}</h3>
            <p>{tvShow.overview}</p>
            <button onClick={() => navigate(`/tv-show/${tvShow.id}`)}>View Details</button>
            <button onClick={handleWatchlistClick}>
                {isInWatchlist ? 'remove from Watchlist' : 'Add to Watchlist'}
            </button>
        </div>
    );
};

export default TVShowCard;