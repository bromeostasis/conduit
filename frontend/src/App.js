import React, { useState, useEffect } from "react";

import logo from './logo.svg';
import './App.css';

function App() {

  const [data, setData] = useState({
      string: 0,
      date: "",
  });

  // Using useEffect for single rendering
  useEffect(() => {
      // Using fetch to fetch the api from 
      // flask server it will be redirected to proxy
      fetch("/data").then((res) =>
          res.json().then((data) => {
              // Setting a data from api
              setData({
                  string: data[0].String,
                  date: data[0].Date,
              });
          })
      );
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React

          Values: {data.string}, {data.date}
        </a>
      </header>
    </div>
  );
}

export default App;
