import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import {
  apiGetCustomerDetails,
  apiRegisterAsCustomer,
} from "../../apiHandler/apiHandlerCustomer";
import { useNavigate } from "react-router";
import Messages from "../../messages";

function RegisterAsCustomerForm() {
  let navigate = useNavigate();
  // const [value, setValue] = React.useState(null);
  //  const [options, setOptions] = React.useState([]);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [address, setAddress] = useState("");
  const [phoneNo, setPhoneNo] = useState("");
  const [creditCardNo, setCreditCardNo] = useState("");
  //  const [userID, setUserID] = useState("");

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

  const handleClick = () => {
    apiRegisterAsCustomer(
      firstName,
      lastName,
      address,
      phoneNo,
      creditCardNo,
      localStorage.getItem("globalVarUserId")
    ).then((response) => {
      if (response.success) {
        console.log(response);
        localStorage.setItem("globalVarMessage", response.success);
        localStorage.setItem("globalVarMessageType", "success");
        apiGetCustomerDetails()
          .then((response) => {
            localStorage.setItem("globalVarCustomerId", response.id);
          })
          .then(() => {
            navigate("/customerPage");
            // setTimeout(() => {

            // }, 1000);
          });
      } else {
        console.log(response);
        localStorage.setItem("globalVarMessage", JSON.stringify(response));
        localStorage.setItem("globalVarMessageType", "error");
        navigate("/registerAsCustomer");
      }
    });
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Register as Customer Page</h2>
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
      <Button variant="contained" className="Button" onClick={handleClick}>
        Register As Customer
      </Button>
    </div>
  );
}

export default RegisterAsCustomerForm;
