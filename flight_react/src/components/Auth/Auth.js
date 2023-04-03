import { checkLogin, checkAdmin } from "../../apiHandler/ApiHandler";
import React, { useState } from "react";


export function Auth(email, password) {

}

// export function Auth(email, password) {
//   const [userID, setUserID] = useState("");

//   const handleUserID = (val) => {
//     setUserID(val);
//     checkAdmin(email, password, val)
//       .then((response) => console.log(response))
//       .catch((err) => console.log(err));
//   };

//   const Authentication = (email, password) => {
//     console.log("start Auth");
//     checkLogin(email, password)
//       .then((response) => {
//         if (response.user_id) {
//           handleUserID(response.user_id);
//         }
//       })
//       .then(() => {
//         console.log("data");
//       })
//       .catch((err) => console.log(err));
//   };

//   return null;
// }
