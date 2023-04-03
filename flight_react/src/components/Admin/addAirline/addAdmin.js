import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
// import "./login.css";
// import { UseAuth } from "../useAuth/useAuth";
import { apiAddAdmin } from "../../../apiHandler/apiHandlerAdmin";

export default function AddAdminForm() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [userID, setUserID] = useState("");

  const handleFirstName = (event) => {
    setFirstName(event.target.value);
  };
  const handleLastName = (event) => {
    setLastName(event.target.value);
  };
  const handleUserID = (event) => {
    setUserID(event.target.value);
  };
  return (
    <div className="container">
      <h2> Add Admin page</h2>
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
        label="User ID:"
        variant="outlined"
        onChange={handleUserID}
      />
      <Button
        variant="contained"
        className="Button"
        onClick={() =>
          apiAddAdmin(firstName, lastName, userID).then((response) =>
            console.log(response)
          )
        }
      >
        Add Admin
      </Button>
    </div>
  );
}
