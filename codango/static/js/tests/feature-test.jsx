import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import Features from '../components/features.jsx';
import { Col } from 'react-bootstrap';

describe('<Features />', () => {
  const wrapper = shallow(<Features />);

  it('expect Col to be rendered three times', () => {
    expect(wrapper.find(Col)).to.have.length(3);
  });

  it('render three flaticon element', () => {
    expect(wrapper.find('.flaticon')).to.have.length(3);
  });

  it('contains the Community heading', () => {
    expect(wrapper.contains(<h4>Community</h4>)).to.equal(true);
  });

  it('contains the Share Resource heading', () => {
    expect(wrapper.contains(<h4>Share Resource</h4>)).to.equal(true);
  });

  it('contains the pair programming heading', () => {
    expect(wrapper.contains(<h4>Pair Programming</h4>)).to.equal(true);
  });

  it('contains three paragraph tags', () => {
    expect(wrapper.find('p')).to.have.length(3);
  });
});
