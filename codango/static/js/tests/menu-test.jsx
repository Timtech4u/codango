import Menu from '../components/menu.jsx';
import { Link } from 'react-router';
import React from 'react';
const expect = require('expect');
import { shallow,mount,render } from 'enzyme';

describe('<Menu />', () => {
  const wrapper = shallow(<Menu />)
  it('Links to About us page', () => {
    expect(wrapper.find(Link).at(0).prop('to')).toEqual('/about')
  });

  it('Links to Contact us page', () => {
    expect(wrapper.find(Link).at(1).prop('to')).toEqual('/contact')
  });

  it('Links to Team page', () => {
    expect(wrapper.find(Link).at(2).prop('to')).toEqual('/team')
  });

});
