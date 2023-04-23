import React from "react";

function Messages(props) {
  const { message, messageType } = props;

  console.log(message);
  localStorage.removeItem("globalVarMessage");
  localStorage.removeItem("globalVarMessageType");
  if (!message) {
    return null;
  }

  // console.log(message.map((d) => d.toString()));

  if (messageType == "success") {
    return <div className="messageContainerSuccess"> {message}</div>;
  } else if (messageType == "error") {
    return <div className="messageContainerError"> {message}</div>;
    // return (
    //   <div className="messageContainerError">
    //     {message.map((msg, index) => (
    //       <p key={index}>{msg}</p>
    //     ))}
    //   </div>
    // );
  } else if (messageType == "warning") {
    return <div className="messageContainerWarning"> {message}</div>;
  }
}

export default Messages;
