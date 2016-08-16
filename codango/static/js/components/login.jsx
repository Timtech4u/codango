import React, { Component } from 'react';
import {
    Button,
    Checkbox,
    ControlLabel,
    form,
    FormGroup,
    FormControl,
    Form,
    Link,
    Modal,
    Col
} from 'react-bootstrap';


export default class Login extends Component {
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
      <Button bsStyle="primary" onClick={this.open}>
        Login / Sign Up
      </Button>
        <Modal show={this.state.showModal} onHide={this.close} className="signin-modal">
          <Modal.Body>
            <h4 >Login with</h4>
            <div className="social-login" >
              <Button className="round-btn facebook-btn" ><i className="mdi mdi-facebook"></i></Button>
              <Button className="round-btn gplus-btn" ><i className="mdi mdi-google-plus"></i></Button>
            </div>
            <p className="or-divider"><span>or</span></p>
            <Form >
              <FormGroup >
                <FormControl.Feedback>
                  <i className="mdi mdi-account"></i>
                </FormControl.Feedback>
                <FormControl type="text" placeholder="Username" />
              </FormGroup>
              <FormGroup >
                <FormControl.Feedback>
                  <i className="mdi mdi-lock"></i>
                </FormControl.Feedback>
                <FormControl type="password" placeholder="Password" />
              </FormGroup>
              <Checkbox>Remember me</Checkbox>
              <Button type="submit" block className="login-btn">
                Login
              </Button>
            </Form>
            <p className="account-message" >Don't have an account? <a href="#">Sign Up</a></p>  
          </Modal.Body>
        </Modal>
      </div>
    );
  }
}
