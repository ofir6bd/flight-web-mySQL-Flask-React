import React from "react";
import Messages from "../../messages";

function adminPage({}) {
  return (
    <div>
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h1> Admin Page </h1>
    </div>
  );
}

export default adminPage;
