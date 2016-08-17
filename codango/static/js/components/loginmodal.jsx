import React, { Component } from 'react';
import {
    Button,
    FormGroup,
    FormControl,
    Form,
    Link,
    Modal,
    Col,
    Nav,
    NavItem,
    Tab
} from 'react-bootstrap';
import LoginForm from './login.jsx';
import RegisterForm from './register.jsx'


export default class LoginModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showModal: false
    };
    this.open = this.open.bind(this);
    this.close = this.close.bind(this);
  }
  close() {
    this.setState({ showModal: false });
  }
  open() {
    this.setState({ showModal: true });
  }
  render() {
    return (
      <div>
        <Button onClick={this.open} role="login">
          {this.props.children}
        </Button>
        <Modal show={this.state.showModal} onHide={this.close} className="signin-modal">
          <Modal.Body>
            <h4 >Login with</h4>
            <div className="social-login" >
              <a href="/login/facebook/?next=/" className="btn round-btn facebook-btn" ><i className="mdi mdi-facebook"></i></a>
              <a href="/login/google-oauth2/?next=/" className="btn round-btn gplus-btn" ><i className="mdi mdi-google-plus"></i></a>
            </div>
            <p className="or-divider"><span>or</span></p>
            <Tab.Container id="login-tab" defaultActiveKey="login">
              <Tab.Content animation>
                <Tab.Pane eventKey="login">
                  <LoginForm />
                </Tab.Pane>

                <Tab.Pane eventKey="signup">
                  <RegisterForm />
                </Tab.Pane>
                <Nav >
                  <NavItem eventKey="signup"><span className="tab-nav-text">Don't have an account? </span>Sign Up</NavItem>
                  <NavItem eventKey="login"><span className="tab-nav-text">Already have an account? </span>Login</NavItem>
                </Nav>
              </Tab.Content>
            </Tab.Container>
          </Modal.Body>
        </Modal>
      </div>
    );
  }
}
