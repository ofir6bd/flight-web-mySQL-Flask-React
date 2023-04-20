import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import "./login.css";
import { auth } from "../auth/auth";
import { useNavigate } from "react-router";
import Messages from "../../messages";

function Login() {
  let navigate = useNavigate();

  const handleClick = () => {
    console.log("The link was clicked before");
    auth(email, password);
    setTimeout(() => {
      if (localStorage.getItem("globalVarCustomerId")) {
        navigate("/customerPage");
      } else if (localStorage.getItem("globalVarAdminId")) {
        navigate("/adminPage");
      } else if (localStorage.getItem("globalVarAirlineId")) {
        navigate("/airlinePage");
      } else {
        localStorage.setItem(
          "globalVarMessage",
          "Email or password are incorrect"
        );
        localStorage.setItem("globalVarMessageType", "error");
        navigate("/");
      }
    }, 1000);

    console.log("The link was clicked after");
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
