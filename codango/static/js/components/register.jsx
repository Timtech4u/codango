import React, { Component } from 'react';
import {
  Button,
  ControlLabel,
  Form,
  FormControl,
  FormGroup
} from 'react-bootstrap';
import request from 'superagent';

class RegisterForm extends Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleFieldChange = this.handleFieldChange.bind(this);
    this.state = {
      username: '',
      password: '',
      email: '',
      confirm_password: ''
    }
  }

  handleSubmit(event) {
    event.preventDefault();
    this.registerUser(this.state.username, this.state.email,
    this.state.password, this.state.confirm_password);
  }

  handleFieldChange(event) {
    event.preventDefault();
    let key = event.target.name;
    let value = event.target.value;
    this.setState({
      [key]: value
    });
  }

  registerUser(username, email, password, confirm_password) {
    request
      .post('/api/v1/auth/register/')
      .send({'username': username, 'password': password, 'email': email,
             'confirm_password': confirm_password })
      .end((err, result) => {
        this.setState({
          user: result.body
        });
          console.log(`response code is ${result.status}`);
          console.log(result.body);
      })
  }

  render() {
    return  (
      <Form onSubmit={this.handleSubmit}>
        <FormGroup >
          <FormControl.Feedback>
            <i className="mdi mdi-account"></i>
          </FormControl.Feedback>
          <FormControl type="text"
           placeholder="Username"
           name="username"
           onChange={this.handleFieldChange} />
        </FormGroup>
        <FormGroup >
          <FormControl.Feedback>
            <i className="mdi mdi-email-outline"></i>
          </FormControl.Feedback>
          <FormControl type="text"
          placeholder="Email"
          name="email"
          onChange={this.handleFieldChange} />
        </FormGroup>
        <FormGroup >
          <FormControl.Feedback>
            <i className="mdi mdi-lock"></i>
          </FormControl.Feedback>
          <FormControl type="password"
          placeholder="Password"
          name="password"
          onChange={this.handleFieldChange} />
        </FormGroup>
        <FormGroup >
          <FormControl.Feedback>
            <i className="mdi mdi-lock"></i>
          </FormControl.Feedback>
          <FormControl type="password"
          placeholder="Confim Password"
          name="confirm_password"
          onChange={this.handleFieldChange}/>
        </FormGroup>
        <Button type="submit" block className="login-btn">
          Sign Up
        </Button>
      </Form>
    )
  }
}

module.exports = RegisterForm
