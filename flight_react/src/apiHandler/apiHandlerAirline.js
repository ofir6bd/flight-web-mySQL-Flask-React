export function apiAddFlight(
  origin_country_id,
  destination_country_id,
  departure_time,
  landing_time,
  remaining_tickets
) {
  console.log("start api apiAddFlight");
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
