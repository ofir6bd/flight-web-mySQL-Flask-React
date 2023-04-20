import React from "react";
import Messages from "../../messages";

function airlinePage({  }) {
  return (
    <div>
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <h1> Airline Page </h1>
    </div>
  );
}

export default airlinePage;
