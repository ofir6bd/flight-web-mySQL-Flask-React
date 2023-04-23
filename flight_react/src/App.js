import "./App.css";
import SearchFlight from "./components/searchFlight/SearchFlight";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import Flights from "./components/flights/flights";
import { Routes, Route } from "react-router-dom";
import { useNavigate } from "react-router";
import Login from "./components/login/login";
import Logout from "./components/logout/logout";
import Signup from "./components/signup/signup";
import CustomerPage from "./components/Customer/CustomerPage";
import AdminPage from "./components/Admin/AdminPage";
import AirlinePage from "./components/Airline/AirlinePage";
import Navbar from "./components/navbar/index";
import AddAirlineForm from "./components/Admin/addAirline/addAirline";
import AddCustomerForm from "./components/Admin/addCustomer/addCustomer";
import AddAdminForm from "./components/Admin/addAdmin/addAdmin";
import AddFlightForm from "./components/Airline/addFlight/addFlight";
import Verification from "./components/verification/verification";
import RemoveAirlineForm from "./components/Admin/removeAirline/removeAirline";
import RemoveCustomerForm from "./components/Admin/removeCustomer/removeCustomer";
import RemoveAdminForm from "./components/Admin/removeAdmin/removeAdmin";
import RemoveTicketForm from "./components/Customer/removeTicket/removeTicket";
import RemoveFlightForm from "./components/Airline/removeFlight/removeFlight";
import UpdateCustomerForm from "./components/Customer/updateCustomer/updateCustomer";
import UpdateAirlineForm from "./components/Airline/updateAirline/updateAirline";
import UpdateFlightForm from "./components/Airline/updateFlight/updateFlight";
import ChooseFlightForm from "./components/Airline/chooseFlight/chooseFlight";
import RegisterAsCustomerForm from "./components/registerAsCustomer/registerAsCustomer";
import RegisterAsAirlineForm from "./components/registerAsAirline/registerAsAirline";

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
          <Route path="verification" element={<Verification />} />
          <Route path="addFlight" element={<AddFlightForm />} />
          <Route path="removeAirline" element={<RemoveAirlineForm />} />
          <Route path="removeCustomer" element={<RemoveCustomerForm />} />
          <Route path="removeAdmin" element={<RemoveAdminForm />} />
          <Route path="removeTicket" element={<RemoveTicketForm />} />
          <Route path="removeFlight" element={<RemoveFlightForm />} />
          <Route path="updateCustomer" element={<UpdateCustomerForm />} />
          <Route path="updateAirline" element={<UpdateAirlineForm />} />
          <Route path="chooseFlight" element={<ChooseFlightForm />} />
          <Route path="updateFlight" element={<UpdateFlightForm />} />
          <Route
            path="registerAsCustomer"
            element={<RegisterAsCustomerForm />}
          />
          <Route path="registerAsAirline" element={<RegisterAsAirlineForm />} />
        </Routes>
      </LocalizationProvider>
    </div>
  );
}

export default App;
