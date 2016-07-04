// Main entry point for react components
import { render } from 'react-dom';
import { browserHistory, IndexRoute, Router, Route } from 'react-router';
import React from 'react';
import Main from './components/main.jsx';
import Home from './components/home.jsx';
import Team from './components/team.jsx';
import About from './components/about.jsx';
import Contact from './components/contact.jsx';

const routes = (<Router history={browserHistory}>
                <Route path="/" component={Main}>
                    <IndexRoute component={Home} history={browserHistory}/>
                    <Route path="/team" component={Team}/>
                    <Route path="/about" component={About}/>
                    <Route path="/contact" component={Contact}/>
                </Route>
              </Router>);

render(routes, document.getElementById('react'));
