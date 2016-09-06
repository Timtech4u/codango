import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import TeamMember from '../components/team-member.jsx';

describe('<TeamMember />', () => {
  const props = {
    name: 'Abdulwahab Abdulmalik',
    position: 'Developer',
    imgSrc: 'https://avatars3.githubusercontent.com/u/17270426?v=3&s=245',
    twitter: 'https://twitter.com/',
    github: 'https://github.com/andela-aabdulwahab',
    linkedin: '#'
  };
  const wrapper = shallow(<TeamMember {...props}/>);

  it("renders image component", () => {
    expect(wrapper.find('img')).to.have.length(1);
  });

  it("renders social icons", () => {
    expect(wrapper.find('.mdi')).to.have.length(3);
  });

  it("pass props to the component", () => {
    expect(wrapper.props().imgSrc).to.be.defined;
    expect(wrapper.props().linkedin).to.be.defined;
    expect(wrapper.props().name).to.be.defined;
    expect(wrapper.props().position).to.be.defined;
    expect(wrapper.props().twiter).to.be.defined;
    expect(wrapper.props().github).to.be.defined;
  });

  it("render name passed as props", () => {
    expect(wrapper.contains(<h3>Abdulwahab Abdulmalik</h3>)).to.equals(true);
  });

  it("render position passed as props in h3 tag", () => {
    expect(wrapper.contains(<p>Developer</p>)).to.equals(true);
  });

});
