import React from "react";
import logo from "../../images/logo.PNG";
import {
  Nav,
  NavLink,
  NavMenu,
  NavBtn,
  NavBtnLink,
} from "./NavbarElements";
import "./index.css";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <>
      <Nav>
        <div>
          <Link to="/">
            <img className="logo" src={logo} alt="Logo" />
          </Link>
        </div>
        {localStorage.getItem("globalVarAdminId") ? (
          <NavMenu>
            <NavLink to="/addCustomer" activestyle={"true"}>
              Add Customer
            </NavLink>
            <NavLink to="/addAdmin" activestyle={"true"}>
              Add Admin
            </NavLink>
            <NavLink to="/addAirline" activestyle={"true"}>
              Add Airline
            </NavLink>
            <NavLink to="/removeAirline" activestyle={"true"}>
              Remove Airline
            </NavLink>
            <NavLink to="/removeCustomer" activestyle={"true"}>
              Remove Customer
            </NavLink>
            <NavLink to="/removeAdmin" activestyle={"true"}>
              Remove Admin
            </NavLink>
          </NavMenu>
        ) : localStorage.getItem("globalVarCustomerId") ? (
          <NavMenu>
            <NavLink to="/searchFlight" activestyle={"true"}>
              Search Flights
            </NavLink>
            <NavLink to="/removeTicket" activestyle={"true"}>
              Remove Ticket
            </NavLink>
            <NavLink to="/updateCustomer" activestyle={"true"}>
              Update Customer
            </NavLink>
          </NavMenu>
        ) : localStorage.getItem("globalVarAirlineId") ? (
          <NavMenu>
            <NavLink to="/addFlight" activestyle={"true"}>
              Add Flight
            </NavLink>
            <NavLink to="/removeFlight" activestyle={"true"}>
              Remove Flight
            </NavLink>
            <NavLink to="/updateAirline" activestyle={"true"}>
              Update Airline
            </NavLink>
            <NavLink to="/chooseFlight" activestyle={"true"}>
              Update Flight
            </NavLink>
          </NavMenu>
        ) : localStorage.getItem("globalVarUserId") &&
          localStorage.getItem("globalVarUserRole") == 3 ? (
          <NavMenu>
            <NavLink to="/registerAsCustomer" activestyle={"true"}>
              Register as Customer
            </NavLink>
          </NavMenu>
        ) : localStorage.getItem("globalVarUserId") &&
          localStorage.getItem("globalVarUserRole") == 2 ? (
          <NavMenu>
            <NavLink to="/registerAsAirline" activestyle={"true"}>
              Register as Airline
            </NavLink>
          </NavMenu>
        ) : (
          <NavMenu>
            <NavLink to="/searchFlight" activestyle={"true"}>
              Search Flights
            </NavLink>
          </NavMenu>
        )}
        {!localStorage.getItem("globalVarUserId") ? (
          <div>
            <div>
              <NavBtn>
                <NavBtnLink to="/login">Sign In</NavBtnLink>
              </NavBtn>
            </div>
            <div>
              <NavBtn>
                <NavBtnLink to="/signup">Sign Up</NavBtnLink>
              </NavBtn>
            </div>
          </div>
        ) : (
          <div>
            <NavBtn>
              <NavBtnLink to="/logout">Logout</NavBtnLink>
            </NavBtn>
          </div>
        )}
      </Nav>
    </>
  );
};

export default Navbar;
