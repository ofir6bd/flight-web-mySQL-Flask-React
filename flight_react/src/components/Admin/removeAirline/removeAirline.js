import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
// import "./login.css";
// import { UseAuth } from "../useAuth/useAuth";
import { apiAddAirline } from "../../../apiHandler/apiHandlerAdmin";
import { useNavigate } from "react-router";

export default function RemoveAirlineForm() {
  let navigate = useNavigate();
  const [name, setName] = useState("");
  const [countryID, setCountryID] = useState("");
  const [userID, setUserID] = useState("");

  const handleName = (event) => {
    setName(event.target.value);
  };
  const handleCountryID = (event) => {
    setCountryID(event.target.value);
  };
  const handleUserID = (event) => {
    setUserID(event.target.value);
  };

  const handleClick = () => {
    console.log("start add customer handleClick");
    apiAddAirline(name, countryID, userID)
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
  };
  return (
    <div className="container">
      <h2> Remove Airline page</h2>
      <TextField
        id="outlined-basic"
        label="Name:"
        variant="outlined"
        onChange={handleName}
      />
      <TextField
        id="outlined-basic"
        label="CountryID:"
        variant="outlined"
        onChange={handleCountryID}
      />
      <TextField
        id="outlined-basic"
        label="UserID:"
        variant="outlined"
        onChange={handleUserID}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Remove Airline
      </Button>
    </div>
  );
}
