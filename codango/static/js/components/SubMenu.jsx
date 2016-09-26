import React, { Component } from 'react';
import {
  Row,
  Col,
  FormGroup,
  Glyphicon,
  Button,
  FormControl,
  DropdownButton,
  MenuItem
} from 'react-bootstrap';
import LoginModal from "./LoginModal.jsx";

export default class SubMenu extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showLogin: false
    }
  }
  componentWillReceiveProps(props){
    this.setState({showLogin: props.showLogin})
  }
  render() {
    return (
        <Row className="submenu" >
          <Col md={2} >
            <DropdownButton title="Filter Posts" id="bg-nested-dropdown">
              <MenuItem eventKey="1">All</MenuItem>
              <MenuItem eventKey="2">Newest</MenuItem>
              <MenuItem eventKey="3">Most Rated</MenuItem>
              <MenuItem eventKey="4">Trending</MenuItem>
            </DropdownButton>
          </Col>
          <Col md={8} >
            <form >
              <FormGroup >
                <FormControl type="text" placeholder="Search"/>
                <FormControl.Feedback>
                  <Glyphicon glyph="search" />
                </FormControl.Feedback>
              </FormGroup>
            </form>
          </Col>
          <Col md={2} >
            { this.state.showLogin ? <LoginModal active="login">Login / Sigin Up </LoginModal> : null }
          </Col>
        </Row>
    )
  }
}
