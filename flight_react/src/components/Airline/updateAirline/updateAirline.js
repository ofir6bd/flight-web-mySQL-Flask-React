import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
// import "./login.css";
// import { UseAuth } from "../useAuth/useAuth";
import { apiUpdateAirline } from "../../../apiHandler/apiHandlerAirline";
import { useNavigate } from "react-router";
import { apiGetAirlineDetails } from "../../../apiHandler/apiHandlerAirline";

export default function AddAirlineForm() {
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
