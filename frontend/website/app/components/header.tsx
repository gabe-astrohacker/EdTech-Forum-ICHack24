'use client'

import React from 'react';

function signOut(): boolean {
  // SIGN OUT LOGIC GOES HERE
  isLoggedIn[0] = false;
  return true; //successful sign out
}

export function signIn(): boolean {
    // SIGN IN LOGIC GOES HERE
    isLoggedIn[0] = true;
    return true;
};


const isLoggedIn = [false];

export const Header = () => {

  return (
      <div className="border bg-white-500 h-[4rem] px-10 w-full flex justify-between  items-center">
        <button className="hover:bg-gray-200 bg-gray-100 rounded-sm text-black p-5 h-1/2 flex items-center justify-center">
          EdTech Forum
        </button>
        <button className="hover:bg-gray-200 bg-gray-100 rounded-sm text-black p-5 h-1/2 flex items-center justify-center">
          Add New Material
        </button>
        {isLoggedIn[0]} ? ( 
        <button onClick={() => signOut()}>Logout</button>
      ) : ( 
        <button className="hover:bg-gray-200 bg-gray-100 rounded-sm text-black p-5 h-1/2 flex items-center justify-center">
          Login
        </button>
       )
      </div>
  );
};

