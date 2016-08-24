// Main entry point for react components
import {render} from 'react-dom';
import {browserHistory, IndexRoute, Router, Route} from 'react-router';
import React from 'react';
import Main from './main.jsx';
import Home from './home.jsx';
import Team from './team.jsx';
import About from './about.jsx';
import Contact from './contact.jsx';
import MainNew from './main-new.jsx'
import HomeNew from './home-new.jsx';

const routes = (
  <Router history={browserHistory}>
    <Route path="/" component={Main}>
      <IndexRoute component={Home} history={browserHistory}/>
      <Route path="/team" component={Team}/>
      <Route path="/about" component={About}/>
      <Route path="/contact" component={Contact}/>
    </Route>
    <Route path="/new-homepage" component={MainNew}>
      <IndexRoute component={Home} history={browserHistory}/>
    </Route>
  </Router>
);

render(routes, document.getElementById('react'));
