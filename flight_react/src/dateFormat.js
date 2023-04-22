import React from "react";

function DateFormat(time) {
  var month = time.$M + 1;
  var hours = time.$H.toString();
  if (hours.length < 2) {
    hours = "0" + time.$H.toString();
  }
  var minutes = time.$m.toString();
  if (minutes.length < 2) {
    minutes = "0" + time.$m.toString();
  }
  var result =
    time.$y.toString() +
    "-" +
    month.toString() +
    "-" +
    time.$D.toString() +
    "T" +
    hours +
    ":" +
    minutes;
  return result;
}

export default DateFormat;
