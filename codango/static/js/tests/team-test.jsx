import React from 'react';
const expect = require('expect');
import { shallow, mount } from 'enzyme';
import Team, { TeamMember } from '../components/team.jsx';

/*
describe('<TeamMember />', () => {
  let member = {
      name: 'Abdulwahab Abdulmalik',
      position: 'Developer',
      imgSrc: 'https://avatars3.githubusercontent.com/u/17270426?v=3&s=245',
      twitter: '#',
      github: 'https://github.com/andela-aabdulwahab',
      linkedin: '#'
  }
  const wrapper = shallow(<TeamMember />);
  it('contains image container', () => {
    expect(wrapper.find('.team-img-container')).to.have.length(1);
  });

  it('contains container for social icons', () => {
    expect(wrapper.find('.team-social-container')).to.have.length(1);
  });

  it('name props rendered', () => {
    expect(wrapper.text()).toContain('Abdulwahab Abdulmalik');
  });

  it('position props rendered', () => {
    expect(wrapper.text()).toContain('Developer');
  });
});

*/
