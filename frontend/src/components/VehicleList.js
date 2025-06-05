import React, { useState, useEffect } from 'react';
import axios from 'axios';

const VehicleList = ({ userId }) => {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    const fetchVehicles = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/users/${userId}/vehicles/`);
        setVehicles(response.data);
      } catch (error) {
        console.error(error);
      }
    };
    if (userId) fetchVehicles();
  }, [userId]);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Vehicles</h2>
      <ul className="space-y-2">
        {vehicles.map((vehicle) => (
          <li
            key={vehicle.id}
            className="p-4 bg-gray-50 rounded-md shadow-sm border border-gray-200"
          >
            {vehicle.year} {vehicle.make} {vehicle.model} - {vehicle.mileage} miles, {vehicle.condition}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default VehicleList;