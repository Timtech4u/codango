import React, {Component} from 'react';
import { Grid, Row } from 'react-bootstrap';
import Features from './features.jsx';
import Contact from './contact.jsx';
import Team from './team.jsx';

export default class About extends Component {
  render() {
    return (
      <div >
        <Grid className="header" />
          <Features />
          <Team />
          <Contact />
      </div>
    )
  }
}
