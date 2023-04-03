import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import "./signup.css";
import {createUser} from "../../apiHandler/ApiHandler";

function Signup() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [user_role, setUserRole] = useState("");

  const handleUsername = (event) => {
    setUsername(event.target.value);
  };
  const handlePassword = (event) => {
    setPassword(event.target.value);
  };
  const handleEmail = (event) => {
    setEmail(event.target.value);
  };
  const handleUserRole = (event) => {
    setUserRole(event.target.value);
  };

  return (
    <div className="container">
      <h2> Sign Up Page</h2>
      <TextField
        id="outlined-basic"
        label="Username:"
        variant="outlined"
        onChange={handleUsername}
      />
      <TextField
        id="outlined-basic"
        label="Password:"
        variant="outlined"
        onChange={handlePassword}
      />
      <TextField
        id="outlined-basic"
        label="Email:"
        variant="outlined"
        onChange={handleEmail}
      />
      <TextField
        id="outlined-basic"
        label="User Role:"
        variant="outlined"
        onChange={handleUserRole}
      />
      <Button
        variant="contained"
        className="Button"
        onClick={() =>
          createUser(username, password, email, user_role).then((response) =>
            console.log(response)
          )
        }
      >
        Sign Up
      </Button>
    </div>
  );
}

export default Signup;
