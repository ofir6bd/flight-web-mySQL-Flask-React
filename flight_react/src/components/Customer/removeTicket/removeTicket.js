import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiGetMyTickets } from "../../../apiHandler/apiHandlerCustomer";
import { apiRemoveTicket } from "../../../apiHandler/apiHandlerCustomer";
import { useNavigate } from "react-router";
import Select from "react-select";

export default function RemoveTicketForm() {
  const [value, setValue] = React.useState();
  const [options, setOptions] = React.useState([]);

  let navigate = useNavigate();

  useEffect(() => {
    function fetchData() {
      apiGetMyTickets().then((response) => {
        setOptions(response);
        console.log(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    if (value !== null) {
      apiRemoveTicket(value.ticket_id)
        .then((response) => {
          if (response.success) {
            console.log(response);
            localStorage.setItem("globalVarMessage", response.success);
            localStorage.setItem("globalVarMessageType", "success");
          } else {
            console.log(response);
            localStorage.setItem("globalVarMessage", JSON.stringify(response));
            localStorage.setItem("globalVarMessageType", "error");
          }
        })
        .then(() => {
          navigate("/customerPage");
        });
    }
  };

  // const handleChange = (selectedOption) => {
  //   setValue(selectedOption);
  //   console.log(`Option selected:`, selectedOption);
  //   console.log(`value:`, value);
  // };

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
