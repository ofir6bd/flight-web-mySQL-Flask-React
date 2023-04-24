import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
// import "./login.css";
// import { UseAuth } from "../useAuth/useAuth";
import { apiAddCustomer } from "../../../apiHandler/apiHandlerAdmin";
import { useNavigate } from "react-router";
import { apiGetAllUsersPreCustomer } from "../../../apiHandler/apiHandlerAdmin";
import Select from "react-select";
import Messages from "../../../messages";

export default function AddCustomerForm() {
  let navigate = useNavigate();
  const [options, setOptions] = React.useState([]);
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

  useEffect(() => {
    function fetchData() {
      apiGetAllUsersPreCustomer().then((response) => {
        setOptions(response);
        // console.log(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    console.log("start add customer handleClick");
    var user_id = "";
    if (userID) {
      user_id = userID.id;
    }
    apiAddCustomer(
      firstName,
      lastName,
      address,
      phoneNo,
      creditCardNo,
      user_id
    ).then((response) => {
      if (response.success) {
        console.log(response);
        localStorage.setItem("globalVarMessage", response.success);
        localStorage.setItem("globalVarMessageType", "success");
        navigate("/adminPage");
      } else {
        console.log(response);
        localStorage.setItem("globalVarMessage", JSON.stringify(response));
        localStorage.setItem("globalVarMessageType", "error");
        navigate("/addCustomer");
      }
    });
    // .then(() => {
    //   navigate("/adminPage");
    // });
  };
  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
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
      <div style={{ width: "800px" }}>
        <Select
          name="user_id"
          options={options}
          value={userID}
          onChange={setUserID}
          getOptionLabel={(option) =>
            "ID: " +
            option.id +
            ", Username: " +
            option.username +
            ", Email: " +
            option.email
          }
          getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
          placeholder="Connect to user:"
        />
      </div>
      <Button variant="contained" className="Button" onClick={handleClick}>
        Add Customer
      </Button>
    </div>
  );
}
