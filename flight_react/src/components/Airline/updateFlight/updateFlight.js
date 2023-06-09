import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiUpdateFlight } from "../../../apiHandler/apiHandlerAirline";
import { useNavigate } from "react-router";
import { useLocation } from "react-router-dom";
import { DateTimePicker } from "@mui/x-date-pickers";
import { apiGetAllCountries } from "../../../apiHandler/apiHandler";
import Select from "react-select";
import DateFormat from "../../../dateFormat";
import Messages from "../../../messages";

export default function UpdateFlightForm() {
  let navigate = useNavigate();
  const { state } = useLocation();
  const [options, setOptions] = React.useState([]);
  const [fromValue, setFromValue] = useState(null);
  const [toValue, setToValue] = useState(null);
  const [depTime, setDepTime] = useState(null);
  const [lanTime, setLanTime] = useState(null);

  //to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetAllCountries().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  const handleRemainingTickets = (event) => {
    const result = event.target.value.replace(/\D/g, "");
    state.flight.remaining_tickets = result;
  };

  //the actions post button submit
  const handleClick = () => {
    if (fromValue) {
      state.flight.origin_country_id = fromValue.id;
    }
    if (toValue) {
      state.flight.destination_country_id = toValue.id;
    }
    if (depTime) {
      state.flight.departure_time = DateFormat(depTime);
    } else {
      state.flight.departure_time = "";
    }
    if (lanTime) {
      state.flight.landing_time = DateFormat(lanTime);
    } else {
      state.flight.landing_time = "";
    }

    apiUpdateFlight(state.flight).then((response) => {
      if (response.success) {
        localStorage.setItem("globalVarMessage", response.success);
        localStorage.setItem("globalVarMessageType", "success");
        navigate("/airlinePage");
      } else {
        localStorage.setItem("globalVarMessage", JSON.stringify(response));
        localStorage.setItem("globalVarMessageType", "error");
        navigate("/airlinePage");
      }
    });
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Update Flight page</h2>
      <div className="float-container">
        <div style={{ width: "300px" }}>
          <Select
            name="outlined-From"
            options={options}
            value={fromValue}
            onChange={setFromValue}
            getOptionLabel={(option) => option.name}
            getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
            placeholder={"From: " + state.flight.origin_country}
          />
        </div>
        <div style={{ width: "300px" }}>
          <Select
            name="outlined-to"
            options={options}
            value={toValue}
            onChange={setToValue}
            getOptionLabel={(option) => option.name}
            getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
            placeholder={"To: " + state.flight.destination_country}
          />
        </div>
      </div>
      <DateTimePicker
        id="outlined-Departure"
        value={depTime}
        label={"Departure time: " + state.flight.departure_time}
        variant="outlined"
        onChange={setDepTime}
      />
      <DateTimePicker
        id="outlined-Landing"
        value={lanTime}
        label={"Landing time: " + state.flight.landing_time}
        variant="outlined"
        onChange={setLanTime}
      />
      <TextField
        inputProps={{
          min: "0",
        }}
        type="number"
        placeholder={"Remaining tickets: " + state.flight.remaining_tickets}
        onChange={(e) => handleRemainingTickets(e)}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Update Flight
      </Button>
    </div>
  );
}
