// import React, { useState } from 'react';
// import { Link } from 'react-router-dom';

// const Navbar = () => {
//   const [searchQuery, setSearchQuery] = useState('');

//   return (
//     <nav className="bg-gray-900 p-4">
//       <div className="container mx-auto flex justify-between items-center">
//         <Link to="/" className="text-yellow-500 text-2xl font-bold">
//           Watchers
//         </Link>
        
//         <div className="flex-1 mx-8">
//           <input
//             type="text"
//             placeholder="Search movies and TV shows..."
//             className="w-full p-2 rounded bg-gray-800 text-white"
//             value={searchQuery}
//             onChange={(e) => setSearchQuery(e.target.value)}
//           />
//         </div>

//         <div className="flex items-center space-x-4">
//           <Link to="/movies" className="text-white">Movies</Link>
//           <Link to="/tv" className="text-white">TV</Link>
//           <Link to="/watchlist" className="text-white">My List</Link>
//           <Link to="/login" className="text-white">Login</Link>
//         </div>
//       </div>
//     </nav>
//   );
// };