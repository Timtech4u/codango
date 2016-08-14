// Main entry point for react components
import { render } from 'react-dom';
import { browserHistory, IndexRoute, Router, Route } from 'react-router';
import React from 'react';
import Main from './main.jsx';
import Home from './home.jsx';
import About from './about.jsx';

function hashLinkScroll() {
  const { hash } = window.location;
  if (hash !== '') {
    // Push onto callback queue so it runs after the DOM is updated,
    // this is required when navigating from a different page so that
    // the element is rendered on the page before trying to getElementById.
    setTimeout(() => {
      const id = hash.replace('#', '');
      const element = document.getElementById(id);
      if (element) element.scrollIntoView();
    }, 0);
  }
}

const routes = (<Route path="/" component={Main}>
                    <IndexRoute component={Home} history={browserHistory}/>
                    <Route path='/about' component={About} />
                </Route>
               );

render(
  <Router
    history={browserHistory}
    routes={routes}
    onUpdate={hashLinkScroll}
    />,
    document.getElementById('react')
);
