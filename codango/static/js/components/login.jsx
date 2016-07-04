import React, { Component } from 'react';
import {
    Button,
    Checkbox,
    ControlLabel,
    form,
    FormGroup,
    FormControl,
} from 'react-bootstrap';
import request from 'superagent';
const Cookies = require('js-cookie');

class LoginForm extends Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleFieldChange = this.handleFieldChange.bind(this);
    this.state = {
      username: '',
      password: '',
      token: '',
    };
  }

  handleSubmit(event) {
    event.preventDefault();
    this.loginUser(this.state.username, this.state.password);
  }

  handleFieldChange(event) {
    event.preventDefault();
    const key = event.target.name;
    const value = event.target.value;
    this.setState({
      [key]: value,
    });
  }

  loginUser(username, password) {
    request
      .post('/login')
      .type('form')
      .set('X-CSRFToken', Cookies.get('csrftoken'))
      .send({ username, password })
      .end((err, result) => {
        window.location.href = '/home';
      });
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <FormGroup controlId="formControlsText">
          <ControlLabel>Username</ControlLabel>
          <FormControl type="text"
            placeholder="Username"
            name="username"
            onChange={this.handleFieldChange}
          />
        </FormGroup>
        <FormGroup controlId="formControlsPassword" >
          <ControlLabel>Password</ControlLabel>
          <FormControl
            type="password"
            placeholder="Password"
            name="password"
            onChange={this.handleFieldChange}
          />
        </FormGroup>
        <Checkbox>Remember me </Checkbox>
        <FormGroup>
          <Button type="submit" className="btn btn-primary">Login</Button>
        </FormGroup>
        <FormGroup>
          <a href="/login/facebook/?next=/" className="btn btn-primary">
            Login with Facebook
          </a>
          {' '}
          <a href="/login/google-oauth2/?next=/" className="btn btn-danger">
            Login with Google
          </a>
        </FormGroup>
        <p>Forgot password? <a href="/recovery">Reset</a></p>
      </form>
    );
  }
}

module.exports = LoginForm;
