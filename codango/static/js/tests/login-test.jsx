import LoginForm from '../components/login.jsx';
import React from 'react';
const expect = require('expect');
import { shallow,mount,render } from 'enzyme';
import { Button, FormControl, FormGroup } from 'react-bootstrap';

describe('<LoginForm />', () => {
  const wrapper = shallow(<LoginForm url="/api/v1/auth/login/"/>)
  it('contains username field', () => {
    expect(wrapper.find(FormControl).at(0).prop('name')).toEqual('username')
  });

  it('contains password field', () => {
    expect(wrapper.find(FormControl).at(1).prop('name')).toEqual('password')
  })

  it('contains login button', () => {
    const html = wrapper.find(Button).at(0).html()
    expect(html.indexOf('Login')).toNotEqual(-1)
  })

  it('contains Facebook login button', () => {
    const button = wrapper.find('a[href="/login/facebook/?next=/"]')
    expect(button.text()).toEqual('Login with Facebook')
    expect(button.props()['href']).toEqual('/login/facebook/?next=/')
  })

  it('contains Google login button', () => {
    const button = wrapper.find('a[href="/login/google-oauth2/?next=/"]')
    expect(button.text()).toEqual('Login with Google')
    expect(button.props()['href']).toEqual('/login/google-oauth2/?next=/')
  })

  it('contains forgot passsword link', () => {
    const element = wrapper.find('a[href="/recovery"]')
    expect(element.text()).toEqual('Reset')
    expect(element.props()['href']).toEqual('/recovery')
  })
})
