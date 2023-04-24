import React, { useEffect } from "react";
import { Button } from "@mui/material";
import {
  apiGetAllAdmins,
  apiRemoveAdmin,
} from "../../../apiHandler/apiHandlerAdmin";
import Messages from "../../../messages";
import { useNavigate } from "react-router";
import Select from "react-select";

export default function RemoveAdminForm() {
  let navigate = useNavigate();
  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);

  //to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetAllAdmins().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  //the actions for the button submit
  const handleClick = () => {
    if (value !== null) {
      apiRemoveAdmin(value.id).then((response) => {
        if (response.success) {
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
          navigate("/adminPage");
        } else {
          localStorage.setItem("globalVarMessage", JSON.stringify(response));
          localStorage.setItem("globalVarMessageType", "error");
          navigate("/removeAdmin");
        }
      });
    }
  };

  return (
    <div className="container">
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h2> Remove Admin page</h2>
      <Select
        name="Admin"
        options={options}
        value={value}
        onChange={setValue}
        getOptionLabel={(option) =>
          "ID: " +
          option.id +
          ", First Name: " +
          option.first_name +
          ", Last Name: " +
          option.last_name +
          ", User ID: " +
          option.user_id
        }
        getOptionValue={(option) => option.id}
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Remove Admin
      </Button>
    </div>
  );
}
