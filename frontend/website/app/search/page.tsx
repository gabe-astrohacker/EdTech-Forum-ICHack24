// pages/search-results.tsx
'use client'

import React from 'react';
import Header from '../components/header.tsx';
import SearchInput from "../components/SearchInput.tsx";

const SearchResults: React.FC = () => {
  return (
    <div className=" flex min-h-screen max-w-screen border w-full flex-col items-center  bg-white">
      <Header/>
      <div className="text-gray-700  h-[50rem] w-full flex">
        <div className="basis-3/5 bg-white, object-center">
          <div className="p-10 py-5">
            <SearchInput/>
          </div>
          <div className="font-bold text-xl px-5">
            HELLO this is search query:
          </div> 

          <div className='p-2 m-2 w-full h-min bg-orange-100 flex'>
            <div>
              <p>Physics and Maths Tutor</p>
              <a href='https://physicsandmathstutor.com'>https://physicsandmathstutor.com</a>
            </div>
            <button className='ml-auto bg-white p-2 m-1' value="upvote">▲</button>
            <button className=" bg-white p-2 m-1" value="downvote">▼</button>
          </div>
        </div>
      </div>

        <div className="basis-2/5">
        
      </div>
    </div>
  );
};

export default SearchResults;