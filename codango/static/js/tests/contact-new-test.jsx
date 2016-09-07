import React from 'react';
import { expect } from 'chai';
import { shallow } from 'enzyme';
import { FormControl } from 'react-bootstrap';
import Contact from '../components/contact-new.jsx';

describe('<Contact />', () => {
  const wrapper = shallow(<Contact />);
  it('contains Get In touch message', () => {
    expect(wrapper.contains(<h3>Get In Touch</h3>)).to.equal(true);
  });

  it('contains name field', () => {
    expect(wrapper.find(FormControl).at(0).prop('name')).to.equal('name');
  });

  it('contains email field', () => {
    expect(wrapper.find(FormControl).at(1).prop('name')).to.equal('email');
  });

  it('contains subject field', () => {
    expect(wrapper.find(FormControl).at(2).prop('name')).to.equal('subject');
  });

  it('contains message field', () => {
    expect(wrapper.find(FormControl).at(3).prop('name')).to.equal('message');
  });
});
