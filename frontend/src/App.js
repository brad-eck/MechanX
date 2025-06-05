import React, { useState } from 'react';
import UserForm from './components/UserForm';
import VehicleForm from './components/VehicleForm';
import VehicleList from './components/VehicleList';
import './index.css';

function App() {
  const [userId, setUserId] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-4">
      <h1 className="text-3xl font-bold text-gray-800 mb-6">MechanX</h1>
      <div className="w-full max-w-md">
        <UserForm />
        <div className="mt-6">
          <label className="block text-sm font-medium text-gray-700">User ID</label>
          <input
            type="number"
            placeholder="Enter User ID"
            onChange={(e) => setUserId(e.target.value)}
            className="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        {userId && (
          <div className="mt-6 space-y-6">
            <VehicleForm userId={userId} />
            <VehicleList userId={userId} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;