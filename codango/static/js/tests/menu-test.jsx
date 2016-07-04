import Menu from '../components/menu.jsx';
import React from 'react';
const expect = require('expect');
import { shallow,mount,render } from 'enzyme';

describe('<Menu />', () => {
  const wrapper = shallow(<Menu />)
  it('Links to About us page', () => {
    expect(wrapper.find('a[href="/about-us"]').length).toEqual(1)
  });

  it('Links to Contact us page', () => {
    expect(wrapper.find('a[href="/contact-us"]').length).toEqual(1)
  });

  it('Links to Team page', () => {
    expect(wrapper.find('a[href="/team"]').length).toEqual(1)
  });
});
