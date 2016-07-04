// Main entry point for react components
import React from 'react';
import { render } from 'react-dom';
import { Router, Route, browserHistory, IndexRoute } from 'react-router';
import Home from './components/home.jsx';
import Main from './components/main.jsx';


const routes = (<Router history={browserHistory}>
                <Route path="/" component={Main}>
                    <IndexRoute component={Home} history={browserHistory}/>
                </Route>
              </Router>);

render(routes, document.getElementById('react'));
