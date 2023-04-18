export function apiAddTicket(flight_id) {
  console.log("start api apiAddTicket");
  const requestOptions = { method: "POST" };
  var url =
    "http://127.0.0.1:5000/API/customer/add_ticket?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword") +
    "&flight_id=" +
    flight_id;
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiRemoveTicket(ticket_id) {
  console.log("start api apiRemoveTicket");
  console.log(ticket_id);
  const requestOptions = { method: "DELETE" };
  var url =
    "http://127.0.0.1:5000/API/customer/delete_my_ticket/" +
    ticket_id +
    "/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}

export function apiGetMyTickets() {
  console.log("start api apiGetMyTickets");
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/customer/my_tickets/?email=" +
    localStorage.getItem("globalVarEmail") +
    "&password=" +
    localStorage.getItem("globalVarPassword");
  var response = fetch(url, requestOptions).then((response) => response.json());
  return response;
}
