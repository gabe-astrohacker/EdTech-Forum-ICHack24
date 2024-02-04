// pages/signup.tsx
'use client'

import React, { useState } from 'react';
import Header from '../components/header.tsx';
import signIn from '../components/header.tsx';

const SignUp: React.FC = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Add logic to handle form submission (e.g., send data to backend)
    signIn();
    console.log('Form submitted with data:', formData);
    // Assume successful
  };

  return (
    <div className="flex min-h-screen max-w-screen border w-full flex-col items-center  bg-white">
      <Header/>
      <form className="max-w-md w-full p-4" onSubmit={handleSubmit}>
        <h2 className="text-2xl font-semibold mb-4">Log In</h2>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
            Email
          </label>
          <input 
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            className="border rounded w-full py-2 px-3 grey text-gray-900"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
            Password
          </label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
            className="border rounded w-full py-2 px-3 text-gray-900"
            required
          />
        </div>
        <button
          type="submit"
          className="bg-orange-500 text-white py-2 px-4 rounded hover:bg-blue-600"
        >
          Log In
        </button>
      </form>
    </div>
  );
};

export default SignUp;
