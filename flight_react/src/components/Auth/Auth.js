import {
  apiCheckLogin,
  apiCheckAdmin,
  apiCheckCustomer,
  apiCheckAirline,
} from "../../apiHandler/apiHandler";

const setEmailGlobalStorage = (email) => {
  localStorage.setItem("globalVarEmail", email.toString());
};

const setPasswordGlobalStorage = (password) => {
  localStorage.setItem("globalVarPassword", password.toString());
};

const setUserIdGlobalStorage = (userID) => {
  localStorage.setItem("globalVarUserId", userID.toString());
};
const setUserRoleIdGlobalStorage = (userRole) => {
  localStorage.setItem("globalVarUserRole", userRole.toString());
};

const setCustomerIdGlobalStorage = (customerID) => {
  localStorage.setItem("globalVarCustomerId", customerID.toString());
};

const setAdminIdGlobalStorage = (adminID) => {
  localStorage.setItem("globalVarAdminId", adminID.toString());
};

const setAirlineIdGlobalStorage = (airlineID) => {
  localStorage.setItem("globalVarAirlineId", airlineID.toString());
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
        setAdminIdGlobalStorage(response.admin_id);
      }
    })
    .catch((err) => console.log(err));
};

const checkIfUserAirline = (email, password, user_id) => {
  apiCheckAirline(email, password, user_id)
    .then((response) => {
      if (response.airline_id) {
        setAirlineIdGlobalStorage(response.airline_id);
      }
    })
    .catch((err) => console.log(err));
};

//saving all the user data in the global storage
export function auth(email, password) {
  apiCheckLogin(email, password)
    .then((response) => {
      if (response.user_id) {
        setEmailGlobalStorage(email);
        setPasswordGlobalStorage(password);
        setUserIdGlobalStorage(response.user_id);
        setUserRoleIdGlobalStorage(response.user_role);
        checkIfUserCustomer(email, password, response.user_id);
        checkIfUserAdmin(email, password, response.user_id);
        checkIfUserAirline(email, password, response.user_id);
      }
    })
    .catch((err) => console.log(err));
}
