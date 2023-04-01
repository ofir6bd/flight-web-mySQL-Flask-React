function getFlights() {
  var url = "http://127.0.0.1:5000/API/flights";
  console.log(url);

  var flights = fetch(url).then((response) => response.json());

  return flights;
}

export default getFlights;
