import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiUpdateFlight } from "../../../apiHandler/apiHandlerAirline";
import { useNavigate } from "react-router";
import { useLocation } from "react-router-dom";
import { DateTimePicker } from "@mui/x-date-pickers";
import { apiGetAllFCountries } from "../../../apiHandler/apiHandler";
import Select from "react-select";

export default function UpdateFlightForm() {
  let navigate = useNavigate();
  const { state } = useLocation();
  const [options, setOptions] = React.useState([]);
  const [fromValue, setFromValue] = useState(null);
  const [toValue, setToValue] = useState(null);
  const [depTime, setDepTime] = useState(null);
  const [lanTime, setLanTime] = useState(null);
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

  const theme = (theme) => ({
    ...theme,
    colors: {
      ...theme.colors,
      // primary25: "blue",
      primary: "green",

      // All possible overrides
      // primary: '#2684FF',
      // primary75: '#4C9AFF',
      // primary50: '#B2D4FF',
      primary25: "#DEEBFF",

      // danger: '#DE350B',
      // dangerLight: '#FFBDAD',

      // neutral0: 'hsl(0, 0%, 100%)',
      // neutral5: 'hsl(0, 0%, 95%)',
      // neutral10: 'hsl(0, 0%, 90%)',
      // neutral20: 'hsl(0, 0%, 80%)',
      neutral30: "hsl(0, 0%, 70%)",
      // neutral40: 'hsl(0, 0%, 60%)',
      // neutral50: 'hsl(0, 0%, 50%)',
      // neutral60: 'hsl(0, 0%, 40%)',
      // neutral70: 'hsl(0, 0%, 30%)',
      // neutral80: 'hsl(0, 0%, 20%)',
      // neutral90: 'hsl(0, 0%, 10%)',
    },
    // Other options you can use
    borderRadius: 4,
    baseUnit: 4,
    controlHeight: 38,
    // menuGutter: baseUnit * 2
  });
  return (
    <div className="container">
      <h2> Update Flight page</h2>
      <Select
        // theme={theme}
        name="outlined-From"
        options={options}
        value={fromValue}
        onChange={setFromValue}
        getOptionLabel={(option) => option.name}
        getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
        placeholder={"From: " + state.flight.origin_country}
      />
      <Select
        name="outlined-From"
        options={options}
        value={toValue}
        onChange={setToValue}
        getOptionLabel={(option) => option.name}
        getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
        placeholder={"From: " + state.flight.destination_country}
      />

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
      <Button variant="contained" className="Button" onClick={handleClick}>
        Update Flight
      </Button>
    </div>
  );
}
