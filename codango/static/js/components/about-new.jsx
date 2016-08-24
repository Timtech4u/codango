import React, {Component} from 'react';
import {Grid, Row} from 'react-bootstrap';
import Features from './features.jsx';

export default class AboutNew extends Component {
  render() {
    return (
      <div>
        <Grid className="header"/>
        <Features/>
      </div>
    )
  }
}
