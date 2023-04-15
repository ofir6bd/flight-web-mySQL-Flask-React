import "./App.css";
import SearchFlight from "./components/searchFlight/SearchFlight";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import Flights from "./components/flights/flights";
import { Routes, Route } from "react-router-dom";
import { useNavigate } from "react-router";
import { Button } from "@mui/material";
import Login from "./components/login/login";
import Logout from "./components/logout/Logout";
import Signup from "./components/signup/signup";
import CustomerPage from "./components/Customer/CustomerPage";
import AdminPage from "./components/Admin/AdminPage";
import AirlinePage from "./components/Airline/AirlinePage";
import Navbar from "./components/navbar/index";
import AddAirlineForm from "./components/Admin/addAirline/addAirline";
import AddCustomerForm from "./components/Admin/addCustomer/addCustomer";
import AddAdminForm from "./components/Admin/addAdmin/addAdmin";
import AddFlightForm from "./components/Airline/addFlight/addFlight";

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
          <Route path="logout" element={<Logout />} />
          <Route path="signup" element={<Signup />} />
          <Route path="customerPage" element={<CustomerPage />} />
          <Route path="adminPage" element={<AdminPage />} />
          <Route path="airlinePage" element={<AirlinePage />} />
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
