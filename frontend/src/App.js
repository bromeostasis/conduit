import React, { useState, useEffect } from "react";

import MaterialSelector from './components/MaterialSelector'
import logo from './logo.svg';
import './App.css';


function App() {
    const [ecn, setECN] = useState('')
    const [nextSelectors, setNextSelectors] = useState([])

    useEffect(() => {
        callApi([], [])
    }, []);

    const onSelectorChange = (index, value) => {
        console.log(index, value)
        let newNextSelectors = []
        if (value) {
            newNextSelectors = nextSelectors.slice(0, index + 1)
            newNextSelectors[index].selected = value
        } else { // They've selected "~Select Value~", so remove the next choice
            newNextSelectors = nextSelectors.slice(0, index)
        }

        const apiInput = newNextSelectors.map((selector) => {
            const input = {}
            input[Object.keys(selector)[0]] = selector.selected
            return input
        })

        callApi(apiInput, newNextSelectors) // TODO: newNextSelectors likely temp, useCallback should fix
    }

    const callApi = (data, newNextSelectors) => { // TODO: setting data should happen in caller. Use usecallback.
        fetch("/get_next_selectors", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        }).then((res) =>
            res.json().then((data) => {
                if (data['Extended Construction Numbers']) {
                    setECN(data['Extended Construction Numbers'])
                } else {
                    setECN('')
                    setNextSelectors(newNextSelectors.concat(data))
                }
            })
        );
    }

    const selectors = []
    for (let i = 0; i < nextSelectors.length; i++) {
        selectors.push(<MaterialSelector index={i} selectorData={nextSelectors[i]} onChange={onSelectorChange} withArrow={i < nextSelectors.length - 1} />)
    }

    return (
        <div className="App">
        Selectors: <br/>
        {selectors}
        {ecn && (
            <p>
                Extended Construction Numbers: {ecn}
            </p>
        )}
        </div>
    );
}

export default App;
