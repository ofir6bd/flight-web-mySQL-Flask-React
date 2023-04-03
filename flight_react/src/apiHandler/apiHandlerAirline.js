export function apiAddFlight(
  email,
  password,
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
    email +
    "&password=" +
    password +
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
