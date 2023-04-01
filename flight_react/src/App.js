import "./App.css";
import SearchFlight from "./components/searchFlight/SearchFlight";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import Flights from "./components/flights/flights";
import { Routes, Route } from "react-router-dom";
import { useNavigate } from "react-router";
import { Button } from "@mui/material";

function App() {
  let navigate = useNavigate();

  function handleClick() {
    navigate("/search_flights");
  }

  return (
    <div className="App">
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <Routes>
          <Route path="" element={<SearchFlight />} />
          <Route path="flights" element={<Flights />} />
        </Routes>
      </LocalizationProvider>
    </div>
  );
}

export default App;
