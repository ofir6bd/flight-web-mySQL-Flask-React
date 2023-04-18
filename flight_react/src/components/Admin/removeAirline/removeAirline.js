import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import {
  apiRemoveAirline,
  getAllAirlines,
} from "../../../apiHandler/apiHandlerAdmin";
import { useNavigate } from "react-router";
import Select from "react-select";

export default function RemoveAirlineForm() {
  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);

  let navigate = useNavigate();

  useEffect(() => {
    function fetchData() {
      getAllAirlines().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    if (value !== null) {
      apiRemoveAirline(value.id)
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
          navigate("/adminPage");
        });
    }
  };

  return (
    <div className="container">
      <h2> Remove Airline page</h2>
      <Select
        name="Airlines"
        options={options}
        value={value}
        onChange={setValue}
        getOptionLabel={(option) => option.name}
        getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
      />

      <Button variant="contained" className="Button" onClick={handleClick}>
        Remove Airline
      </Button>
    </div>
  );
}
