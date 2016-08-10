import React, {Component} from 'react';
import {Col, Row, Media, Grid} from 'react-bootstrap';

export default class Feeds extends Component {
    render() {
        return (
          <Grid >
            <Row className="show-grid" >
              <Col md={8} >
                <Post />
                <Post />
                <Post />
                <Post />
              </Col>
              <Col md={4} >

              </Col>
            </Row>
          </Grid>
        )
    }
}


class Post extends Component {
  render() {
    return (
      <Row className="show-grid post" >
        <Col xs={3} sm={2}>
          <img src="#" width={60} height={60} />
          <span className="rating-icons">
            <a href="#"><i className="mdi mdi-thumb-up"></i> 20</a>
            <a href="#"><i className="mdi mdi-thumb-down"></i> 20</a>
          </span>
        </Col>
        <Col xs={7} sm={8} >
          <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor </p>
          <div className="snippet" >
            <pre class="prettyprint linenums">
              response = redirect('/')
              response.delete_cookie('userid')
            </pre>
          </div>
        </Col>
        <Col xs={2} >
          <div className="comment" >
            <i className="mdi mdi-comment"></i>
            <p className="comment-count">20</p>
          </div>
          <div className="share" >
            <a href="#" ><i className="mdi mdi-share-variant"></i>Share</a>
          </div>
        </Col>
      </Row>
    )
  }
}
