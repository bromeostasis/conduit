import React from 'react';

const MaterialSelector = ({ index, selectorData, onChange }) => {
	const key = Object.keys(selectorData)[0]
	const values = selectorData[key]
	const selected = selectorData['selected']
	return (
	  <>
	    <label>{key}</label>
	    <select key={key} onChange={(e) => onChange(index, e.target.value)}>
	      <option value={undefined}>~Select value~</option>
	      {values.map((value) => (
	        <option value={value} selected={value === selected}>{value}</option>
	      ))}
	    </select>
	  </>
	)
}

export default MaterialSelector;