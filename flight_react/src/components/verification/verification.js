import React from "react";

import { Button } from "@mui/material";
import "./verification.css";
import { apiAddTicket } from "../../apiHandler/apiHandlerCustomer";
import { useNavigate } from "react-router";
import SearchFlight from "../searchFlight/SearchFlight";

function Verification() {
  let navigate = useNavigate();

  const handleClick = () => {
    console.log("start Verification handleClick");
    apiAddTicket(
      localStorage.getItem("globalVarEmail"),
      localStorage.getItem("globalVarPassword"),
      3
    )
      .then((response) => {
        if (response.success) {
          console.log(response);
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
        } else if (response[0].error) {
          console.log(response);
          localStorage.setItem(
            "globalVarMessage",
            JSON.stringify(response[0].error)
          );
          localStorage.setItem("globalVarMessageType", "error");
        }
      })
      .then(() => navigate("/"));
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
