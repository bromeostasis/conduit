import React, { useState, useEffect } from "react";

import MaterialSelector from './components/MaterialSelector'
import logo from './logo.svg';
import './App.css';


function App() {
    const [nextSelectors, setNextSelectors] = useState([])

    useEffect(() => {
        callApi([])
    }, []);

    const onSelectorChange = (index, value) => { // TODO: Maybe need to check for same value
        console.log(index, value)
        nextSelectors[index].selected = value
        setNextSelectors(nextSelectors) // TODO: Maybe useReducer to set individual field within. Also guarantee callApi happens after setSelectors

        const apiInput = nextSelectors.map((selector) => {
            const input = {}
            input[Object.keys(selector)[0]] = selector.selected
            return input
        })

        callApi(apiInput)
    }

    const callApi = (data) => {
        fetch("/get_next_selectors", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        }).then((res) =>
            res.json().then((data) => {
                setNextSelectors(nextSelectors.concat(data))
            })
        );
    }

    const selectors = []
    for (let i = 0; i < nextSelectors.length; i++) {
        selectors.push(<MaterialSelector index={i} selectorData={nextSelectors[i]} onChange={onSelectorChange} />)
    }

    return (
        <div className="App">
        Selectors: <br/>
        {selectors}
        </div>
    );
}

export default App;
