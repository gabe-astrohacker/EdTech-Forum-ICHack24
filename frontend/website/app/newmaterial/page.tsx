'use client'

import React from 'react';
import Header from '../components/header.tsx';

const NewMaterial: React.FC<> = () => {
  return (
    <div className="flex min-h-screen max-w-screen border w-full flex-col items-center  bg-white">
    <Header/>
      <form className='h-1/3 w-2/3'>
        <div className="bg-white rounded-sm m-10 p-5 w-full">
          <input className="border-2 w-full box-border h-16 p=2" type="text" name="name" placeholder="Enter your resource's name here:"/><br/>
          <input className="border-2 box-border h-16 w-full p=2" type="text" name="url" placeholder="Enter your resource's URL here:"/><br/>
          <input className="border-2 box-border h-24 w-full p=2" type="text" name="description" placeholder='Describe the resource'/><br/>
          <input className='font-bold text-lg rounded-sm border-black border-2 bg-orange-400 text-white m-3 m-1/2 p-3' type="submit" value="Add new material:"/>
        </div>
      </form>
    </div>
  )
}
export default NewMaterial;