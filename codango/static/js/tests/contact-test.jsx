import React from 'react';
const expect = require('expect');
import { mount } from 'enzyme';
import { FormControl } from 'react-bootstrap';
import Contact from '../components/contact.jsx';

describe('<Contact />', () => {
  const wrapper = mount(<Contact />);
  it('contains Get In touch message', () => {
    expect(wrapper.text()).toContain('Get In Touch');
  });

  it('contains name field', () => {
    expect(wrapper.find(FormControl).at(0).prop('name')).toEqual('name')
  });

  it('contains email field', () => {
    expect(wrapper.find(FormControl).at(1).prop('name')).toEqual('email')
  });

  it('contains subject field', () => {
    expect(wrapper.find(FormControl).at(2).prop('name')).toEqual('subject')
  });

  it('contains message field', () => {
    expect(wrapper.find(FormControl).at(3).prop('name')).toEqual('message')
  });
});
