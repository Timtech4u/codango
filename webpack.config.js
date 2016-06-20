<<<<<<< 210f6e615a9870d6a7edec4a65c99c189b6e66c5
var path = require('path');
=======
var path = require("path");
>>>>>>> [Chore 116191131] Configure js build & test environemnt
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
module.exports = {
    context: __dirname,
    entry: [
<<<<<<< 210f6e615a9870d6a7edec4a65c99c189b6e66c5
      './codango/static/js/app.react.js'
=======
      "./codango/static/js/app.react.js"
>>>>>>> [Chore 116191131] Configure js build & test environemnt
    ],
    output: {
      path: __dirname + '/codango/static/js/build',
      filename: "bundle.js"
    },
    module: {
        loaders: [
            { test: /\.jsx?$/, loaders: ['react-hot', 'babel-loader', 'eslint-loader'], exclude: /node_modules/ }, // to transform JSX into JS
        ]
    },
    plugins: [
      new BundleTracker({filename: './webpack-stats.json'}),
    ],
    resolve: {
        modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['', '.js', '.jsx']
    },
};
