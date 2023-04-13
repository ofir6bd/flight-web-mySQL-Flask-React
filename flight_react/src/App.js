import "./App.css";
import SearchFlight from "./components/searchFlight/SearchFlight";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import Flights from "./components/flights/flights";
import { Routes, Route } from "react-router-dom";
import { useNavigate } from "react-router";
import { Button } from "@mui/material";
import Login from "./components/login/login";
import Signup from "./components/signup/signup";
import Navbar from "./components/navbar/index";
import AddAirlineForm from "./components/Admin/addAirline/addAirline";
import AddCustomerForm from "./components/Admin/addAirline/addCustomer";
import AddAdminForm from "./components/Admin/addAirline/addAdmin";
import AddFlightForm from "./components/Airline/addFlight";
import { StoreProvider, createStore } from "easy-peasy";



function App() {
  let navigate = useNavigate();

  function navigateTo(path) {
    navigate(path);
  }

  return (
    
    <div className="App">
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <Navbar />
        <Routes>
          <Route path="" element={<SearchFlight />} />
          <Route path="login" element={<Login />} />
          <Route path="signup" element={<Signup />} />
          <Route path="flights" element={<Flights />} />
          <Route path="addAirline" element={<AddAirlineForm />} />
          <Route path="addCustomer" element={<AddCustomerForm />} />
          <Route path="addAdmin" element={<AddAdminForm />} />

          <Route path="addFlight" element={<AddFlightForm />} />
        </Routes>
      </LocalizationProvider>
    </div>

  );
}

export default App;
