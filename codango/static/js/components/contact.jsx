import React, {Component} from 'react';

import {
  Grid,
  Row,
  Col,
  Form,
  FormGroup,
  FormControl,
  Button,
} from 'react-bootstrap';

export default class Contact extends Component {

  render() {
    return (
      <Grid >
        <Row className="show-grid contact" >
          <Form action="post" onSubmit={this.handleSubmit} className="Contact">
            <Col md={12} >
                <h3> Get In Touch </h3>
            </Col>
            <Col md={6}>
              <FormControl type="text" placeholder="Name" name="name" required={true} onChange={this.handleFieldChange}/>
            </Col>
            <Col md={6}>
              <FormControl type="text" placeholder="Email" name="email" required={true} onChange={this.handleFieldChange}/>
            </Col>
            <Col md={12}>
              <FormControl type="text" placeholder="Subject" name="subject" onChange={this.handleFieldChange}/>
            </Col>
            <Col md={12} >
              <FormControl componentClass="textarea" required={true} placeholder="Message" name="message" onChange={this.handleFieldChange}/>
            </Col>
            <Col mdOffset={4} md={4}>
              <Button type="submit" id="contact" type="submit" className="btn">Send Message</Button>
            </Col>
          </Form>
        </Row>
      </Grid>
    )
  }
}
