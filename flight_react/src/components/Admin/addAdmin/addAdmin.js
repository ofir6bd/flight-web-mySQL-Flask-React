import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
// import "./login.css";
// import { UseAuth } from "../useAuth/useAuth";
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
  // const handleUserID = (event) => {
  //   setUserID(event.target.value);
  // };

  useEffect(() => {
    function fetchData() {
      apiGetAllUsersPreAdmin().then((response) => {
        setOptions(response);
        // console.log(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    console.log("start add admin handleClick");
    var user_id = "";
    if (userID) {
      user_id = userID.id;
    }
    apiAddAdmin(firstName, lastName, user_id).then((response) => {
      if (response.success) {
        console.log(response);
        localStorage.setItem("globalVarMessage", response.success);
        localStorage.setItem("globalVarMessageType", "success");
        navigate("/adminPage");
      } else {
        console.log(response);
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
          getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
          placeholder="Connect to user:"
        />
      </div>
      <Button variant="contained" className="Button" onClick={handleClick}>
        Add Admin
      </Button>
    </div>
  );
}
