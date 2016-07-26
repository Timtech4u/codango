import React, {Component} from 'react';
import {Carousel} from 'react-bootstrap';

export default class Slider extends Component {
    render() {
        return (
            <div className="row">
                <div className="slide-container">
                    <div className="slide-content">
                        <Carousel>
                            <Carousel.Item>
                            <Carousel.Caption>
                                <h3>First slide label</h3>
                                <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                            </Carousel.Caption>
                            </Carousel.Item>
                            <Carousel.Item>
                            <Carousel.Caption>
                                <h3>Second slide label</h3>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                            </Carousel.Caption>
                            </Carousel.Item>
                            <Carousel.Item>
                            <Carousel.Caption>
                                <h3>Third slide label</h3>
                                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                            </Carousel.Caption>
                            </Carousel.Item>
                        </Carousel>
                    </div>
                </div>
            </div>
        )
    }
}
