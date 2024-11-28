const path = require("path");

module.exports = {
  entry: "./src/index.js",  // Adjust to your entry point
  output: {
    path: path.resolve(__dirname, "static/js"),
    filename: "bundle.js",
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-react"],
          },
        },
      },
    ],
  },
};
