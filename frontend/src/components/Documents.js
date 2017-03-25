import React from 'react';
import { Col, Grid, Row } from 'react-bootstrap';

import Document from './Document';
import { chunk, ProjectType } from '../utils';

const Documents = ({ documents }) => {
  const rows = chunk(documents, 3).map((row, i) => {
    const columns = row.map(document => (
      <Col key={document.name} sm={4}>
        <Document {...document} />
      </Col>
    ));
    return (<Row key={i}>{columns}</Row>);
  });

  return (
    <Grid>
      {rows}
    </Grid>
  );
};

Documents.propTypes = {
  documents: React.PropTypes.arrayOf(
    React.PropTypes.shape(ProjectType),
  ).isRequired,
};

export default Documents;
