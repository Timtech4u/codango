import React, {Component} from 'react';
import Slider from './slider.jsx';
import { StickyContainer, Sticky } from 'react-sticky';
import SubMenu from './SubMenu.jsx';
import Features from './features.jsx';

export default class HomeNew extends Component {
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
      <div style={{"background": '#fff'}}>
        <Slider/>
          <StickyContainer>
            <Sticky onStickyStateChange={this.onStickyStateChange.bind(this)}>
              <header>
                <SubMenu showLogin={this.state.showLogin}/>
              </header>
            </Sticky>
          </StickyContainer>
      </div>
    );
  }
}
