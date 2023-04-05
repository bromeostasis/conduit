import React, { useState, useEffect } from "react";

import MaterialSelector from './components/MaterialSelector'
import logo from './logo.svg';
import './App.css';


function App() {
    const [ecn, setECN] = useState('')
    const [materialSelectors, setMaterialSelectors] = useState([])

    useEffect(() => {
        getNextSelectors([], [])
    }, []);

    const onSelectorChange = (index, value) => {
        console.log(index, value)
        let newMaterialSelectors = []
        if (value) {
            newMaterialSelectors = materialSelectors.slice(0, index + 1)
            newMaterialSelectors[index].selectedValue = value
        } else { // They've selected "~Select Value~", so remove the next choice
            newMaterialSelectors = materialSelectors.slice(0, index)
        }

        const apiInput = newMaterialSelectors.map((materialSelector) => {
            const selection = {}
            selection[Object.keys(materialSelector)[0]] = materialSelector.selectedValue
            return selection
        })

        getNextSelectors(apiInput, newMaterialSelectors)
    }

    const getNextSelectors = (currentMaterialSelections, newMaterialSelectors) => {
        fetch("/get_next_selectors", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(currentMaterialSelections)
        }).then((res) =>
            res.json().then((returnData) => {
                if (returnData['Extended Construction Numbers']) {
                    setECN(returnData['Extended Construction Numbers'])
                } else {
                    setECN('')
                    setMaterialSelectors(newMaterialSelectors.concat(returnData))
                }
            })
        );
    }

    const selectorElements = []
    for (let i = 0; i < materialSelectors.length; i++) {
        selectorElements.push(<MaterialSelector index={i} selectorData={materialSelectors[i]} onChange={onSelectorChange} withArrow={i < materialSelectors.length - 1} />)
    }

    return (
        <div className="App">
            <h2>
                Select your building materials:
            </h2>
            <div className='selectorWrapper'>
                {selectorElements}
            </div>
            {ecn && (
                <div className='ecn'>
                    <strong>Extended Construction Numbers:</strong> {ecn}
                </div>
            )}
        </div>
    );
}

export default App;
