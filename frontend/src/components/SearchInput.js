import React from 'react';
import { FormControl, FormGroup, InputGroup } from 'react-bootstrap';
import FaSearch from 'react-icons/lib/fa/search';

const SearchInput = ({ doSetFilter }) => (
  <FormGroup>
    <InputGroup>
      <InputGroup.Addon>
        <FaSearch />
      </InputGroup.Addon>
      <FormControl
        onChange={event => doSetFilter(event.target.value)}
        placeholder="Search"
        type="text"
      />
    </InputGroup>
  </FormGroup>
);

SearchInput.propTypes = {
  doSetFilter: React.PropTypes.func.isRequired,
};

export default SearchInput;
