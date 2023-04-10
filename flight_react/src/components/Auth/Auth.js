import {
  apiCheckLogin,
  apiCheckAdmin,
  apiCheckCustomer,
  apiCheckAirline,
} from "../../apiHandler/ApiHandler";
// import React, { Component, useState } from "react";

export const checkIfUserCustomer = (email, password, val) => {
  apiCheckCustomer(email, password, val)
    .then((response) => console.log(response))
    .catch((err) => console.log(err));
};
export const checkIfUserAdmin = (email, password, val) => {
  apiCheckAdmin(email, password, val)
    .then((response) => console.log(response))
    .catch((err) => console.log(err));
};
export const checkIfUserAirline = (email, password, val) => {
  apiCheckAirline(email, password, val)
    .then((response) => console.log(response))
    .catch((err) => console.log(err));
};

export const Auth = (email, password) => {
  console.log("start Auth");
  apiCheckLogin(email, password)
    .then((response) => {
      if (response.user_id) {
        checkIfUserCustomer(email, password, response.user_id);
        checkIfUserAdmin(email, password, response.user_id);
        checkIfUserAirline(email, password, response.user_id);
      }
    })
    .then(() => {
      console.log("data");
    })
    .catch((err) => console.log(err));
};
