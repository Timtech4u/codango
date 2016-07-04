// tests.webpack.js
var context = require.context('./codango/static/js', true, /-test\.jsx$/);
context.keys().forEach(context);
