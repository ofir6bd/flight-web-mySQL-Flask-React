export function apiAddAirline(email, password, name, country_id, user_id) {
  console.log("start api apiAddAirline");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/admin/add_airline?email=" +
    email +
    "&password=" +
    password +
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
  email,
  password,
  firstName,
  lastName,
  address,
  phoneNo,
  creditCardNo,
  user_id
) {
  console.log("start api apiAddCustomer");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/admin/add_customer?email=" +
    email +
    "&password=" +
    password +
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
