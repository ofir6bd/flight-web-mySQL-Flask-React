import React from "react";

import { Button } from "@mui/material";
import "./verification.css";
import { apiAddTicket } from "../../apiHandler/apiHandlerCustomer";
import { useNavigate } from "react-router";

function Verification(flightId) {
  let navigate = useNavigate();

  const handleClick = () => {
    apiAddTicket(
      localStorage.getItem("globalVarEmail"),
      localStorage.getItem("globalVarPassword"),
      flightId
    );
    navigate("/");
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
