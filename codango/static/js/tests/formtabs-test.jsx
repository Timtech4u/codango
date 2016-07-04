import React from 'react';
const expect = require('expect');
import { shallow,mount,render } from 'enzyme';
import FormTabs from '../components/formtabs.jsx';
import LoginForm from '../components/login.jsx';
import RegisterForm from '../components/register.jsx';

describe('<FormTabs', () => {
  it('contains auth forms', () => {
    const wrapper = shallow(<FormTabs />);
    expect(wrapper.contains(<LoginForm url="/api/v1/auth/login/"/>)).toBe(true);
  });

  it('contains Register Form', () => {
    const wrapper = shallow(<FormTabs />);
    expect(wrapper.contains(<RegisterForm />)).toBe(true);
  });
});
