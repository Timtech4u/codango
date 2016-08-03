import ReactDOM from 'react-dom';
import React, {Component} from 'react';
import request from 'superagent';
import {
    Alert,
    Col,
    form,
    Form,
    FormGroup,
    FormControl,
    Control,
    ControlLabel,
    Checkbox,
    Button,
    Tab,
    Tabs
} from 'react-bootstrap';

class Contact extends Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleFieldChange = this.handleFieldChange.bind(this);
    this.sendMessage = this.sendMessage.bind(this);
    this.displayFlashMessage = this.displayFlashMessage.bind(this);
    this.clearTextFields = this.clearTextFields.bind(this);
    this.state = {
      name: '',
      email: '',
      subject: '',
      message: '',
      flashMessage: '',
      displayFlashMessage: 'none',
      messageType: 'success'
      }
  }

  handleFieldChange(event) {
    event.preventDefault();
    let key = event.target.name;
    let value = event.target.value;
    this.setState({
        [key]: value
    });
  }

  handleSubmit(event) {
    event.preventDefault();
    this.sendMessage(this.state.name, this.state.email,
      this.state.subject, this.state.message)
  }

  clearTextFields() {
    this.setState({name: '', email: '', subject:'', message:''});
  }

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
      <div>
        <div className="row">
          <div className="col-sm-12 col-lg-12">
              <h1 className="page-title">Contact us <small><em>We'd love to hear from you</em></small></h1>
          </div>
        </div>
        <div className="row">
          <div className="col-md-8">
            <div  className="well  well-sm">
              <Form horizontal action="post" onSubmit={this.handleSubmit} className="Contact">
                <Alert bsStyle={this.state.messageType} style={{"display": this.state.displayFlashMessage}}>
                  {this.state.flashMessage}
                </Alert>
                <FormGroup controlId="formControlsText">
                  <Col componentClass={ControlLabel} sm={2}>Name</Col>
                  <Col sm={10}>
                    <FormControl type="text" required={true} placeholder="Enter fullname" name="name" value={this.state.name} onChange={this.handleFieldChange}/>
                  </Col>
                </FormGroup>
                <FormGroup controlId="formControlsText">
                  <Col componentClass={ControlLabel} sm={2}>Email</Col>
                  <Col sm={10}>
                      <FormControl type="email" required={true} placeholder="john.doe@example.com" name="email" value={this.state.email} onChange={this.handleFieldChange}/>
                  </Col>
                </FormGroup>
                <FormGroup controlId="formControlsText">
                    <Col componentClass={ControlLabel} sm={2}>Subject</Col>
                    <Col sm={10}>
                        <FormControl type="text" placeholder="Enter message subject" name="subject" value={this.state.subject} onChange={this.handleFieldChange}/>
                    </Col>
                </FormGroup>
                <FormGroup controlId="formControlsText">
                  <Col componentClass={ControlLabel} sm={2}>Message</Col>
                  <Col sm={10}>
                      <FormControl componentClass="textarea" required={true} placeholder="Enter your message here" name="message" value={this.state.message} onChange={this.handleFieldChange}/>
                  </Col>
                </FormGroup>
                <FormGroup controlId="formControlsText">
                  <Col smOffset = {2} sm={2}>
                      <Button type="submit" id="contact" type="submit" className="btn btn-primary">Send Message</Button>
                  </Col>
                </FormGroup>
              </Form>
            </div>
          </div>
          <div className="col-md-4">
              <address>
                <strong>Codango, Inc.</strong><br />
                55 Moleye Street<br />
                Sabo, Yaba<br />
                Nigeria<br />
                0800-codango
              </address>
          </div>
        </div>
      </div>
    );
  }
};
module.exports = Contact;
