import {render} from 'react-dom'
import React, {Component} from 'react';
import MenuNew from './menu-new.jsx'

export default class MainNew extends Component {
  constructor() {
    super();
  }

  render() {
    return (
      <div>
        <MenuNew/> {this.props.children}
      </div>
    )
  }
}
