import React, {Component} from 'react';
import { Row, Col } from 'react-bootstrap';

export default class Features extends Component {
  render() {
    return (
      <Row className="show-grid" >
        <Col md={4} >
          <h4 >
            Community
          </h4>
          <p >
            Codango is an ever expanding community of vibrant developers from different stacks and levels, helping each other grow to be even stronger developers.
          </p>
        </Col>
        <Col md={4} >
          <h4 >
            Share Resource
          </h4>
          <p >
            Codango provides a platform for developers from various stacks to upload PDFs, DOCS, code snippets and knowledgable updates making them available for all to learn and use.
          </p>
        </Col>
        <Col md={4} >
          <h4 >
            Pair Programming
          </h4>
          <p >
            Codango provides a platform where developers can act as mentors to other developers in real time and help grow a community of stronger developers.
          </p>
        </Col>
      </Row>
    )
  }
}
