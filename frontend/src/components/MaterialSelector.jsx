import React from 'react';

const MaterialSelector = ({ index, onChange, selectorData, withArrow }) => {
	const key = Object.keys(selectorData)[0]
	const values = selectorData[key]
	const selected = selectorData['selected']
	return (
	  <>
	    <label>{key}</label>
	    <select key={key} onChange={(e) => onChange(index, e.target.value)}>
	      <option value=''>~Select value~</option>
	      {values.map((value) => (
	        <option value={value} selected={value === selected}>{value}</option>
	      ))}
	    </select>
	    {withArrow && (
	    	<span> -> </span>
	    )}
	  </>
	)
}

export default MaterialSelector;