export function apiAddFlight(
  origin_country_id,
  destination_country_id,
  departure_time,
  landing_time,
  remaining_tickets
) {
  console.log("start api apiAddFlight");
  console.log(remaining_tickets);
  const requestOptions = { method: "POST" };
  var url =
    "http://127.0.0.1:5000/API/airline/add_flight?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword") +
    "&origin_country_id=" +
    origin_country_id +
    "&destination_country_id=" +
    destination_country_id +
    "&departure_time=" +
    departure_time +
    "&landing_time=" +
    landing_time +
    "&remaining_tickets=" +
    remaining_tickets;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiRemoveFlight(flight_id) {
  console.log("start api apiRemoveFlight");
  const requestOptions = { method: "DELETE" };
  var url =
    "http://127.0.0.1:5000/API/airline/delete_my_flight/" +
    flight_id +
    "/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiGetMyFlights() {
  console.log("start api apiGetMyFlights");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/airline/my_flights/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiGetAirlineDetails() {
  console.log("start api apiGetAirlineDetails");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/airline/get_airline_details/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiUpdateAirline(name) {
  console.log("start api apiUpdateAirline");
  const requestOptions = { method: "PUT" };
  var url =
    "http://127.0.0.1:5000/API/airline/update_airline?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword") +
    "&name=" +
    name;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiUpdateFlight(flight) {
  console.log("start api apiUpdateFlight");
  const requestOptions = { method: "PUT" };
  var url =
    "http://127.0.0.1:5000/API/airline/update_flight/" +
    flight.flight_id +
    "?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword") +
    "&origin_country_id=" +
    flight.origin_country_id +
    "&destination_country_id=" +
    flight.destination_country_id +
    "&departure_time=" +
    flight.departure_time +
    "&landing_time=" +
    flight.landing_time +
    "&remaining_tickets=" +
    flight.remaining_tickets;

  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

// export function apiGetCustomerDetails() {
//   console.log("start api apiGetCustomerDetails");
//   const requestOptions = { method: "GET" };
//   var url =
//     "http://127.0.0.1:5000/API/airline/get_airline_details/?email=" +
//     localStorage.getItem("globalVarEmail") +
//     "&password=" +
//     localStorage.getItem("globalVarPassword");
//   var response = fetch(url, requestOptions).then((response) => response.json());
//   return response;
// }

export function apiRegisterAsAirline(name, country_id, user_id) {
  console.log("start api apiRegisterAsAirline");
  const requestOptions = { method: "POST" };
  var url =
    "http://127.0.0.1:5000/API/register_as_airline?email=" +
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
