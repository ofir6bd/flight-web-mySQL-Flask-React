import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import "./login.css";
import { Auth } from "../Auth/Auth";
import { useNavigate } from "react-router";

function Login() {
  let navigate = useNavigate();

  const handleClick = (e) => {
    Auth(email, password);
    console.log("The link was clicked.");
    navigate("/customerPage");
  };
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleEmail = (event) => {
    setEmail(event.target.value);
  };
  const handlePassword = (event) => {
    setPassword(event.target.value);
  };

  return (
    <div className="container">
      <h2> Sign In Page</h2>
      <TextField
        id="outlined-basic"
        label="Email:"
        variant="outlined"
        onChange={handleEmail}
      />
      <TextField
        id="outlined-basic"
        label="Password:"
        variant="outlined"
        onChange={handlePassword}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Log In
      </Button>
    </div>
  );
}

export default Login;
