import './styles.css'
export const TextInput = ({handleChange, searchValue}) => {
	return (
		<input onChange={handleChange} 
			value={searchValue}
			type="search" 
			className="text-input"
			placeholder="Type your search"
		/>
	)
}