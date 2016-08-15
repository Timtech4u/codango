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
          <Col md={3} mdOffset={1}>
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
              <Popular />
              <Popular />
              </div>
            </div>
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
          <img src="http://res.cloudinary.com/codangofile/image/upload/c_fill,h_70,w_70/v1443782603/vqr7n59zfxyeybttleug.gif" width={60} height={60} />
          <span className="rating-icons">
            <a href="#"><i className="mdi mdi-thumb-up"></i> 20</a>
            <a href="#"><i className="mdi mdi-thumb-down"></i> 20</a>
          </span>
        </Col>
        <Col xs={7} sm={8} >
          <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor </p>
          <div className="snippet" >
            <pre className="prettyprint linenums">
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

class Popular extends Component {
  render () {
    return(
      <div className="list-group">
        <a href="#" className="list-group-item">
          <h5 className="list-group-item-heading">Posted by hassan <small><em>2&nbsp;months ago</em></small></h5>
          <p className="list-group-item-text">Learn Django - the web framework for perfectionists with deadlines</p>
        </a>
      </div>
    )
  }
}
