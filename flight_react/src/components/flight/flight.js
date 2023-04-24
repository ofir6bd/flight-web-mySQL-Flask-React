import React from "react";
import { Button } from "@mui/material";
import { useNavigate } from "react-router";
import "./flight.css";

function Flight({ flight }) {
  let navigate = useNavigate();

  //the actions post button submit
  const handleClick = () => {
    if (localStorage.getItem("globalVarCustomerId")) {
      localStorage.setItem("globalVarFlightID", flight.flight_id);
      navigate("/verification");
    } else {
      localStorage.setItem(
        "globalVarMessage",
        "You must log in before booking flights"
      );
      localStorage.setItem("globalVarMessageType", "error");
      navigate("/login");
    }
  };

  return (
    <div className="containerFlight">
      <h4> From: {flight.origin_country}</h4>
      <h4> To: {flight.destination_country}</h4>
      <h4> Departure time: {flight.departure_time}</h4>
      <h4> Landing time: {flight.landing_time}</h4>
      <h4> Remaining tickets: {flight.remaining_tickets}</h4>
      <Button onClick={handleClick}> Book </Button>
    </div>
  );
}

export default Flight;
