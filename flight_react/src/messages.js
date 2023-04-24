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
  console.log("message:", message);
  console.log("messageType:", typeof message);
  console.log("message include error: ", message.includes("error"));

  if (messageType === "success") {
    return <div className="messageContainerSuccess"> {message}</div>;
  }
  // else if (message.includes("error") && typeof message === "string") {
  //   try {
  //     console.log("options2");
  //     const errorArray = JSON.parse(message);
  //     console.log("errorArray type:", typeof errorArray);
  //     console.log(errorArray.length > 0);
  //     return (
  //       <div>
  //         {errorArray.map((error, index) => {
  //           return <Message message={error.error} index={index} />;
  //         })}
  //       </div>
  //     );
  //   } catch (e) {
  //     console.log("options2 catch");
  //     console.log("Error parsing message:", e);
  //     return <div className="messageContainerError"> {message}</div>;
  //   }
  // }
  else if (messageType === "error") {
    return <div className="messageContainerError"> {message}</div>;
  } else if (messageType === "warning") {
    return <div className="messageContainerWarning"> {message}</div>;
  }
}

export default Messages;
