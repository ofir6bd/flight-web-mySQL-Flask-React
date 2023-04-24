import React from "react";
import Flight from "../flight/flight";
import { useLocation } from "react-router-dom";

function Flights() {
  const { state } = useLocation();

  return (
    <div>
      <h1>The best flights are here </h1>
      
        {state.flights.map((flight) => (
          <Flight flight={flight}></Flight>
        ))}
    </div>
  );
}

export default Flights;
