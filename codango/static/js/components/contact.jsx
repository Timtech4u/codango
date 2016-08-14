import React, {Component} from 'react';
import request from 'superagent';
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

  displayFlashMessage(message, messageType) {
    this.setState({messageType: messageType,
                    flashMessage: message,
                    displayFlashMessage: "block",
                  });
    setTimeout(function(){
      this.setState({flashMessage: "",
                      displayFlashMessage: "none"});
    }.bind(this), 3000);
  }

  sendMessage(name, email, subject, message) {
    request
      .post('/api/v1/contact/')
      .type('form')
      .send({'name': name, 'email': email, 'subject': subject,
             'message': message })
      .end((err, result) => {
        if (err) {
          return this.displayFlashMessage("An error occured. Ensure you supply a valid email", "danger")
        }
        else {
          if (result.status === 201) {
            this.clearTextFields()
            return this.displayFlashMessage("Your message has been successfully sent", "success")
          }
          return this.displayFlashMessage("Message not sent", "danger")
        }
      });
  }
  render() {
    return (
      <Grid id="contact">
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
