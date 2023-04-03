import React from "react";
import TextField from "@mui/material/TextField";
import { DateField } from "@mui/x-date-pickers/DateField";
import "./SearchFlight.css";
import { Button } from "@mui/material";
import { getFlights } from "../../apiHandler/ApiHandler";
import Flight from "../flight/flight";
import { useNavigate } from "react-router";

function SearchFlight() {
  let navigate = useNavigate();

  function navigateToFlights(flights_list) {
    console.log(flights_list);
    navigate("/flights", { state: { flights: flights_list } });
  }

  return (
    <div>
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
