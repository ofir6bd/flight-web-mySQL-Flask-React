import React from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
import "./login.css";

function Login() {

    
  return (
    <div className="container">
      <h2> Sign In Page</h2>
      <TextField id="outlined-basic" label="Email:" variant="outlined" />
      <TextField id="outlined-basic" label="Password:" variant="outlined" />
      <Button> Log In</Button>
    </div>
  );
}

export default Login;
