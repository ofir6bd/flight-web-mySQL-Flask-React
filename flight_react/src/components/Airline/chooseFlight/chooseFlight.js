import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiUpdateFlight } from "../../../apiHandler/apiHandlerAirline";
import { useNavigate } from "react-router";
import { apiGetMyFlights } from "../../../apiHandler/apiHandlerAirline";
import Select from "react-select";

export default function ChooseFlightForm() {
  let navigate = useNavigate();

  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);

  // const handleName = (event) => {
  //   // setName(event.target.value);
  // };

  const handleClick = () => {
    console.log("value is: ", value);
    navigate("/updateFlight", { state: { flight: value } });
  };

  useEffect(() => {
    function fetchData() {
      apiGetMyFlights().then((response) => {
        setOptions(response);
        console.log(response);
      });
    }
    fetchData();
  }, []);

  return (
    <div className="container">
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
        getOptionValue={(option) => option.flight_id} // It should be unique value in the options. E.g. ID
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Submit
      </Button>
    </div>
  );
}
