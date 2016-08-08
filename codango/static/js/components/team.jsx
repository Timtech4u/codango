import React, {Component} from 'react';
import { Grid, Row } from 'react-bootstrap';
var Slider = require('react-slick');

export default class Team extends Component {
  render(){
      var settings = {
          dots: true,
          infinite: true,
          speed: 500,
          slidesToShow: 4,
          slidesToScroll: 1,
          autoplay: false,
          responsive: [{
              breakpoint: 1024,
              settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3,
                  infinite: true,
                  dots: true
              }
          }, {
              breakpoint: 600,
              settings: {
                  slidesToShow: 2,
                  slidesToScroll: 2
              }
          }, {
              breakpoint: 480,
              settings: {
                  slidesToShow: 1,
                  slidesToScroll: 1
              }
          }]
      };
    return(
    <Grid className="team">
      <Row className="show-grid">
        <Slider {...settings}>
          <div>
            <img src='https://avatars2.githubusercontent.com/u/12407721?v=3&s=245' />
            <div className="slide-after" >Everything goes here</div>
            <a href="#"><h3>Margaret Ochieng</h3></a>
            <p> Developer </p>
          </div>
          <div>
            <img src='https://avatars1.githubusercontent.com/u/3100850?v=3&s=245' />
            <div className="slide-after" >Everything goes here</div>
            <a href="#"><h3>Chidiebere Nnadi</h3></a>
            <p> Developer </p>
          </div>
          <div>
            <img src='https://avatars2.githubusercontent.com/u/15629602?v=3&s=245' />
            <a href="#"><h3>Stanley Ndagi</h3></a>
            <p> Developer </p>
          </div>
          <div>
            <img src='https://avatars3.githubusercontent.com/u/17270426?v=3&s=245' />
            <a href="#"><h3>Abdulwahab Abdulmalik</h3></a>
            <p> Developer </p>
          </div>
          <div>
            <img src='https://avatars2.githubusercontent.com/u/17288133?v=3&s=245' />
            <a href="#"><h3>Alex Kiura</h3></a>
            <p> Developer </p>
          </div>
          <div>
            <img src='https://avatars0.githubusercontent.com/u/18328313?v=3&s=245' />
            <a href="#"><h3>Nwuguru Sunday</h3></a>
            <p> Developer </p>
          </div>
        </Slider>
      </Row>
    </Grid>
    )
  }
}
