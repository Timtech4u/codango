import React, {Component} from 'react';
import {Col, Row, Media, Grid, Popover, OverlayTrigger} from 'react-bootstrap';


export default class Post extends Component {
  render(){
    return(
      <div className="feed">
        <div className="profile-img">
          <img height="70" src="http://res.cloudinary.com/codangofile/image/upload/c_fill,h_70,w_70/v1443782603/vqr7n59zfxyeybttleug.gif" width="70"/>
        </div>
        <div className="feed-content">
          <p className="poster-details">
            <a href="/link/to/user">Username</a> -
              <small><em>6 days, 23 hours ago</em></small>
          </p>
          <h1>Post content</h1>
          <div id="codango-link" className="codango-badge">
            <a href="/resource/ajax/community/untagged">Untagged</a>
          </div> <br />
          <p>
            <pre className="prettyprint linenums">print hello;</pre>
          </p>
          <div className="comments">
            <div >
              <div className="col-sm-12 action-button">
                  <div className="comments-icons btn-group">
                      <a href="/resource/28/likes" data-id="28" className="like "><span className="mdi mdi-thumb-up item">&nbsp;&nbsp;<strong>0</strong></span></a>
                      <a href="/resource/28/unlikes" data-id="28" className="unlike "><span className="mdi mdi-thumb-down item">&nbsp;&nbsp;<strong>0</strong></span></a>
                  </div>
                  <div className="commentcount"><a className=" comment-count"><span className="mdi mdi-comment item">&nbsp;&nbsp;<strong>5 Comment</strong></span></a>
                  </div>
                  <div className="share-wrapper pull-right">
                    <a className="share-resource"><span className="mdi mdi-share-variant">&nbsp;&nbsp;</span><strong> Share</strong></a>
                    <div className="share-container">
                      <div className="share-icons">
                          <a className="facebook" data-id="28" title="Facebook"><span className="mdi mdi-facebook-box">&nbsp;&nbsp;</span></a>
                          <a className="twitter" data-id="28" title="Twitter"><span className="mdi mdi-twitter-box">&nbsp;&nbsp;</span></a>
                          <a className="gplus" data-id="28" title="Google+"><span className="mdi mdi-google-plus-box">&nbsp;&nbsp;</span></a>
                      </div>
                      <div className="arrow-down"></div>
                    </div>
                  </div>
              </div>
            </div>
          </div>
        </div>
        <br/>
        <hr/>
      </div>
    )
  }
}


class PostNew extends Component {
  handleClick(event) {
      event.preventDefault()
  }
  render() {
    let share = (
      <Popover id="share" >
          <a className="facebook" data-id={4} title="Facebook"><span className="mdi mdi-facebook-box">&nbsp;&nbsp;</span></a>
          <a className="twitter" data-id={4} title="Twitter"><span className="mdi mdi-twitter-box">&nbsp;&nbsp;</span></a>
          <a className="gplus" data-id={4} title="Google+"><span className="mdi mdi-google-plus-box">&nbsp;&nbsp;</span></a>
      </Popover>
    )
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
            <OverlayTrigger trigger="focus" placement="top" overlay={share}>
              <a href="#" onClick={this.handleClick}><i className="mdi mdi-share-variant"></i>Share</a>
            </OverlayTrigger>
          </div>
        </Col>
      </Row>
    )
  }
}
