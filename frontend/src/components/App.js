import React from 'react';
import request from 'superagent';

import Documents from './Documents';
import InfoBar from './InfoBar';
import TopBar from './TopBar';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      documents: [],
      filter: '',
      info: '',
    };
    this.doSetFilter = this.doSetFilter.bind(this);
  }

  componentDidMount() {
    this.fetchData();
  }

  doSetFilter(filter) {
    this.setState({ filter });
  }

  fetchData() {
    request.get('/api/v1/projects/').end((error, response) => {
      if (error) {
        console.log(error);
      } else {
        this.handleData(response.body);
      }
    });
  }

  handleData(documents) {
    const nextState = { documents };
    if (documents.length === 0) {
      nextState.info = (
        <div>
          <h4>No projects were found</h4>
          <a href="/api/v1/projects/name/version/">
            Click here to add one using the API
          </a>
        </div>
      );
    }
    this.setState(nextState);
  }

  render() {
    const filtered = this.state.documents.filter(document => (
      document.name.indexOf(this.state.filter) >= 0
    ));
    const infoBar = this.state.info ? (<InfoBar>{this.state.info}</InfoBar>) : null;
    return (
      <div>
        <TopBar doSetFilter={this.doSetFilter} />
        {infoBar}
        <Documents documents={filtered} />
      </div>
    );
  }
}

export default App;
