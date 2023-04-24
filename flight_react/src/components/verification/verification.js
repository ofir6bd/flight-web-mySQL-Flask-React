import React from "react";
import { Button } from "@mui/material";
import "./verification.css";
import { apiAddTicket } from "../../apiHandler/apiHandlerCustomer";
import { useNavigate } from "react-router";

function Verification() {
  let navigate = useNavigate();

  //the action post button submit
  const handleClick = () => {
    apiAddTicket(localStorage.getItem("globalVarFlightID"))
      .then((response) => {
        if (response.success) {
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
        } else if (response[0].error) {
          localStorage.setItem(
            "globalVarMessage",
            JSON.stringify(response[0].error)
          );
          localStorage.setItem("globalVarMessageType", "error");
        }
      })
      .then(() => {
        localStorage.removeItem("globalVarFlightID");
        navigate("/");
      });
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
