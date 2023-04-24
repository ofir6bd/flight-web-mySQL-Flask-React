import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiUpdateCustomer } from "../../../apiHandler/apiHandlerCustomer";
import { useNavigate } from "react-router";
import { apiGetCustomerDetails } from "../../../apiHandler/apiHandlerCustomer";
import Messages from "../../../messages";

export default function AddCustomerForm() {
  let navigate = useNavigate();
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [address, setAddress] = useState("");
  const [phoneNo, setPhoneNo] = useState("");
  const [creditCardNo, setCreditCardNo] = useState("");
  const [options, setOptions] = React.useState([]);

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

  //to load the options for the button submit
  useEffect(() => {
    function fetchData() {
      apiGetCustomerDetails().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  //the actions post button submit
  const handleClick = () => {
    const userID = 1;
    apiUpdateCustomer(
      firstName,
      lastName,
      address,
      phoneNo,
      creditCardNo,
      userID
    ).then((response) => {
      if (response.success) {
        localStorage.setItem("globalVarMessage", response.success);
        localStorage.setItem("globalVarMessageType", "success");
        navigate("/customerPage");
      } else {
        localStorage.setItem("globalVarMessage", JSON.stringify(response));
        localStorage.setItem("globalVarMessageType", "error");
        navigate("/updateCustomer");
      }
    });
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Update Customer page</h2>
      <TextField
        id="outlined-basic"
        label={"First Name: " + options.first_name}
        variant="outlined"
        onChange={handleFirstName}
      />
      <TextField
        id="outlined-basic"
        label={"Last Name: " + options.last_name}
        variant="outlined"
        onChange={handleLastName}
      />
      <TextField
        id="outlined-basic"
        label={"Address: " + options.address}
        variant="outlined"
        onChange={handleAddress}
      />
      <TextField
        id="outlined-basic"
        label={"Phone No: " + options.phone_no}
        variant="outlined"
        onChange={handlePhoneNo}
      />
      <TextField
        id="outlined-basic"
        label={"Credit Card No: " + options.credit_card_no}
        variant="outlined"
        onChange={handleCreditCardNo}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Update Customer
      </Button>
    </div>
  );
}
