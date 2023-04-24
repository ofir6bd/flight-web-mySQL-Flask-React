import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
// import "./login.css";
// import { UseAuth } from "../useAuth/useAuth";
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

  const handleClick = () => {
    console.log("start update Airline handleClick");
    apiUpdateAirline(name)
      .then((response) => {
        if (response.success) {
          console.log(response);
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
          navigate("/airlinePage");
        } else {
          console.log(response);
          localStorage.setItem("globalVarMessage", JSON.stringify(response));
          localStorage.setItem("globalVarMessageType", "error");
          navigate("/updateAirline");
        }
      });
  };

  useEffect(() => {
    function fetchData() {
      apiGetAirlineDetails().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

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
