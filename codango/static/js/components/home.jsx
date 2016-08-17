import React, { Component } from 'react';
import Slider from './slider'
import SubMenu from './subMenu'
import Feeds from './feeds'
import { StickyContainer, Sticky } from 'react-sticky';

export default class Home extends Component {
  constructor(props){
    super(props);
    this.state = {
      showLogin: false
    }
  }
  onStickyStateChange(isSticky) {
    this.setState({ showLogin: isSticky})
  }
  render() {
    return (
      <div>
      <Slider />
        <StickyContainer>
        <Sticky onStickyStateChange={this.onStickyStateChange.bind(this)}>
          <header>
            <SubMenu showLogin={this.state.showLogin}/>
          </header>
        </Sticky>
        <Feeds />
      </StickyContainer>
      </div>
    );
  }
}
