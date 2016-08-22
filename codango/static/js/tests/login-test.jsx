import React from 'react';
const expect = require('expect');
import { mount } from 'enzyme';
import { FormControl, Button } from 'react-bootstrap';
import Login from '../components/login.jsx';

describe('<Login />', () => {
  const wrapper = mount(<Login />);
  it('contains username field', () => {
    expect(wrapper.find(FormControl).at(0).prop('name')).toEqual('username')
  });

  it('contains password field', () => {
    expect(wrapper.find(FormControl).at(1).prop('name')).toEqual('password')
  });

  it('contains login button', () => {
    const html = wrapper.find(Button).at(0).html()
    expect(html.indexOf('Login')).toNotEqual(-1)
  });
});
