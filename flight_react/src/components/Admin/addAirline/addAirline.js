import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiAddAirline } from "../../../apiHandler/apiHandlerAdmin";
import { useNavigate } from "react-router";
import Select from "react-select";
import { apiGetAllUsersPreAirline } from "../../../apiHandler/apiHandlerAdmin";
import { apiGetAllCountries } from "../../../apiHandler/apiHandler";
import Messages from "../../../messages";

export default function AddAirlineForm() {
  let navigate = useNavigate();
  const [options, setOptions] = React.useState([]);
  const [optionsCountry, setOptionsCountry] = React.useState([]);
  const [name, setName] = useState("");
  const [countryID, setCountryID] = useState("");
  const [userID, setUserID] = useState("");

  const handleName = (event) => {
    setName(event.target.value);
  };
// to load the options to the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetAllUsersPreAirline().then((response) => {
        setOptions(response);
      });
      apiGetAllCountries().then((response) => {
        setOptionsCountry(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    console.log("start add customer handleClick");
    var country_id = "";
    var user_id = "";
    if (countryID) {
      country_id = countryID.id;
    }
    if (userID) {
      user_id = userID.id;
    }
    apiAddAirline(name, country_id, user_id).then((response) => {
      if (response.success) {
        localStorage.setItem("globalVarMessage", response.success);
        localStorage.setItem("globalVarMessageType", "success");
        navigate("/adminPage");
      } else {
        localStorage.setItem("globalVarMessage", JSON.stringify(response));
        localStorage.setItem("globalVarMessageType", "error");
        navigate("/addAirline");
      }
    });
  };
  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Add Airline page</h2>
      <TextField
        id="outlined-basic"
        label="Name:"
        variant="outlined"
        onChange={handleName}
      />
      <div style={{ width: "800px" }}>
        <Select
          name="User Role:"
          options={optionsCountry}
          value={countryID}
          onChange={setCountryID}
          getOptionLabel={(option) => option.name}
          getOptionValue={(option) => option.id} 
          placeholder="Country:"
        />
      </div>
      <div style={{ width: "800px" }}>
        <Select
          name="user_id"
          options={options}
          value={userID}
          onChange={setUserID}
          getOptionLabel={(option) =>
            "ID: " +
            option.id +
            ", Username: " +
            option.username +
            ", Email: " +
            option.email
          }
          getOptionValue={(option) => option.id} 
          placeholder="Connect to user:"
        />
      </div>
      <Button variant="contained" className="Button" onClick={handleClick}>
        Add Airline
      </Button>
    </div>
  );
}
