import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { DateField } from "@mui/x-date-pickers/DateField";
import "./SearchFlight.css";
import { Button } from "@mui/material";
import { getFlights } from "../../apiHandler/apiHandler";
import Flight from "../flight/flight";
import { useNavigate } from "react-router";
import { useLocation } from "react-router-dom";

function SearchFlight() {
  let navigate = useNavigate();
  const { state } = useLocation();

  function navigateToFlights(flights_list) {
    navigate("/flights", { state: { flights: flights_list } });
  }

  function Messages(props) {
    const { message, messageType } = props;
    localStorage.removeItem("globalVarMessage");
    localStorage.removeItem("globalVarMessageType");
    if (!message) {
      return null;
    }
    if (messageType == "success") {
      return <div className="messageContainerSuccess"> {message}</div>;
    } else {
      return <div className="messageContainerError"> {message}</div>;
    }
  }

  return (
    <div>
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Search flight </h2>
      <div className="container">
        <TextField id="outlined-basic" label="From:" variant="outlined" />
        <TextField id="outlined-basic" label="To:" variant="outlined" />
        <DateField label="Departure time" />
        <DateField label="Landing time" />
        <Button
          variant="contained"
          className="Button"
          onClick={() =>
            getFlights().then((result) => navigateToFlights(result))
          }
        >
          Search
        </Button>
      </div>
    </div>
  );
}

export default SearchFlight;
