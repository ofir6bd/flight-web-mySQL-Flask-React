import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiAddFlight } from "../../../apiHandler/apiHandlerAirline";
import { apiGetAllCountries } from "../../../apiHandler/apiHandler";
import { DateTimePicker } from "@mui/x-date-pickers";
import Select from "react-select";
import DateFormat from "../../../dateFormat";
import { useNavigate } from "react-router";
import Messages from "../../../messages";

export default function AddFlightForm() {
  let navigate = useNavigate();
  const [fromValue, setFromValue] = useState(null);
  const [toValue, setToValue] = useState(null);
  const [depTime, setDepTime] = useState(null);
  const [lanTime, setLanTime] = useState(null);
  const [remainingTickets, setRemainingTickets] = useState("");
  const [options, setOptions] = React.useState([]);

  const handleRemainingTickets = (event) => {
    const result = event.target.value.replace(/\D/g, "");
    setRemainingTickets(result);
  };

  //to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetAllCountries().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    if (
      fromValue !== null &&
      toValue !== null &&
      depTime !== null &&
      lanTime !== null &&
      remainingTickets !== null
    ) {
      var departure_time = DateFormat(depTime);
      var landing_time = DateFormat(lanTime);
      apiAddFlight(
        fromValue.id,
        toValue.id,
        departure_time,
        landing_time,
        remainingTickets
      )
        .then((response) => {
          if (response.success) {
            localStorage.setItem("globalVarMessage", response.success);
            localStorage.setItem("globalVarMessageType", "success");
          } else {
            localStorage.setItem("globalVarMessage", JSON.stringify(response));
            localStorage.setItem("globalVarMessageType", "error");
          }
        })
        .then(() => {
          navigate("/airlinePage");
        });
    } else {
      localStorage.setItem(
        "globalVarMessage",
        "one or more of the items are missing"
      );
      localStorage.setItem("globalVarMessageType", "error");
      navigate("/addFlight");
    }
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Add Flight page</h2>
      <div class="float-container">
        <div style={{ width: "300px" }}>
          <Select
            name="outlined-From"
            options={options}
            value={fromValue}
            onChange={setFromValue}
            getOptionLabel={(option) => option.name}
            getOptionValue={(option) => option.id}
            placeholder={"From: "}
          />
        </div>
        <div style={{ width: "300px" }}>
          <Select
            name="outlined-to"
            options={options}
            value={toValue}
            onChange={setToValue}
            getOptionLabel={(option) => option.name}
            getOptionValue={(option) => option.id}
            placeholder={"To: "}
          />
        </div>
      </div>
      <DateTimePicker
        id="outlined-Departure"
        value={depTime}
        label={"Departure time: "}
        variant="outlined"
        onChange={setDepTime}
      />
      <DateTimePicker
        id="outlined-Landing"
        value={lanTime}
        label={"Landing time: "}
        variant="outlined"
        onChange={setLanTime}
      />
      <TextField
        inputProps={{
          min: "0",
        }}
        type="number"
        placeholder={"Remaining tickets: "}
        value={remainingTickets}
        onChange={handleRemainingTickets}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Add Flight
      </Button>
    </div>
  );
}
