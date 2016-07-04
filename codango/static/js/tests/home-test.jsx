import React from 'react';
const expect = require('expect');
import { shallow , mount, render } from 'enzyme';
import Home from '../components/home.jsx';
import FormTabs from '../components/formtabs.jsx';
import { Grid, Row, Tabs } from 'react-bootstrap';
import { Link } from 'react-router';

describe('<Home />', () => {
  const wrapper = shallow(<Home />);
  it('contains form (authentication) tabs', () => {
    expect(wrapper.contains(<FormTabs />)).toBe(true);
  });

  it('contains one grid', () => {
    expect(wrapper.find(Grid).length).toBe(1);
  });

  it('displays join our community', () => {
    expect(wrapper.find('#index-h1').text()).toEqual('Join Our Community');
  });

  it('links to about-us', () => {
    expect(wrapper.find(Link).first().prop('to')).toEqual('/about-us')
  })
});
