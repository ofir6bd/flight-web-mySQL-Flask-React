import React, { useState, useEffect } from "react";
import { Button } from "@mui/material";
import { apiGetMyTickets } from "../../../apiHandler/apiHandlerCustomer";
import { apiRemoveTicket } from "../../../apiHandler/apiHandlerCustomer";
import { useNavigate } from "react-router";
import Select from "react-select";

export default function RemoveTicketForm() {
  let navigate = useNavigate();
  const [value, setValue] = React.useState();
  const [options, setOptions] = React.useState([]);

  //to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetMyTickets().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  //the actions post button submit
  const handleClick = () => {
    if (value !== null) {
      apiRemoveTicket(value.ticket_id)
        .then((response) => {
          if (response.success) {
            localStorage.setItem("globalVarMessage", response.success);
            localStorage.setItem("globalVarMessageType", "success");
          } else {
            localStorage.setItem("globalVarMessage", JSON.stringify(response));
            localStorage.setItem("globalVarMessageType", "error");
          }
        })
        .then(() => {
          navigate("/customerPage");
        });
    }
  };

  return (
    <div className="container">
      <h2> Remove Ticket page</h2>
      <Select
        name="ticket"
        options={options}
        value={value}
        onChange={setValue}
        getOptionLabel={(option) =>
          "ID: " +
          option.ticket_id +
          ", From: " +
          option.origin_country +
          ", To: " +
          option.destination_country +
          ", Departure Time: " +
          option.departure_time +
          ", Landing Time: " +
          option.landing_time
        }
        getOptionValue={(option) => option.ticket_id} // It should be unique value in the options. E.g. ID
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Remove Ticket
      </Button>
    </div>
  );
}
