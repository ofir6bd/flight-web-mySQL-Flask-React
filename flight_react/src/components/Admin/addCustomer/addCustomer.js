import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
// import "./login.css";
// import { UseAuth } from "../useAuth/useAuth";
import { apiAddCustomer } from "../../../apiHandler/apiHandlerAdmin";

export default function AddCustomerForm() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [address, setAddress] = useState("");
  const [phoneNo, setPhoneNo] = useState("");
  const [creditCardNo, setCreditCardNo] = useState("");
  const [userID, setUserID] = useState("");

  const handleFirstName = (event) => {
    setFirstName(event.target.value);
  };
  const handleLastName = (event) => {
    setLastName(event.target.value);
  };
  const handleAddress = (event) => {
    setAddress(event.target.value);
  };
  const handlePhoneNo = (event) => {
    setPhoneNo(event.target.value);
  };
  const handleCreditCardNo = (event) => {
    setCreditCardNo(event.target.value);
  };
  const handleUserID = (event) => {
    setUserID(event.target.value);
  };
  return (
    <div className="container">
      <h2> Add Customer page</h2>
      <TextField
        id="outlined-basic"
        label="First Name:"
        variant="outlined"
        onChange={handleFirstName}
      />
      <TextField
        id="outlined-basic"
        label="Last Name:"
        variant="outlined"
        onChange={handleLastName}
      />
      <TextField
        id="outlined-basic"
        label="Address:"
        variant="outlined"
        onChange={handleAddress}
      />
      <TextField
        id="outlined-basic"
        label="Phone No:"
        variant="outlined"
        onChange={handlePhoneNo}
      />
      <TextField
        id="outlined-basic"
        label="Credit Card No:"
        variant="outlined"
        onChange={handleCreditCardNo}
      />
      <TextField
        id="outlined-basic"
        label="User ID:"
        variant="outlined"
        onChange={handleUserID}
      />
      <Button
        variant="contained"
        className="Button"
        onClick={() =>
          apiAddCustomer(
            firstName,
            lastName,
            address,
            phoneNo,
            creditCardNo,
            userID
          ).then((response) => console.log(response))
        }
      >
        Add Customer
      </Button>
    </div>
  );
}
