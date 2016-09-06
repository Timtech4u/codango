import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import Team from '../components/team-new.jsx';
import TeamMember from '../components/team-member.jsx';
var Slider = require('react-slick');


describe('<Team />', () => {
  const wrapper = shallow(<Team />)
  it('expect Slider to be rendered tow times', () => {
    expect(wrapper.find(Slider)).to.have.length(2);
  });

  it('expect TeamMember container to be in component', () => {
    expect(wrapper.containsMatchingElement(<TeamMember />)).to.equals(true);
  });
});
