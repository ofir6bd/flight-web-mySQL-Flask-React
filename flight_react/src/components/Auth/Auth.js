import {
  apiCheckLogin,
  apiCheckAdmin,
  apiCheckCustomer,
  apiCheckAirline,
} from "../../apiHandler/ApiHandler";

const setEmailGlobalStorage = (email) => {
  localStorage.setItem("globalVarEmail", email.toString());
  console.log(localStorage.getItem("globalVarEmail"));
};

const setPasswordGlobalStorage = (password) => {
  localStorage.setItem("globalVarPassword", password.toString());
  console.log(localStorage.getItem("globalVarPassword"));
};

const setUserIdGlobalStorage = (userID) => {
  localStorage.setItem("globalVarUserId", userID.toString());
  console.log(localStorage.getItem("globalVarUserId"));
};

const setCustomerIdGlobalStorage = (customerID) => {
  localStorage.setItem("globalVarCustomerId", customerID.toString());
  console.log(localStorage.getItem("globalVarCustomerId"));
};

const setAdminIdGlobalStorage = (adminID) => {
  localStorage.setItem("globalVarAdminId", adminID.toString());
  console.log(localStorage.getItem("globalVarAdminId"));
};

const setAirlineIdGlobalStorage = (airlineID) => {
  localStorage.setItem("globalVarAirlineId", airlineID.toString());
  console.log(localStorage.getItem("globalVarAirlineId"));
};

const checkIfUserCustomer = (email, password, user_id) => {
  apiCheckCustomer(email, password, user_id)
    .then((response) => {
      if (response.customer_id) {
        setCustomerIdGlobalStorage(response.customer_id);
      }
    })
    .catch((err) => console.log(err));
};
const checkIfUserAdmin = (email, password, user_id) => {
  apiCheckAdmin(email, password, user_id)
    .then((response) => {
      if (response.admin_id) {
        setCustomerIdGlobalStorage(response.admin_id);
      }
    })
    .catch((err) => console.log(err));
};
const checkIfUserAirline = (email, password, user_id) => {
  apiCheckAirline(email, password, user_id)
    .then((response) => {
      if (response.airline_id) {
        setCustomerIdGlobalStorage(response.airline_id);
      }
    })
    .catch((err) => console.log(err));
};

export function Auth(email, password) {
  

  apiCheckLogin(email, password)
    .then((response) => {
      if (response.user_id) {
        setEmailGlobalStorage(email);
        setPasswordGlobalStorage(password);
        setUserIdGlobalStorage(response.user_id);
        checkIfUserCustomer(email, password, response.user_id);
        checkIfUserAdmin(email, password, response.user_id);
        checkIfUserAirline(email, password, response.user_id);
      }
    })
    .catch((err) => console.log(err))
    
;

  // return null; // render the component to use the useGlobalState hook
}
