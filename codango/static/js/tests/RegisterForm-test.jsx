
import RegisterForm from '../components/RegisterForm.jsx';
import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import { Button, FormControl, FormGroup } from 'react-bootstrap';

describe('<RegisterForm />', () => {
  const wrapper = shallow(<RegisterForm />);
  it('contains register form', () => {
    expect(wrapper.find(FormControl).at(0).prop('name')).to.equal('username');
    expect(wrapper.find(FormControl).at(1).prop('name')).to.equal('email');
    expect(wrapper.find(FormControl).at(2).prop('name')).to.equal('password');
    expect(wrapper.find(FormControl).at(3).prop('name')).to.equal('confirm_password');
  });

  it('contains Register button', () => {
    const html = wrapper.find(Button).at(0).html();
    expect(html.indexOf('Sign Up')).to.not.equal(-1);
  });
});
