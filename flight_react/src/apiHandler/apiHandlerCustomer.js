export function apiAddTicket(email, password, flight_id) {
  console.log("start api apiAddTicket");
  console.log(email);
  console.log(password);
  console.log(flight_id);
  const requestOptions = { method: "POST" };
  var url =
    "http://127.0.0.1:5000/API/customer/add_ticket?email=" +
    email +
    "&password=" +
    password +
    "&flight_id=" +
    flight_id;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}
