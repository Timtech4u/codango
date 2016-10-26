import { Link } from 'react-router';
import React, { Component } from 'react';
import { Nav, Navbar, NavItem, NavDropdown, MenuItem } from 'react-bootstrap';
import LoginModal from './LoginModal.jsx';

class MenuNew extends Component {
  componentWillUpdate() {
    alert('Jam session');
  }

  handleScroll(event) {
    alert('Jam sth');
  }

  render() {
    return (
      <Navbar className="static-nav" onScroll={this.handleScroll.bind(this)}>
        <Navbar.Header>
          <Navbar.Brand>
            <a href="/"><img src="../static/img/codango-logo-white.png"/></a>
          </Navbar.Brand>
          <Navbar.Toggle/>
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav pullRight>
            <li>
              <Link to="/about-new#features">Features</Link>
            </li>
            <li>
              <Link to="/about-new#team">Team</Link>
            </li>
            <li>
              <Link to="/about-new#contact">Contact Us</Link>
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

export default MenuNew;
