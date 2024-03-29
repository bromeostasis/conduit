import React from 'react';

const MaterialSelector = ({ index, onChange, selectorData, withArrow }) => {
    const materialCategory = Object.keys(selectorData)[0]
    const materialValues = selectorData[materialCategory]
    const selectedValue = selectorData['selectedValue']
    return (
        <div className='selector'>
            <div className='selectBox'>
                <label>{materialCategory}</label>
                <select key={materialCategory} onChange={(e) => onChange(index, e.target.value)} value={selectedValue || ''}>
                  <option value=''>~Select value~</option>
                  {materialValues.map((materialValue) => (
                    <option key={materialValue} value={materialValue}>{materialValue}</option>
                  ))}
                </select>
            </div>
            {withArrow && (
                <span className='arrow'> -> </span>
            )}
        </div>
    )
}

export default MaterialSelector;