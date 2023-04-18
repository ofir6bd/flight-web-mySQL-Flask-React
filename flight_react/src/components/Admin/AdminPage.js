import React from "react";

function adminPage({}) {
   function Messages(props) {
     const { message, messageType } = props;
     localStorage.removeItem("globalVarMessage");
     localStorage.removeItem("globalVarMessageType");
     if (!message) {
       return null;
     }
     if (messageType == "success") {
       return <div className="messageContainerSuccess"> {message}</div>;
     } else {
       return <div className="messageContainerError"> {message}</div>;
     }
   }
   
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
