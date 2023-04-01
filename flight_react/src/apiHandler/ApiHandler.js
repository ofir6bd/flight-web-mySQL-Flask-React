export function getFlights() {
  var url = "http://127.0.0.1:5000/API/flights";
  console.log(url);

  var flights = fetch(url).then((response) => response.json());

  return flights;
}

export function createUser(username, password, email, user_role) {
  console.log("first signup");
  console.log(username);
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
  console.log(response);
  return response;
}

export function checkLogin(email, password) {
  console.log("first login");
  console.log(email);
  const requestOptions = { method: "GET" };
  var url =
    "http://127.0.0.1:5000/API/check_login/?email=" +
    email +
    "&password=" +
    password;

  var response = fetch(url, requestOptions).then((response) => response.json());
  console.log(response);
  return response;
}
