import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiRemoveAirline } from "../../../apiHandler/apiHandlerAdmin";
import { apiGetAllAirlines } from "../../../apiHandler/apiHandler";
import { useNavigate } from "react-router";
import Select from "react-select";
import Messages from "../../../messages";

export default function RemoveAirlineForm() {
  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);

  let navigate = useNavigate();

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
          console.log(response);
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
          navigate("/adminPage");
        } else {
          console.log(response);
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
        getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
      />

      <Button variant="contained" className="Button" onClick={handleClick}>
        Remove Airline
      </Button>
    </div>
  );
}
