import React from 'react';
import { Button, ButtonGroup, DropdownButton, MenuItem, Panel } from 'react-bootstrap';

import { ProjectType } from '../utils';

const Document = (props) => {
  const header = props.name;
  const latest = props.versions[0];
  const others = props.versions.slice(1);

  let dropdown = null;

  if (others.length > 0) {
    const menuItems = others.map(other => (
      <MenuItem key={other.version} href={other.url}>
        {other.version}
      </MenuItem>
    ));
    dropdown = (
      <DropdownButton id="seeMore" title="See more">{menuItems}</DropdownButton>
    );
  }

  const footer = (
    <ButtonGroup>
      <Button href={latest.url}>{latest.version}</Button>
      {dropdown}
    </ButtonGroup>
  );
  return (
    <Panel bsStyle="primary" header={header}>
      {footer}
    </Panel>
  );
};

Document.propTypes = React.PropTypes.shape(ProjectType);

export default Document;
