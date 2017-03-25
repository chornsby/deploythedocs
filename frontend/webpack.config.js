const path = require('path');

const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: ['./src/index.js'],
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist', 'static'),
    publicPath: '/static/',
  },
  devServer: {
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: ['babel-loader'],
      },
    ],
  },
  plugins: [
    new CopyWebpackPlugin([
      { from: 'index.html', to: path.resolve(__dirname, 'dist') },
      { from: 'node_modules/bootstrap/dist', to: 'bootstrap' },
    ]),
  ],
};
