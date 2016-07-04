import React, { Component } from 'react';
import { Tab, Tabs } from 'react-bootstrap';
import LoginForm from './login.jsx';
import RegisterForm from './register.jsx';

export default class FormTabs extends Component {
  render() {
    return (
      <Tabs defaultActiveKey={1} id="authentication-forms">
        <Tab eventKey={1} title="Login">
          <LoginForm url="/api/v1/auth/login/"/>
        </Tab>
        <Tab eventKey={2} title="Register">
          <RegisterForm />
        </Tab>
      </Tabs>
    );
  }
}
