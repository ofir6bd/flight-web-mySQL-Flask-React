import React from "react";
import { Button } from "@mui/material";

function Flight({ flight }) {

  return (
    <div>
      <h3> Flight number: </h3>
      <h4> Flight ID: {flight.id}</h4>
      <h4> Airline ID: {flight.airline_company_id}</h4>
      <h4> From: {flight.origin_country_id}</h4>
      <h4> To: {flight.destination_country_id}</h4>
      <h4> Departure time: {flight.departure_time}</h4>
      <h4> Landing time: {flight.landing_time}</h4>
      <h4> Remaining tickets: {flight.remaining_tickets}</h4>
      <Button onClick> Book </Button>
    </div>
  );
}

export default Flight;