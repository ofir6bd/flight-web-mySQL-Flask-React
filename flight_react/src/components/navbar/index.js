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
  const [logged_in, set_logged_in] = useState(0);

  return (
    <>
      <Nav>
        <NavMenu>
          <NavLink to="/" activeStyle>
            Search Flights
          </NavLink>
          <NavLink to="/addAirline" activeStyle>
            Add Airline
          </NavLink>
          <NavLink to="/addCustomer" activeStyle>
            Add Customer
          </NavLink>
          <NavLink to="/addAdmin" activeStyle>
            Add Admin
          </NavLink>

          <NavLink to="/addFlight" activeStyle>
            Add Flight
          </NavLink>

        </NavMenu>
        {!logged_in ? (
          <div>
            <NavBtn>
              <NavBtnLink to="/login">Sign In</NavBtnLink>
            </NavBtn>
            <NavBtn>
              <NavBtnLink to="/signup">Sign Up</NavBtnLink>
            </NavBtn>
          </div>
        ) : (
          <h1> User Already logged in</h1>
        )}
      </Nav>
    </>
  );
};

export default Navbar;
