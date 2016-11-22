import { Link } from 'react-router';
import React, { Component } from 'react';
import { Nav, Navbar, NavItem, NavDropdown, MenuItem } from 'react-bootstrap';
import LoginModal from './LoginModal.jsx';

class Menu extends Component {
  render() {
    return (
      <Navbar className="static-nav">
        <Navbar.Header>
          <Navbar.Brand>
            <a href="/"><img src="../static/img/codango-logo-white.png"/></a>
          </Navbar.Brand>
          <Navbar.Toggle/>
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav pullRight>
            <li>
              <Link to="/about#features">Features</Link>
            </li>
            <li>
              <Link to="/about#team">Team</Link>
            </li>
            <li>
              <Link to="/about#contact">Contact Us</Link>
            </li>
            <li>
              <LoginModal active="login">Login / Sign Up</LoginModal>
            </li>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
  }
}

export default Menu;
