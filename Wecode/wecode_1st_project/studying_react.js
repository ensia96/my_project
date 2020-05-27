import React from "react";
import "./styles.css";

class App extends React.Component {
  componentDidMount() {
    fetch("https://api.kurly.com/v2/categories?ver=1")
      .then(res => res.json())
      .then(res => {
        console.log(res);
      });
  }

  render() {
    return (
      <div className="App">
        <h1>Hello CodeSandbox</h1>
        <h2>Start editing to see some magic happen!</h2>
      </div>
    );
  }
}

export default App;
