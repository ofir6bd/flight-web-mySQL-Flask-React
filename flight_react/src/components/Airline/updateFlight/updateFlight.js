import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
// import "./login.css";
// import { UseAuth } from "../useAuth/useAuth";
import { apiUpdateFlight } from "../../../apiHandler/apiHandlerAirline";
import { useNavigate } from "react-router";
import { useLocation } from "react-router-dom";

export default function UpdateFlightForm() {
  let navigate = useNavigate();
  const { state } = useLocation();

  const [name, setName] = useState("");
  const [options, setOptions] = React.useState([]);

  const handleName = (event) => {
    setName(event.target.value);
  };

  const handleClick = () => {
    console.log("start update Flight handleClick");
    apiUpdateFlight(name)
      .then((response) => {
        if (response.success) {
          console.log(response);
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
        } else {
          console.log(response);
          localStorage.setItem("globalVarMessage", JSON.stringify(response));
          localStorage.setItem("globalVarMessageType", "error");
        }
      })
      .then(() => {
        navigate("/airlinePage");
      });
  };

  return (
    <div className="container">
      <h2> Update Flight page</h2>
      <TextField
        id="outlined-basic"
        label={"From: " + state.flight.origin_country}
        variant="outlined"
        onChange={handleName}
      />
      <TextField
        id="outlined-basic"
        label={"To: " + state.flight.destination_country}
        variant="outlined"
        onChange={handleName}
      />
      <TextField
        id="outlined-basic"
        label={"Departure time: " + state.flight.departure_time}
        variant="outlined"
        onChange={handleName}
      />
      <TextField
        id="outlined-basic"
        label={"Landing time: " + state.flight.landing_time}
        variant="outlined"
        onChange={handleName}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Update Flight
      </Button>
    </div>
  );
}
