import React from 'react';
const expect = require('expect');
import { mount } from 'enzyme';
import { Form } from 'react-bootstrap';
import Footer from '../components/footer-new.jsx';

describe('<Footer-new />', () => {
  const wrapper = mount(<Footer />);
  it('contains socialize message', () => {
    expect(wrapper.text()).toContain('Socialize with Codango');
  });
  it('contains term of use', () => {
    expect(wrapper.text()).toContain('Term of use');
  })
  it('has subscribe form', () => {
    expect(wrapper.find(Form).length).toBe(1);
  })
});
