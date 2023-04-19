import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import "./login.css";
import { Auth } from "../Auth/Auth";
import { useNavigate } from "react-router";

function Login() {
  let navigate = useNavigate();

  const handleClick = () => {
    console.log("The link was clicked before");
    Auth(email, password);
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
    }, 800);

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
  function Messages(props) {
    const { message, messageType } = props;
    localStorage.removeItem("globalVarMessage");
    localStorage.removeItem("globalVarMessageType");
    if (!message) {
      return null;
    }
    if (messageType == "success") {
      return <div className="messageContainerSuccess"> {message}</div>;
    } else {
      return <div className="messageContainerError"> {message}</div>;
    }
  }
  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> LogIn Page</h2>
      <TextField
        id="outlined-basic"
        label="Email:"
        variant="outlined"
        type={"email"}
        onChange={handleEmail}
      />
      <TextField
        id="outlined-basic"
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
