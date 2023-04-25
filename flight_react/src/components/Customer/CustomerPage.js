import React from "react";
import Messages from "../../messages";

function customerPage({}) {
  return (
    <div>
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h1 className="mainPage"> Customer Page </h1>
    </div>
  );
}

export default customerPage;
