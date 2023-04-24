import React, { useState, useEffect } from "react";
import { Button } from "@mui/material";
import { apiGetMyFlights } from "../../../apiHandler/apiHandlerAirline";
import { apiRemoveFlight } from "../../../apiHandler/apiHandlerAirline";
import { useNavigate } from "react-router";
import Select from "react-select";
import Messages from "../../../messages";

export default function RemoveFlightForm() {
  let navigate = useNavigate();
  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);

  //to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetMyFlights().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  //the actions for the button submit
  const handleClick = () => {
    if (value !== null) {
      apiRemoveFlight(value.flight_id).then((response) => {
        if (response.success) {
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
          navigate("/airlinePage");
        } else {
          localStorage.setItem("globalVarMessage", JSON.stringify(response));
          localStorage.setItem("globalVarMessageType", "error");
          navigate("/removeFlight");
        }
      });
    }
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Remove Flight page</h2>
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
          option.landing_time
        }
        getOptionValue={(option) => option.flight_id} // It should be unique value in the options. E.g. ID
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Remove Flight
      </Button>
    </div>
  );
}
