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
  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);

  let navigate = useNavigate();

  useEffect(() => {
    function fetchData() {
      apiGetAllAdmins().then((response) => {
        setOptions(response);
        console.log(response);
      });
    }
    fetchData();
  }, []);

  const handleClick = () => {
    if (value !== null) {
      apiRemoveAdmin(value.id).then((response) => {
        if (response.success) {
          console.log(response);
          localStorage.setItem("globalVarMessage", response.success);
          localStorage.setItem("globalVarMessageType", "success");
          navigate("/adminPage");
        } else {
          console.log(response);
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
        getOptionValue={(option) => option.id} // It should be unique value in the options. E.g. ID
      />

      <Button variant="contained" className="Button" onClick={handleClick}>
        Remove Admin
      </Button>
    </div>
  );
}
