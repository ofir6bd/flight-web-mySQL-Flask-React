import React from "react";

import { Button } from "@mui/material";
import "./verification.css";
import { apiAddTicket } from "../../apiHandler/apiHandlerCustomer";
import { useNavigate } from "react-router";

function Verification() {
  let navigate = useNavigate();

  const handleClick = () => {
    console.log("start Verification handleClick");
    apiAddTicket(
      localStorage.getItem("globalVarEmail"),
      localStorage.getItem("globalVarPassword"),
      3
    ).then((response) => {
      if (response.success) {
        localStorage.setItem("globalVarMessage", response.success);
      } else if (response.error) {
        localStorage.setItem("globalVarMessage", response.error);
      }
    });
    setTimeout(() => {
      navigate("/");
    }, 800);
  };

  return (
    <div className="container">
      <h2> Verification page</h2>
      <h4> Are you sure you want to book this flight?</h4>
      <Button variant="contained" className="Button" onClick={handleClick}>
        Sure
      </Button>
    </div>
  );
}

export default Verification;
