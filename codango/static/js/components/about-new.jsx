import React, { Component } from 'react';
import { Grid, Row } from 'react-bootstrap';
import Features from './features.jsx';
import Team from './team-new.jsx';
import Contact from './contact-new.jsx';
import Footer from './footer-new.jsx';

class AboutNew extends Component {
  render() {
    return (
      /*
        * Inline styling is here pending the time
        * the new page completes, the background
        * color on the current home page is different
        * from that of the new home page
      */
      <div style={{"background": '#fff'}}>
        <Grid className="header" />
        <Features />
        <Team />
        <Contact />
        <Footer />
      </div>
    )
  }
}

export default AboutNew;
