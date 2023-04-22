import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiUpdateFlight } from "../../../apiHandler/apiHandlerAirline";
import { useNavigate } from "react-router";
import { useLocation } from "react-router-dom";
import { DateTimePicker } from "@mui/x-date-pickers";
import { apiGetAllFCountries } from "../../../apiHandler/apiHandler";
import Select from "react-select";
// import NumberField from "react-number-field";

export default function UpdateFlightForm() {
  let navigate = useNavigate();
  const { state } = useLocation();
  const [options, setOptions] = React.useState([]);
  const [fromValue, setFromValue] = useState(null);
  const [toValue, setToValue] = useState(null);
  const [depTime, setDepTime] = useState(null);
  const [lanTime, setLanTime] = useState(null);
  const [remainingTickets, setRemainingTickets] = useState("");
  const [value, setValue] = useState("");

  const [name, setName] = useState("");
  // const [options, setOptions] = React.useState([]);

  const handle = (event) => {
    setName(event.target.value);
  };
  useEffect(() => {
    function fetchData() {
      apiGetAllFCountries().then((response) => {
        setOptions(response);
        // console.log(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    console.log("start update Flight handleClick");
    console.log(remainingTickets);
    if (fromValue) {
      state.flight.origin_country_id = fromValue.id;
    }
    if (toValue) {
      state.flight.destination_country_id = toValue.id;
    }
    if (depTime) {
      // state.flight.origin_country_id = depTime.id;
    }
    if (lanTime) {
      // state.flight.destination_country_id = toValue.id;
    }
    // if (remainingTickets) {
    //   console.log("remainingTickets" + remainingTickets);
    //   state.flight.remainingTickets = remainingTickets;
    // }
    console.log("remainingTiddddckets" + remainingTickets);
    apiUpdateFlight(state.flight)
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
  const handleRemainingTickets = (event) => {
    const result = event.target.value.replace(/\D/g, "");
    state.flight.remaining_tickets = result;
  };

  return (
    <div className="container">
      <h2> Update Flight page</h2>
      <div class="float-container">
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
            name="outlined-From"
            options={options}
            value={toValue}
            onChange={setToValue}
            getOptionLabel={(option) => option.name}
            getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
            placeholder={"From: " + state.flight.destination_country}
          />
        </div>
      </div>
      <DateTimePicker
        id="outlined-basic"
        label={"Departure time: " + state.flight.departure_time}
        variant="outlined"
        onChange={setDepTime}
      />
      <DateTimePicker
        id="outlined-basic"
        label={"Landing time: " + state.flight.landing_time}
        variant="outlined"
        onChange={setLanTime}
      />
      <input
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
