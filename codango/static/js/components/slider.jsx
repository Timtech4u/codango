import React, {Component} from 'react';
import {Carousel, Button} from 'react-bootstrap';
import LoginModal from "./loginmodal.jsx"

export default class Slider extends Component {
    render() {
        return (
            <Carousel className="slide-container">
                <Carousel.Item>
                <img width={900} height={500} alt="900x500" src="static/img/laptop.jpg"/>
                <Carousel.Caption>
                    <h3>Share</h3>
                    <p>Reach out to our awesome community</p>
                    <LoginModal type="get-stated-btn btn-lg" active="signup">
                        Start Sharing today<i className="mdi mdi-trending-neutral"></i>
                    </LoginModal>
                </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                <img width={900} height={500} alt="900x500" src="static/img/collaborate.png"/>
                <Carousel.Caption>
                    <h3>Collaborate</h3>
                    <p>Work with multiple members of your team at the same time in one code editor.</p>
                    <LoginModal type="get-stated-btn btn-lg" active="signup">
                        Get Started today<i className="mdi mdi-trending-neutral"></i>
                    </LoginModal>
                </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                <img width={900} height={500} alt="900x500" src="static/img/community.png"/>
                <Carousel.Caption>
                    <h3>Community</h3>
                    <p>Create a community and find other users with the same interest</p>
                    <LoginModal type="get-stated-btn btn-lg" active="signup">
                        Join the Community<i className="mdi mdi-trending-neutral"></i>
                    </LoginModal>
                </Carousel.Caption>
                </Carousel.Item>
            </Carousel>
        )
    }
}
