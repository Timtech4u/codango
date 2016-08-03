// Main entry point for react components
import { render } from 'react-dom';
import { browserHistory, IndexRoute, Router, Route } from 'react-router';
import React from 'react';
import Main from './main.jsx';
import Home from './home.jsx';
import About from './about.jsx';

const routes = (<Router history={browserHistory}>
                <Route path="/" component={Main}>
                    <IndexRoute component={Home} history={browserHistory}/>
                    <Route path='/about' component={About} />
                </Route>
              </Router>);

render(routes, document.getElementById('react'));
