import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import baas from 'baas-library'

var token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6IjEyMyIsImVtYWlsIjoiZXNzYW0iLCJfaWQiOnsiJG9pZCI6IjVhY2JiNmJhN2Y3OGIxMGZmMmRjODEyNiJ9fQ.zhcvC1RjxZcYMPcss2c-by1Fn4u-xpU5nFVNPTE-W8I';

class App extends Component {
	constructor(props){
		super(props);
		this.state = {data: [], text: ''}
	}
	componentDidMount(){
		baas.listen("sessiondb.comedyMovies", token, (response) => {
			this.setState({data: response.message});
		});
	}
	updateVals(){
		baas.update("sessiondb.comedyMovies", token, {name: this.state.data[0].name}, {name: this.state.text});
	}
	render() {
		return (
		  <div className="App">
			<header className="App-header">
			  <img src={logo} className="App-logo" alt="logo" />
			  <h1 className="App-title">Welcome to React</h1>
			</header>
			<input type="text" onChange={(event) => {this.setState({text: event.target.value})}} />
			<button onClick={this.updateVals.bind(this)} value="update">update name</button>
			<div className="App-intro">
			{this.state.data.map((item) => <div>{JSON.stringify(item)}</div>)}
			</div>
		  </div>
		);
	}
}

export default App;
