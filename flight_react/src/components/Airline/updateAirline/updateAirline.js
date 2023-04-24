import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiUpdateAirline } from "../../../apiHandler/apiHandlerAirline";
import { useNavigate } from "react-router";
import { apiGetAirlineDetails } from "../../../apiHandler/apiHandlerAirline";
import Messages from "../../../messages";

export default function UpdateAirlineForm() {
  let navigate = useNavigate();
  const [name, setName] = useState("");
  const [options, setOptions] = React.useState([]);

  const handleName = (event) => {
    setName(event.target.value);
  };

  //to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetAirlineDetails().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  //the action post button submit
  const handleClick = () => {
    apiUpdateAirline(name).then((response) => {
      if (response.success) {
        localStorage.setItem("globalVarMessage", response.success);
        localStorage.setItem("globalVarMessageType", "success");
        navigate("/airlinePage");
      } else {
        localStorage.setItem("globalVarMessage", JSON.stringify(response));
        localStorage.setItem("globalVarMessageType", "error");
        navigate("/updateAirline");
      }
    });
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Update Airline page</h2>
      <TextField
        id="outlined-basic"
        label={"Name: " + options.name}
        variant="outlined"
        onChange={handleName}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Update Airline
      </Button>
    </div>
  );
}
