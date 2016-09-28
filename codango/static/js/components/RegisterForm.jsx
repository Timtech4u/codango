import React, { Component } from 'react';
import {
  Button,
  ControlLabel,
  Form,
  FormControl,
  FormGroup,
  Alert
} from 'react-bootstrap';
import request from 'superagent';

class RegisterForm extends Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleFieldChange = this.handleFieldChange.bind(this);
    this.registerUser = this.registerUser.bind(this);
    this.state = {
      username: '',
      password: '',
      email: '',
      confirm_password: '',
      message: '',
      messageType: ''
    };
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
        if(err || !result.ok){
          let errorMessage = 'Error occured';
          if(result.body.username){
            errorMessage = result.body.username[0];
          } else if(result.body[0]) {
              errorMessage = result.body[0];
          }
          this.setState({
            message: errorMessage,
            messageType: 'danger',
            password: '',
            confirm_password: '',
          });
        } else {
            this.setState({
              message: 'Sign Up Successful. You can now Login',
              messageType: 'success',
              username: '',
              password: '',
              email: '',
              confirm_password: '',
            });
        }
      });
  }

  render() {
    return  (
      <Form onSubmit={this.handleSubmit}>
        {this.state.message ?
          <Alert bsStyle={this.state.messageType}>
           {this.state.message}
          </Alert> : null
        }
        <FormGroup >
          <FormControl.Feedback>
            <i className="mdi mdi-account"></i>
          </FormControl.Feedback>
          <FormControl type="text"
                       placeholder="Username"
                       name="username"
                       value={this.state.username}
                       onChange={this.handleFieldChange}
          />
        </FormGroup>
        <FormGroup >
          <FormControl.Feedback>
            <i className="mdi mdi-email-outline"></i>
          </FormControl.Feedback>
          <FormControl type="text"
                       placeholder="Email"
                       name="email"
                       value={this.state.email}
                       onChange={this.handleFieldChange}
          />
        </FormGroup>
        <FormGroup >
          <FormControl.Feedback>
            <i className="mdi mdi-lock"></i>
          </FormControl.Feedback>
          <FormControl type="password"
                       placeholder="Password"
                       name="password"
                       value={this.state.password}
                       onChange={this.handleFieldChange}
          />
        </FormGroup>
        <FormGroup >
          <FormControl.Feedback>
            <i className="mdi mdi-lock"></i>
          </FormControl.Feedback>
          <FormControl type="password"
                       placeholder="Confim Password"
                       name="confirm_password"
                       value={this.state.confirm_password}
                       onChange={this.handleFieldChange}
          />
        </FormGroup>
        <Button type="submit" block className="login-btn">
          Sign Up
        </Button>
      </Form>
    );
  }
}

export default RegisterForm;
