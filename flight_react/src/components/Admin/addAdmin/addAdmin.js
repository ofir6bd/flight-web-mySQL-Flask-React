import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import { apiAddAdmin } from "../../../apiHandler/apiHandlerAdmin";
import { useNavigate } from "react-router";
import Select from "react-select";
import { apiGetAllUsersPreAdmin } from "../../../apiHandler/apiHandlerAdmin";
import Messages from "../../../messages";

export default function AddAdminForm() {
  let navigate = useNavigate();
  const [options, setOptions] = React.useState([]);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [userID, setUserID] = useState("");

  const handleFirstName = (event) => {
    setFirstName(event.target.value);
  };
  const handleLastName = (event) => {
    setLastName(event.target.value);
  };

// to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetAllUsersPreAdmin().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  //the actions post button submit
  const handleClick = () => {
    var user_id = "";
    if (userID) {
      user_id = userID.id;
    }
    apiAddAdmin(firstName, lastName, user_id).then((response) => {
      if (response.success) {
        localStorage.setItem("globalVarMessage", response.success);
        localStorage.setItem("globalVarMessageType", "success");
        navigate("/adminPage");
      } else {
        localStorage.setItem("globalVarMessage", JSON.stringify(response));
        localStorage.setItem("globalVarMessageType", "error");
        navigate("/addAdmin");
      }
    });
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
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
          getOptionValue={(option) => option.id} 
          placeholder="Connect to user:"
        />
      </div>
      <Button variant="contained" className="Button" onClick={handleClick}>
        Add Admin
      </Button>
    </div>
  );
}
