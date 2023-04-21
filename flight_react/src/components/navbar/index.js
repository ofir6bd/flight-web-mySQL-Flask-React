import React, { useState } from "react";
import {
  Nav,
  NavLink,
  Bars,
  NavMenu,
  NavBtn,
  NavBtnLink,
} from "./NavbarElements";

const Navbar = () => {
  // const [logged_in, set_logged_in] = useState(0);

  return (
    <>
      <Nav>
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
            <NavLink to="/" activeStyle>
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
        ) : (
          <NavMenu>
            <NavLink to="/" activeStyle>
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
