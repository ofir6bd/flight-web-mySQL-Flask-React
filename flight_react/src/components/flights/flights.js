import React from "react";
import Flight from "../flight/flight";
import { useLocation } from "react-router-dom";

function Flights({ flights_list }) {
  const { state } = useLocation();

  return (
    <div>
      {state.flights.map((flight, i) => (
        <Flight key={i} flight={flight}></Flight>
      ))}
    </div>
  );
}

export default Flights;
