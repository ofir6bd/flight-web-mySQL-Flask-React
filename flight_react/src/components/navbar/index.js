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
