import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import "./signup.css";
import { apiCreateUser } from "../../apiHandler/apiHandler";
import { apiGetUserRoles } from "../../apiHandler/apiHandler";
import Select from "react-select";
import { useNavigate } from "react-router";
import Messages from "../../messages";

function Signup() {
  let navigate = useNavigate();
  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  // const [user_role, setUserRole] = useState("");

  const handleUsername = (event) => {
    setUsername(event.target.value);
  };
  const handlePassword = (event) => {
    setPassword(event.target.value);
  };
  const handleEmail = (event) => {
    setEmail(event.target.value);
  };

  useEffect(() => {
    function fetchData() {
      apiGetUserRoles().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    if (value !== null) {
      apiCreateUser(username, password, email, value.id)
        .then((response) => {
          if (response.success) {
            // console.log(response);
            localStorage.setItem("globalVarMessage", response.success);
            localStorage.setItem("globalVarMessageType", "success");
          } else {
            // console.log(response);
            localStorage.setItem("globalVarMessage", JSON.stringify(response));
            localStorage.setItem("globalVarMessageType", "error");
          }
        })
        .then(() => {
          navigate("/login");
        });
    }
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Sign Up Page</h2>
      <TextField
        id="Username"
        label="Username:"
        variant="outlined"
        onChange={handleUsername}
      />
      <TextField
        id="Password"
        label="Password:"
        variant="outlined"
        type="password"
        onChange={handlePassword}
      />
      <TextField
        id="Email"
        label="Email:"
        variant="outlined"
        type={"email"}
        onChange={handleEmail}
      />
      <div style={{ width: "300px" }}>
        <Select
          name="User Role:"
          options={options}
          value={value}
          onChange={setValue}
          getOptionLabel={(option) => option.role_name}
          getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
          placeholder="User Role"
        />
      </div>
      <Button variant="contained" className="Button" onClick={handleClick}>
        Sign Up
      </Button>
    </div>
  );
}

export default Signup;
