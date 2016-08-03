import React, {Component} from 'react';
import { Grid, Row } from 'react-bootstrap';
import Features from './features.jsx';

export default class About extends Component {
  render() {
    return (
      <div >
        <Grid className="header" />
        <Grid className="content">
          <Features />
        </Grid>
      </div>
    )
  }
}
