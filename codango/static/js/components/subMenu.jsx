import React, {Component} from 'react';
import {Grid, Row, Col, FormGroup, Glyphicon, Button, FormControl, DropdownButton, MenuItem} from 'react-bootstrap';

export default class SubMenu extends Component {
  render() {
    return (
        <Row className="submenu" >
          <Col md={4} >
            <DropdownButton title="Filter Post" id="bg-nested-dropdown">
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
        </Row>
    )
  }
}
