import React, {Component} from 'react';
import {Media} from 'react-bootstrap';

export default class Menu extends Component {
    render() {
        return (
            <div className="row">
                <div className="col-md-8">
                    <div className="col-md-11 resource">
                        <Media>
                         <Media.Left>
                            <img width={64} height={64} src="/assets/thumbnail.png" className="img-circle"/>
                            <hr/>
                            <p>
                                left
                            </p>
                          </Media.Left>
                          <Media.Body>
                            <Media.Heading>Media Heading</Media.Heading>
                            <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                          </Media.Body>
                        </Media>
                    </div>
                    <div className="col-md-11 resource">
                        <Media>
                         <Media.Left>
                            <img width={64} height={64} src="/assets/thumbnail.png" className="img-circle"/>
                          </Media.Left>
                          <Media.Body>
                            <Media.Heading>Media Heading</Media.Heading>
                            <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                          </Media.Body>
                        </Media>
                    </div>
                </div>
                <div className="col-md-4">
                    hed
                </div>
            </div>

        )
    }
}
module.exports = Menu;
