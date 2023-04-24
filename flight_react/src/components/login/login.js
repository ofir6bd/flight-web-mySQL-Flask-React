import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import "./login.css";
import { auth } from "../auth/auth";
import { useNavigate } from "react-router";
import Messages from "../../messages";

function Login() {
  let navigate = useNavigate();
  const [email, setEmail] = useState(null);
  const [password, setPassword] = useState(null);

  const handleEmail = (event) => {
    setEmail(event.target.value);
  };
  const handlePassword = (event) => {
    setPassword(event.target.value);
  };

  //actions post button submit
  const handleClick = () => {
    if (email !== null && password !== null) {
      auth(email, password);
      setTimeout(() => {
        if (localStorage.getItem("globalVarCustomerId")) {
          navigate("/customerPage");
        } else if (localStorage.getItem("globalVarAdminId")) {
          navigate("/adminPage");
        } else if (localStorage.getItem("globalVarAirlineId")) {
          navigate("/airlinePage");
        } else if (
          localStorage.getItem("globalVarUserId") &&
          localStorage.getItem("globalVarUserRole") == 3
        ) {
          navigate("/registerAsCustomer");
        } else if (
          localStorage.getItem("globalVarUserId") &&
          localStorage.getItem("globalVarUserRole") == 2
        ) {
          navigate("/registerAsAirline");
        } else {
          localStorage.setItem(
            "globalVarMessage",
            "Email or password are incorrect"
          );
          localStorage.setItem("globalVarMessageType", "error");
          navigate("/login");
        }
      }, 1000);
    } else {
      localStorage.setItem(
        "globalVarMessage",
        "one or more of the fields are missing"
      );
      localStorage.setItem("globalVarMessageType", "error");
      navigate("/login");
    }
    //auth function checks the authentication and saves the basic data in the local storage
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> LogIn Page</h2>
      <TextField
        id="email"
        label="Email:"
        variant="outlined"
        type={"email"}
        onChange={handleEmail}
      />
      <TextField
        id="Passwordc"
        label="Password:"
        variant="outlined"
        type="password"
        onChange={handlePassword}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Log In
      </Button>
    </div>
  );
}

export default Login;
