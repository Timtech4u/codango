import React, { Component } from 'react';
import { Link } from 'react-router';
import { Col, Grid, Row } from 'react-bootstrap';
import FormTabs from './formtabs.jsx';

class Home extends Component {
  render() {
    return (
      <Grid>
        <Row className="show-grid">
          <Col md={8}>
            <div className="jumbotron">
              <h1 id="index-h1">Join Our Community</h1>
              <h3 className="section-text">Codango is a social networking
                site that connects all types of developers allowing for
                sharing resources, joining various communities and pair
                programming
              </h3>
              <Link className="btn btn-primary btn-lg" to="/about">Learn more</Link>
            </div>
          </Col>
          <Col md={4}>
            <FormTabs />
          </Col>
        </Row>
      </Grid>
    );
  }
}

module.exports = Home;
