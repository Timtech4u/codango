import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import { FormControl, Button } from 'react-bootstrap';
import LoginForm from '../components/LoginForm.jsx';

describe('<LoginForm />', () => {
  const wrapper = shallow(<LoginForm />);
  it('contains login form', () => {
    expect(wrapper.find(FormControl).at(0).prop('name')).to.equal('username');
    expect(wrapper.find(FormControl).at(1).prop('name')).to.equal('password');
  });

 it('contains login button', () => {
    // find the html of the login button
    const html = wrapper.find(Button).at(0).html();
    expect(html.indexOf('Login')).to.not.equal(-1);
  });
});
