import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiRemoveAirline } from "../../../apiHandler/apiHandlerAdmin";
import { apiGetAllAirlines } from "../../../apiHandler/apiHandler";
import { useNavigate } from "react-router";
import Select from "react-select";
import Messages from "../../../messages";

export default function RemoveAirlineForm() {
  let navigate = useNavigate();
  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);

  //to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetAllAirlines().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    if (value !== null) {
      apiRemoveAirline(value.id).then((response) => {
        if (response.success) {
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
          navigate("/adminPage");
        } else {
          localStorage.setItem("globalVarMessage", JSON.stringify(response));
          localStorage.setItem("globalVarMessageType", "error");
          navigate("/removeAirline");
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
      <h2> Remove Airline page</h2>
      <Select
        name="Airlines"
        options={options}
        value={value}
        onChange={setValue}
        getOptionLabel={(option) => option.name}
        getOptionValue={(option) => option.id}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Remove Airline
      </Button>
    </div>
  );
}
