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
