import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import "./logout.css";
import { Auth } from "../Auth/Auth";
import { useNavigate } from "react-router";

function Logout() {
  let navigate = useNavigate();

  const handleClick = () => {
    localStorage.clear();
    // localStorage.getItem("globalVarPassword").clear;
    // localStorage.getItem("globalVarUserId").clear;
    // localStorage.getItem("globalVarCustomerId").clear;
    // localStorage.getItem("globalVarAdminId").clear;
    // localStorage.getItem("globalVarAirlineId").clear;
    console.log("The link was clicked logout");
    navigate("/");
  };

  return (
    <div className="container">
      <h2> Logout Page</h2>
      <h4> are you sure you want to log out?</h4>
      <Button variant="contained" className="Button" onClick={handleClick}>
        Log out
      </Button>
    </div>
  );
}

export default Logout;
