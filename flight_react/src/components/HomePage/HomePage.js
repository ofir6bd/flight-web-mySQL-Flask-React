import React from "react";
import "./HomePage.css";
import Messages from "../../messages";
import HelloSlider from "./HelloSlider";

function HomePage() {

  return (
    <div>
      <Messages
        message={localStorage.getItem("globalVarMessage")}
        messageType={localStorage.getItem("globalVarMessageType")}
      />
      <br />
      <h2> Home Page </h2>
      <h4>The best flight deals to everywhere, from anywhere</h4>
      <HelloSlider />
    </div>
  );
}

export default HomePage;
