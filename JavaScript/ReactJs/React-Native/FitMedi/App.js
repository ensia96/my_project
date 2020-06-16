import React, {Component} from 'react';

import Loading from './temp/Loading';
import Login from './temp/Login';
import Main from './temp/Main';
import Survey from './temp/Survey';
import Wating from './temp/Wating';
import Routine from './temp/Routine';
import Description from './temp/Description';
import Search from './temp/Search';
import Nav from './temp/Nav';
import Active from './temp/Active';

export default class App extends Component {
  state = {loading: true, done: false};
  componentDidMount() {
    setTimeout(() => {
      this.setState({loading: false});
      this.setState({done: true});
    }, 3000);
  }

  render() {
    return (
      <>
        <Login />
      </>
    );
    /*
    <Routine />
    <Loading />
    <Main />
    <Survey />
    <Wating />
    <Description />
    <Search />
    <Nav />
    <Active />
    return <>{this.state.done ? <Wating /> : <Survey />}</>;
    return <>{this.state.loading ? <Loading /> : <Login />}</>;
    */
  }
}
