import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiRegisterAsAirline } from "../../apiHandler/apiHandlerAirline";
import { apiGetAllCountries } from "../../apiHandler/apiHandler";
import { apiGetAirlineDetails } from "../../apiHandler/apiHandlerAirline";

import Select from "react-select";
import { useNavigate } from "react-router";
import Messages from "../../messages";

function RegisterAsAirlineForm() {
  let navigate = useNavigate();
  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);
  const [name, setName] = useState("");

  const handleName = (event) => {
    setName(event.target.value);
  };

  useEffect(() => {
    function fetchData() {
      apiGetAllCountries().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    if (value !== null) {
      apiRegisterAsAirline(
        name,
        value.id,
        localStorage.getItem("globalVarUserId")
      ).then((response) => {
        if (response.success) {
          // console.log(response);
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
          apiGetAirlineDetails()
            .then((response) => {
              localStorage.setItem("globalVarAirlineId", response.id);
            })
            .then(() => {
              navigate("/airlinePage");
            });
        } else {
          localStorage.setItem("globalVarMessage", JSON.stringify(response));
          localStorage.setItem("globalVarMessageType", "error");
          navigate("/registerAsAirline");
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
      <h2> Register as Airline Page</h2>
      <TextField
        id="name"
        label="Name:"
        variant="outlined"
        onChange={handleName}
      />

      <Select
        name="User Role:"
        options={options}
        value={value}
        onChange={setValue}
        getOptionLabel={(option) => option.name}
        getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Register as Airline
      </Button>
    </div>
  );
}

export default RegisterAsAirlineForm;
