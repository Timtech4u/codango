import RegisterForm from '../components/register.jsx';
import React from 'react';
const expect = require('expect');
import { shallow,mount,render } from 'enzyme';
import { Button, FormControl, FormGroup } from 'react-bootstrap';

describe('<RegisterForm />', () => {
  const wrapper = shallow(<RegisterForm />)
  it('contains username field', () => {
    expect(wrapper.find(FormControl).at(0).prop('name')).toEqual('username')
  });

  it('contains email field', () => {
    expect(wrapper.find(FormControl).at(1).prop('name')).toEqual('email')
  });

  it('contains password field', () => {
    expect(wrapper.find(FormControl).at(2).prop('name')).toEqual('password')
  });

  it('contains confirm password field', () => {
    expect(wrapper.find(FormControl).at(3).prop('name')).toEqual('confirm_password')
  });

  it('contains Register button', () => {
    const html = wrapper.find(Button).at(0).html()
    expect(html.indexOf('Sign Up')).toNotEqual(-1)
  })
});
