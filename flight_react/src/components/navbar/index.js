import React from "react";
import logo from "../../images/logo.PNG";
import {
  Nav,
  NavLink,
  // Bars,
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
            <NavLink to="/addCustomer" activeStyle>
              Add Customer
            </NavLink>
            <NavLink to="/addAdmin" activeStyle>
              Add Admin
            </NavLink>
            <NavLink to="/addAirline" activeStyle>
              Add Airline
            </NavLink>
            <NavLink to="/removeAirline" activeStyle>
              Remove Airline
            </NavLink>
            <NavLink to="/removeCustomer" activeStyle>
              Remove Customer
            </NavLink>
            <NavLink to="/removeAdmin" activeStyle>
              Remove Admin
            </NavLink>
          </NavMenu>
        ) : localStorage.getItem("globalVarCustomerId") ? (
          <NavMenu>
            <NavLink to="/searchFlight" activeStyle>
              Search Flights
            </NavLink>
            <NavLink to="/removeTicket" activeStyle>
              Remove Ticket
            </NavLink>
            <NavLink to="/updateCustomer" activeStyle>
              Update Customer
            </NavLink>
          </NavMenu>
        ) : localStorage.getItem("globalVarAirlineId") ? (
          <NavMenu>
            <NavLink to="/addFlight" activeStyle>
              Add Flight
            </NavLink>
            <NavLink to="/removeFlight" activeStyle>
              Remove Flight
            </NavLink>
            <NavLink to="/updateAirline" activeStyle>
              Update Airline
            </NavLink>
            <NavLink to="/chooseFlight" activeStyle>
              Update Flight
            </NavLink>
          </NavMenu>
        ) : localStorage.getItem("globalVarUserId") &&
          localStorage.getItem("globalVarUserRole") == 3 ? (
          <NavMenu>
            <NavLink to="/registerAsCustomer" activeStyle>
              Register as Customer
            </NavLink>
          </NavMenu>
        ) : localStorage.getItem("globalVarUserId") &&
          localStorage.getItem("globalVarUserRole") == 2 ? (
          <NavMenu>
            <NavLink to="/registerAsAirline" activeStyle>
              Register as Airline
            </NavLink>
          </NavMenu>
        ) : (
          <NavMenu>
            <NavLink to="/searchFlight" activeStyle>
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
