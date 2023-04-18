export function getFlights() {
  console.log("start api getFlights");
  var url = "http://127.0.0.1:5000/API/flights";
  var flights = fetch(url).then((response) => response.json());
  return flights;
}

export function createUser(username, password, email, user_role) {
  console.log("start api createUser");
  const requestOptions = { method: "POST" };
  var url =
    "http://127.0.0.1:5000/API/create_new_user?username=" +
    username +
    "&password=" +
    password +
    "&email=" +
    email +
    "&user_role=" +
    user_role;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiCheckLogin(email, password) {
  console.log("start api apiCheckLogin");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/check_login/?email=" +
    email +
    "&password=" +
    password;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiCheckAdmin(email, password, user_id) {
  console.log("start api apiCheckAdmin");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/get_admin_by_user_id/?email=" +
    email +
    "&password=" +
    password +
    "&user_id=" +
    user_id;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiCheckCustomer(email, password, user_id) {
  console.log("start api apiCheckCustomer");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/get_customer_by_user_id/?email=" +
    email +
    "&password=" +
    password +
    "&user_id=" +
    user_id;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiCheckAirline(email, password, user_id) {
  console.log("start api apiCheckAirline");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/get_airline_by_user_id/?email=" +
    email +
    "&password=" +
    password +
    "&user_id=" +
    user_id;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiGetAllAirlines() {
  console.log("start api getAllAirlines");
  var url = "http://127.0.0.1:5000/API/airlines";
  var response = fetch(url).then((response) => response.json());
  return response;
}

export function apiGetAllCustomers() {
  console.log("start api apiGetAllCustomers");
  var url =
    "http://127.0.0.1:5000/API/admin/get_all_customers?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url).then((response) => response.json());
  return response;
}


