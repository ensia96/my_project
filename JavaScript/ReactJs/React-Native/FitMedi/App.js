import React, {Component} from 'react';

import Loading from './temp/Loading';
import Login from './temp/Login';
import Survey from './temp/Survey';

export default class App extends Component {
  state = {loading: true};
  componentDidMount() {
    setTimeout(() => {
      this.setState({loading: false});
    }, 3000);
  }

  render() {
    return <>{this.state.loading ? <Loading /> : <Login />}</>;

    /*
        return (
          <>
            <Survey />
          </>
        );
    */
  }
}
