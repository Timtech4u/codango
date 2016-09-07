import React, { Component } from 'react';
import { Grid, Row } from 'react-bootstrap';
import Features from './features.jsx';
import Team from './team-new.jsx';

class AboutNew extends Component {
  render() {
    return (
      <div>
        <Grid className="header" />
        <Features />
        <Team />
      </div>
    )
  }
}

export default AboutNew;
