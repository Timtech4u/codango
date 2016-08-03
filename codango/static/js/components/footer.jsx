import React, {Component} from 'react';
import { Grid, Row, Col, Form, FormGroup, FormControl, InputGroup, Button} from 'react-bootstrap';

export default class Footer extends Component {
  render(){
    return(
      <Grid className="static-footer">
        <Row className="show-grid" >
          <Col md={4} >
            <p> Socialize with Codango </p>
            <span></span>
          </Col>
          <Col md={4} >
            <p><a href="#" >Term of use</a></p>
            <p><a href="#" >Privacy Policy</a></p>
          </Col>
          <Col md={4} >
            <p>Subscribe to Our news letter</p>
            <Form >
              <FormGroup>
                <InputGroup>
                  <FormControl type="text" />
                    <InputGroup.Button>
                      <Button>Subscribe</Button>
                    </InputGroup.Button>
                </InputGroup>
              </FormGroup>
            </Form>
          </Col>
        </Row>
      </Grid>
    )
  }
}
