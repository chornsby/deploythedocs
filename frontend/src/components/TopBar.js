import React from 'react';
import { Navbar } from 'react-bootstrap';
import SearchInput from './SearchInput';

const TopBar = ({ doSetFilter }) => (
  <Navbar inverse staticTop>
    <Navbar.Header>
      <Navbar.Brand>
        <a href="/">Deploy The Docs</a>
      </Navbar.Brand>
      <Navbar.Toggle />
    </Navbar.Header>
    <Navbar.Collapse>
      <Navbar.Form pullRight>
        <SearchInput doSetFilter={doSetFilter} />
      </Navbar.Form>
    </Navbar.Collapse>
  </Navbar>
);

TopBar.propTypes = {
  doSetFilter: React.PropTypes.func.isRequired,
};

export default TopBar;
