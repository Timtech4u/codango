// Main entry point for react components
import {render} from 'react-dom';
import {browserHistory, IndexRoute, Router, Route} from 'react-router';
import React from 'react';
import Main from './main.jsx';
import Home from './home.jsx';
import Team from './team.jsx';
import About from './about.jsx';
import Contact from './contact.jsx';


function hashLinkScroll() {
  const {hash} = window.location;
  if (hash !== '') {
    // Push onto callback queue so it runs after the DOM is updated, this is
    // required when navigating from a different page so that the element is
    // rendered on the page before trying to getElementById.
    setTimeout(() => {
      const id = hash.replace('#', '');
      history.pushState("", document.title, window.location.pathname +
                                            window.location.search);
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView();
      }
    }, 0);
  }
}

const routes = (
  <Router history={browserHistory} onUpdate={hashLinkScroll}>
    <Route path="/" component={Main}>
      <IndexRoute component={Home} history={browserHistory}/>
      <Route path="/team" component={Team}/>
      <Route path="/about" component={About}/>
      <Route path="/contact" component={Contact}/>
    </Route>
  </Router>
);

render(routes, document.getElementById('react'));
