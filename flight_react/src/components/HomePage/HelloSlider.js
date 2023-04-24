import React from "react";
import airplane1 from "../../images/airplane1.PNG";
import airplane2 from "../../images/airplane2.PNG";
import airplane3 from "../../images/airplane3.PNG";
import airplane4 from "../../images/airplane4.PNG";
import { Carousel } from "react-bootstrap";

// this Component is used for the carousel in the main page
const HelloSlider = () => {
  return (
    <>
      <Carousel fade>
        <Carousel.Item>
          <img
            className="d-block w-100 slideImages"
            src={airplane2}
            alt="First slide"
          />
          <Carousel.Caption>
            <h2>Book your flight early for the best deals</h2>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100 slideImages"
            src={airplane1}
            alt="Second slide"
          />
          <Carousel.Caption>
            <h2>Compare prices and airlines before booking</h2>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100 slideImages"
            src={airplane3}
            alt="Third slide"
          />
          <Carousel.Caption>
            <h2>Book a flexible ticket in case your plans change</h2>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100 slideImages"
            src={airplane4}
            alt="forth slide"
          />
          <Carousel.Caption>
            <h2>Double-check your flight details before departure</h2>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    </>
  );
};

export default HelloSlider;
