import React from "react";

function Message(props) {
  return <div className="messageContainerError">{props.message}</div>;
}

function Messages(props) {
  const { message, messageType } = props;

  // console.log(message);
  localStorage.removeItem("globalVarMessage");
  localStorage.removeItem("globalVarMessageType");
  if (!message) {
    return null;
  }
  console.log("message", message);
  console.log("mess", message.includes("error"));
  if (messageType === "success") {
    return <div className="messageContainerSuccess"> {message}</div>;
  } else if (message.includes("error")) {
    try {
      const errorArray = JSON.parse(message);

      return (
        <div>
          {errorArray.map((error) => {
            return <Message message={error.error} />;
          })}
        </div>
      );
    } catch (e) {
      console.log("Error parsing message:", e);
      return <div className="messageContainerError"> {message}</div>;
    }
  } else if (messageType === "error") {
    return <div className="messageContainerError"> {message}</div>;
  } else if (messageType === "warning") {
    return <div className="messageContainerWarning"> {message}</div>;
  }
}

export default Messages;
