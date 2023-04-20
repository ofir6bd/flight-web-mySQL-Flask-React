import React from "react";
import Flight from "../flight/flight";
import { useLocation } from "react-router-dom";

function Flights() {
  const { state } = useLocation();

  return (
    <div>
      {state.flights.map((flight, i) => (
        <Flight flight={flight}></Flight>
      ))}
    </div>
  );
}

export default Flights;
