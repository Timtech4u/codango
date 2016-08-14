import React, { Component } from 'react';
import Slider from './slider'
import SubMenu from './subMenu'
import Feeds from './feeds'

export default class Home extends Component {
  render() {
    return (
      <div>
      <Slider />
      <SubMenu />
      <Feeds />

      </div>
    );
  }
}

