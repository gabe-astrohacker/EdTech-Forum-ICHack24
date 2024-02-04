import React from 'react';

const Header: React.FC<> = () => {
  return (
      <div className="border bg-white-500 h-[4rem] px-10 w-full flex justify-between  items-center">
        <button className="hover:bg-gray-200 bg-gray-100 rounded-sm text-black p-5 h-1/2 flex items-center justify-center">
          EdTech Forum
        </button>
        <button className="hover:bg-gray-200 bg-gray-100 rounded-sm text-black p-5 h-1/2 flex items-center justify-center">
          Login
        </button>
      </div>
  );
};

export default Header;