import React, {Component} from 'react';
import {Navbar, FormGroup, FormControl} from 'react-bootstrap';

export default class Menu extends Component {
    render() {
        return (
            <Navbar className="search-bar">
             <form className="search-form">
                 <div className="col-md-6">
                     <div className="form-group">
                        <input type="text" className="form-control search-field h50" placeholder="Search" />
                        <span className="glyphicon glyphicon-search"></span>
                      </div>
                 </div>
                 <div className="col-md-6">
                   <FormGroup controlId="formControlsSelect">
                      <FormControl componentClass="select" placeholder="Filter"  className="h50">
                        <option value="select">All filters</option>
                        <option value="">Newest</option>
                        <option value="">Oldest</option>
                        <option value="">Most Engaging</option>
                        <option value="">Highest Rated</option>
                      </FormControl>
                    </FormGroup>
                 </div>
            </form>
          </Navbar>

        )
    }
}
module.exports = Menu;
