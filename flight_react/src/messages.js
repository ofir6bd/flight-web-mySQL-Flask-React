import React from "react";

// function Message(props) {
//   return <div className="messageContainerError">{props.message}</div>;
// }

function Messages(props) {
  const { message, messageType } = props;

  localStorage.removeItem("globalVarMessage");
  localStorage.removeItem("globalVarMessageType");
  if (!message) {
    return null;
  }

  if (messageType === "success") {
    return <div className="messageContainerSuccess"> {message}</div>;
  } else if (message.includes("error") && typeof message === "string") {
    try {
      const errorArray = JSON.parse(message);
      if (errorArray.length) {
        return (
          <div className="messageContainerError"> {errorArray[0].error}</div>
        );
      }
      return <div className="messageContainerError"> {errorArray.error}</div>;
    } catch (e) {
      return <div className="messageContainerError"> {message}</div>;
    }
  } else if (messageType === "error") {
    return <div className="messageContainerError"> {message}</div>;
  } else if (messageType === "warning") {
    return <div className="messageContainerWarning"> {message}</div>;
  }
}

export default Messages;
