import React, { useState, useEffect } from "react";

import logo from './logo.svg';
import './App.css';

function App() {
    const [nextSelectors, setNextSelectors] = useState([])

    useEffect(() => {
        fetch("/get_next_selectors", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify([])
        }).then((res) =>
        res.json().then((data) => {
            setNextSelectors(data)
        })
        );
    }, []);

    const test = () => {
        console.log('woo')
    }

    return (
        <div className="App">
        Selectors: <br/>
        {nextSelectors.map((selector) => {
            const key = Object.keys(selector)[0]
            const values = Object.values(selector)[0]
            return (
                <>
                <label>{key}</label>
                <select key={key} onChange={test}>
                <option value={undefined}>~Select value~</option>
                {values.map((value) => (
                    <option value={value}>{value}</option>
                    ))}
                </select>
                </>
                )
        })}
        </div>
        );
}

export default App;
