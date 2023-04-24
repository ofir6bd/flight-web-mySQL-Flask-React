export function apiAddAirline(name, country_id, user_id) {
  console.log("start api apiAddAirline");
  const requestOptions = { method: "POST" };
  var url =
    "http://127.0.0.1:5000/API/admin/add_airline?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword") +
    "&name=" +
    name +
    "&country_id=" +
    country_id +
    "&user_id=" +
    user_id;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiAddCustomer(
  firstName,
  lastName,
  address,
  phoneNo,
  creditCardNo,
  user_id
) {
  console.log("start api apiAddCustomer");
  const requestOptions = { method: "POST" };
  var url =
    "http://127.0.0.1:5000/API/admin/add_customer?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword") +
    "&first_name=" +
    firstName +
    "&last_name=" +
    lastName +
    "&address=" +
    address +
    "&phone_no=" +
    phoneNo +
    "&credit_card_no=" +
    creditCardNo +
    "&user_id=" +
    user_id;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiAddAdmin(firstName, lastName, user_id) {
  console.log("start api apiAddAdmin");
  const requestOptions = { method: "POST" };
  var url =
    "http://127.0.0.1:5000/API/admin/add_admin?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword") +
    "&first_name=" +
    firstName +
    "&last_name=" +
    lastName +
    "&user_id=" +
    user_id;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiRemoveAirline(airline_id) {
  console.log("start api apiRemoveAirline");
  const requestOptions = { method: "DELETE" };
  var url =
    "http://127.0.0.1:5000/API/admin/delete_airline/" +
    airline_id +
    "/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiRemoveCustomer(customer_id) {
  console.log("start api apiRemoveCustomer");
  const requestOptions = { method: "DELETE" };
  var url =
    "http://127.0.0.1:5000/API/admin/delete_customer/" +
    customer_id +
    "/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiGetAllAdmins() {
  console.log("start api apiGetAllAdmins");
  var url =
    "http://127.0.0.1:5000/API/admin/get_all_admins?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url).then((response) => response.json());
  return response;
}

export function apiRemoveAdmin(customer_id) {
  console.log("start api apiRemoveAdmin");
  const requestOptions = { method: "DELETE" };
  var url =
    "http://127.0.0.1:5000/API/admin/delete_admin/" +
    customer_id +
    "/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiGetAllUsersPreCustomer() {
  console.log("start api apiGetAllUsersPreCustomer");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/admin/get_all_pre_customers/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiGetAllUsersPreAdmin() {
  console.log("start api apiGetAllUsersPreAdmin");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/admin/get_all_pre_admin/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiGetAllUsersPreAirline() {
  console.log("start api apiGetAllUsersPreAirline");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/admin/get_all_pre_airline/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}
