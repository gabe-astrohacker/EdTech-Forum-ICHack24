// components/SearchInput.tsx
'use client'

import React, { useState } from 'react';

const SearchInput: React.FC = () => {
  const [searchValue, setSearchValue] = useState('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearchValue(e.target.value);
  };

  const handleSearch = () => {
    // Implement your search logic here (e.g., filter data, make API calls)
    console.log('Search value:', searchValue);
  };

  return (
    <div className="flex items-center w-full mx-20">
      <input
        type="text"
        placeholder="Search..."
        value={searchValue}
        onChange={handleInputChange}
        className="border text-gray-700 p-2 rounded-l-md"
      />
      
      <button
        type="button"
        onClick={handleSearch}
        className="bg-orange-500 text-white p-2 rounded-r-md"
      >
        Search
      </button>
    </div>
  );
};

export default SearchInput;
