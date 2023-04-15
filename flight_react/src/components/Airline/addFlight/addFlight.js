import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiAddFlight } from "../../../apiHandler/apiHandlerAirline";
// import "./login.css";
// import { UseAuth } from "../useAuth/useAuth";

export default function AddFlightForm() {
  const [originCountryID, setOriginCountryID] = useState("");
  const [destinationCountryID, setDestinationCountryID] = useState("");
  const [departureTime, setDepartureTime] = useState("");
  const [landingTime, setLandingTime] = useState("");
  const [remainingTickets, setRemainingTickets] = useState("");

  const handleOriginCountryID = (event) => {
    setOriginCountryID(event.target.value);
  };
  const handleDestinationCountryID = (event) => {
    setDestinationCountryID(event.target.value);
  };
  const handleDepartureTime = (event) => {
    setDepartureTime(event.target.value);
  };
  const handleLandingTime = (event) => {
    setLandingTime(event.target.value);
  };
  const handleRemainingTickets = (event) => {
    setRemainingTickets(event.target.value);
  };
  return (
    <div className="container">
      <h2> Add Flight page</h2>
      <TextField
        id="outlined-basic"
        label="Origin Country:"
        variant="outlined"
        onChange={handleOriginCountryID}
      />
      <TextField
        id="outlined-basic"
        label="Destination Country:"
        variant="outlined"
        onChange={handleDestinationCountryID}
      />
      <TextField
        id="outlined-basic"
        label="Departure time:"
        variant="outlined"
        onChange={handleDepartureTime}
      />
      <TextField
        id="outlined-basic"
        label="Landing time:"
        variant="outlined"
        onChange={handleLandingTime}
      />
      <TextField
        id="outlined-basic"
        label="Remaining tickets:"
        variant="outlined"
        onChange={handleRemainingTickets}
      />
      <Button
        variant="contained"
        className="Button"
        onClick={() =>
          apiAddFlight(
            originCountryID,
            destinationCountryID,
            departureTime,
            landingTime,
            remainingTickets
          ).then((response) => console.log(response))
        }
      >
        Add Flight
      </Button>
    </div>
  );
}
