import React, { Component } from 'react';
import { Col, Row, Media, Grid, Popover, OverlayTrigger } from 'react-bootstrap';

class Feeds extends Component {
  render() {
    return (
      <Grid className="feeds">
        <Row className="show-grid" >
          <Col md={3}>
            <div className="community-list-section">
              <h3 className="section-header">Communities</h3>
              <div className="list-group" id="community">
                <a href="#" className="list-group-item active"><i className="mdi mdi-view-list"></i> All Feeds</a>
                <a href="#" className="list-group-item"><i className="mdi mdi-language-python"></i> Python</a>
                <a href="#" className="list-group-item"><i className="mdi mdi-android"></i> Android</a>
                <a href="#" className="list-group-item"><i className="mdi mdi-language-javascript"></i> Javascript</a>
              </div>
            </div>

            <div className="popular-block">
              <h3 className="section-header">Popular Resources</h3>
              <div className="list-group" id="popular">

              </div>
            </div>
          </Col>
          <Col md={8} mdOffset={1}>
          {/* Post Goes here */}
          </Col>
        </Row>
      </Grid>
    )
  }
}

export default Feeds;
