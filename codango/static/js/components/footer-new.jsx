import React, { Component } from 'react';
import {
  Grid,
  Row,
  Col,
  Form,
  FormGroup,
  FormControl,
  InputGroup,
  Button
} from 'react-bootstrap';

class Footer extends Component {
  render(){
    return(
      <div className="static-footer" >
        <Grid >
          <Row className="show-grid" >
            <Col md={4} >
              <p> Socialize with Codango </p>
              <a href="#"><i className="mdi mdi-facebook-box"></i></a>
              <a href="#"><i className="mdi mdi-github-box"></i></a>
              <a href="#"><i className="mdi mdi-twitter-box"></i></a>
              <a href="#"><i className="mdi mdi-google-plus-box"></i></a>
            </Col>
            <Col md={4} >
              <p><a href="#" >Term of use</a></p>
              <p><a href="#" >Privacy Policy</a></p>
            </Col>
            <Col md={4} >
              <p>Subscribe to our news letter</p>
              <Form >
                <FormGroup>
                  <InputGroup>
                    <FormControl type="text" />
                      <InputGroup.Button>
                        <Button type="submit" className="btn">Subscribe</Button>
                      </InputGroup.Button>
                  </InputGroup>
                </FormGroup>
              </Form>
            </Col>

          </Row>
          <Row className="reserved" >
              <p> ©2016 All Right reserved. Codango </p>
          </Row>
        </Grid>
      </div>
    )
  }
}

export default Footer;
