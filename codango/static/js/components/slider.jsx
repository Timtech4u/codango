import React, {Component, PropTypes} from 'react';
import {Carousel, Button} from 'react-bootstrap';

export default class Slider extends Component {
  render() {
    let carouselCaptions = [
      {
        key: 1,
        title: "Share",
        imageSrc: "static/img/laptop.jpg",
        caption: "Reach out to our awesome community",
        buttonText: "Start Sharing today"
      }, {
        key: 2,
        title: "Collaborate",
        imageSrc: "static/img/collaborate.png",
        caption: "Work with multiple members of your team at the same time in one code editor",
        buttonText: "Get Started today"
      }, {
        key: 3,
        title: "Community",
        imageSrc: "static/img/community.png",
        caption: "Create a community and find other users with the same interest",
        buttonText: "Join the Community"
      }
    ]
    return (
      <Carousel className="slide-container">
        {carouselCaptions.map((captions) => {
          return (
            <Carousel.Item>
              <img width={900} height={500} alt="900x500" src={captions.imageSrc}/>
              <Carousel.Caption>
                <h3>{captions.title}</h3>
                <p>{captions.caption}</p>
                <Button className="get-stated-btn btn-lg">
                  {captions.buttonText}<i className="mdi mdi-trending-neutral"></i>
                </Button>
              </Carousel.Caption>
            </Carousel.Item>
          )
        })}
      </Carousel>
    )
  }
}
