import React from 'react';
const expect = require('expect');
import {mount} from 'enzyme';
import Features from '../components/features.jsx';

describe('<Features />', () => {
  const wrapper = mount(<Features />);
  it('contains community explanation', () => {
    expect(wrapper.text()).toContain('Community');
  });

  it('contains Share Resource explanation', () => {
    expect(wrapper.text()).toContain('Share Resource');
  });

  it('contains Pair Programming explanation', () => {
    expect(wrapper.text()).toContain('Pair Programming');
  });
});
