import React, {Component} from 'react';
import {Carousel} from 'react-bootstrap';

export default class Slider extends Component {
    render() {
        return (
                        <Carousel className="slide-container">
                            <Carousel.Item>
                            <img width={900} height={500} alt="900x500" src="static/img/laptop.jpg"/>
                            <Carousel.Caption>
                                <h3>Collaborate</h3>
                                <p>Work with multiple members of your team at the same time in one code editor.</p>
                            </Carousel.Caption>
                            </Carousel.Item>
                            <Carousel.Item>
                            <img width={900} height={500} alt="900x500" src="static/img/laptop.jpg"/>
                            <Carousel.Caption>
                                <h3>Second slide label</h3>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                            </Carousel.Caption>
                            </Carousel.Item>
                            <Carousel.Item>
                            <img width={900} height={500} alt="900x500" src="static/img/laptop.jpg"/>
                            <Carousel.Caption>
                                <h3>Third slide label</h3>
                                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                            </Carousel.Caption>
                            </Carousel.Item>
                        </Carousel>
        )
    }
}
