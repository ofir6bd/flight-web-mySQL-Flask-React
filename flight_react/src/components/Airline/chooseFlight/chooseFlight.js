import React, { useState, useEffect } from "react";
import { Button } from "@mui/material";
import Messages from "../../../messages";
import { useNavigate } from "react-router";
import { apiGetMyFlights } from "../../../apiHandler/apiHandlerAirline";
import Select from "react-select";

export default function ChooseFlightForm() {
  let navigate = useNavigate();

  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);

  const handleClick = () => {
    if (value !== null) {
    navigate("/updateFlight", { state: { flight: value } });
  }};

  //to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetMyFlights().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Choose which flight to update</h2>
      <Select
        name="Flight"
        options={options}
        value={value}
        onChange={setValue}
        getOptionLabel={(option) =>
          "ID: " +
          option.flight_id +
          ", From: " +
          option.origin_country +
          ", To: " +
          option.destination_country +
          ", Departure Time: " +
          option.departure_time +
          ", Landing Time: " +
          option.landing_time +
          ", Remaining tickets: " +
          option.remaining_tickets
        }
        getOptionValue={(option) => option.flight_id}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Submit
      </Button>
    </div>
  );
}
