import { Link } from 'react-router';
import React, {Component} from 'react';
import {Nav, Navbar, NavItem, NavDropdown, MenuItem} from 'react-bootstrap';

export default class Menu extends Component {
    render() {
        return (
            <Navbar fixedTop={true}>
                <Navbar.Header>
                  <Navbar.Brand>
                    <a href="/"><img src="../static/img/codango-logo-white.png"/></a>
                  </Navbar.Brand>
                  <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>
                 <Nav pullRight>
                    <li><Link to="/about">Features</Link></li>
                    <li><Link to="/team">Team</Link></li>
                    <li><Link to="/contact">Contact Us</Link></li>
                    <li><Link to="/login">Login</Link></li>
                  </Nav>
                </Navbar.Collapse>
              </Navbar>
        )
    }
}