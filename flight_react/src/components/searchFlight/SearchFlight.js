import React, { useState, useEffect } from "react";
import "./SearchFlight.css";
import { Button } from "@mui/material";
import { apiGetAllCountries } from "../../apiHandler/apiHandler";
import { apiGetFlightsByParameters } from "../../apiHandler/apiHandler";
import { useNavigate } from "react-router";
import Select from "react-select";
import Messages from "../../messages";
import { DateTimePicker } from "@mui/x-date-pickers";
import DateFormat from "../../dateFormat";

function SearchFlight() {
  let navigate = useNavigate();
  const [fromValue, setFromValue] = useState(null);
  const [toValue, setToValue] = useState(null);
  const [options, setOptions] = React.useState([]);
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

  var from = "";
  var to = "";
  var departure_time = "";
  var landing_time = "";

  //the actions post button submit
  const handleClick = () => {
    if (fromValue) {
      from = fromValue.id;
    }
    if (toValue) {
      to = toValue.id;
    }
    if (depTime) {
      departure_time = DateFormat(depTime);
    }
    if (lanTime) {
      landing_time = DateFormat(lanTime);
    }

    apiGetFlightsByParameters(from, to, departure_time, landing_time).then(
      (response) => {
        if (response.length > 0) {
          navigate("/flights", { state: { flights: response } });
        } else {
          localStorage.setItem("globalVarMessage", "no flights found");
          localStorage.setItem("globalVarMessageType", "warning");
          navigate("/searchFlight");
        }
      }
    );
  };

  return (
    <div>
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <div className="mainPageSearchFlight">
        <h2> Search flight </h2>
        <h4>The best flight deals to everywhere, from anywhere</h4>
      </div>
      <div className="container-all">
        <div className="container-select-first">
          <div style={{ width: "300px" }}>
            <Select
              name="From"
              options={options}
              value={fromValue}
              onChange={setFromValue}
              getOptionLabel={(option) => option.name}
              getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
              placeholder="From:"
            />
          </div>
        </div>
        <div className="container-select-second">
          <div style={{ width: "300px" }}>
            <Select
              name="To"
              options={options}
              value={toValue}
              onChange={setToValue}
              getOptionLabel={(option) => option.name}
              getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
              placeholder="To:"
            />
          </div>
        </div>
        <DateTimePicker
          id="outlined-basic"
          value={depTime}
          label={"Departure time"}
          variant="outlined"
          onChange={setDepTime}
        />
        <DateTimePicker
          id="outlined-basic"
          value={lanTime}
          label={"Landing time"}
          variant="outlined"
          onChange={setLanTime}
        />
        <Button variant="contained" className="Button" onClick={handleClick}>
          Submit
        </Button>
      </div>
    </div>
  );
}

export default SearchFlight;
