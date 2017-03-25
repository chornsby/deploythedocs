import React from 'react';
import { Alert, Grid } from 'react-bootstrap';

const InfoBar = ({ children }) => (
  <Grid>
    <Alert>{children}</Alert>
  </Grid>
);

InfoBar.propTypes = {
  children: React.PropTypes.node.isRequired,
};

export default InfoBar;
