import React, { Component } from 'react';
import {
    Button,
    Checkbox,
    FormGroup,
    FormControl,
    Form
} from 'react-bootstrap';
import request from 'superagent';
const Cookies = require('js-cookie');

export default class LoginForm extends Component {
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
        if(result.accepted){
            console.log('succesful')
        }
        console.log(result)
      });
  }
  render() {
    return(
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
            <i className="mdi mdi-lock"></i>
          </FormControl.Feedback>
          <FormControl type="password"
            placeholder="Password"
            name="password"
            onChange={this.handleFieldChange} />
        </FormGroup>
        <Checkbox>Remember me</Checkbox>
        <Button type="submit" block className="login-btn">
          Login
        </Button>
      </Form>
    )
  }
}
