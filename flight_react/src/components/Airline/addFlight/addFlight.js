import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiAddFlight } from "../../../apiHandler/apiHandlerAirline";
import { apiGetAllCountries } from "../../../apiHandler/apiHandler";
import { DateTimePicker } from "@mui/x-date-pickers";
import Select from "react-select";
import DateFormat from "../../../dateFormat";
import { useNavigate } from "react-router";

export default function AddFlightForm() {
  let navigate = useNavigate();
  const [fromValue, setFromValue] = useState(null);
  const [toValue, setToValue] = useState(null);
  const [depTime, setDepTime] = useState(null);
  const [lanTime, setLanTime] = useState(null);
  const [remainingTickets, setRemainingTickets] = useState("");
  const [options, setOptions] = React.useState([]);

  useEffect(() => {
    function fetchData() {
      apiGetAllCountries().then((response) => {
        setOptions(response);
        // console.log(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
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
    setRemainingTickets(result);
  };

  return (
    <div className="container">
      <h2> Add Flight page</h2>
      <div class="float-container">
        <div style={{ width: "300px" }}>
          <Select
            name="outlined-From"
            options={options}
            value={fromValue}
            onChange={setFromValue}
            getOptionLabel={(option) => option.name}
            getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
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
            getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
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
        // is24Hour
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
      <Button
        variant="contained"
        className="Button"
        onClick={handleClick}
        // apiAddFlight(
        //   originCountryID,
        //   destinationCountryID,
        //   departureTime,
        //   landingTime,
        //   remainingTickets
        // ).then((response) => console.log(response))
        // }
      >
        Add Flight
      </Button>
    </div>
  );
}
