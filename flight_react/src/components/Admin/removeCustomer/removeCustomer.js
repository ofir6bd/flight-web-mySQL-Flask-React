import React, { useEffect } from "react";
import { Button } from "@mui/material";
import { apiGetAllCustomers } from "../../../apiHandler/apiHandler";
import { apiRemoveCustomer } from "../../../apiHandler/apiHandlerAdmin";
import { useNavigate } from "react-router";
import Select from "react-select";
import Messages from "../../../messages";

export default function RemoveCustomerForm() {
  let navigate = useNavigate();
  const [value, setValue] = React.useState(null);
  const [options, setOptions] = React.useState([]);

//to load the options for the dropdown
  useEffect(() => {
    function fetchData() {
      apiGetAllCustomers().then((response) => {
        setOptions(response);
      });
    }
    fetchData();
  }, []);

  //for the actions post button submit
  const handleClick = () => {
    if (value !== null) {
      apiRemoveCustomer(value.id)
        .then((response) => {
          if (response.success) {
            localStorage.setItem("globalVarMessage", response.success);
            localStorage.setItem("globalVarMessageType", "success");
             navigate("/adminPage");
          } else {
            localStorage.setItem("globalVarMessage", JSON.stringify(response));
            localStorage.setItem("globalVarMessageType", "error");
             navigate("/removeCustomer");
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
      <h2> Remove Customer page</h2>
      <Select
        name="Customers"
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
          ", Address: " +
          option.address +
          ", Phone Number: " +
          option.pgone_no +
          ", Credit Card Number: " +
          option.credit_card_no +
          ", User ID: " +
          option.user_id
        }
        getOptionValue={(option) => option.id} 
      />
      <Button variant="contained" className="Button" onClick={handleClick}>
        Remove Customer
      </Button>
    </div>
  );
}
