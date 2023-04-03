import { checkLogin, checkAdmin } from "../../apiHandler/ApiHandler";
import React, { Component, useState } from "react";

export const handleUserID = (email, password, val) => {
  checkAdmin(email, password, val)
    .then((response) => console.log(response))
    .catch((err) => console.log(err));
};

export const Auth = (email, password) => {
  console.log("start Auth");
  checkLogin(email, password)
    .then((response) => {
      if (response.user_id) {
        handleUserID(email, password, response.user_id);
      }
    })
    .then(() => {
      console.log("data");
    })
    .catch((err) => console.log(err));
};
