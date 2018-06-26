import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux'
import apiTest from './actions/apiTest';

class App extends Component {
	componentDidMount(){
		this.props.apiTest();
	}
	render() {
		console.log(this.props.apiTestReducer);
		return (
			<div className="App">
				<header className="App-header">
					<img src={logo} className="App-logo" alt="logo" />
					<h1 className="App-title">Welcome to React</h1>
				</header>
				<p className="App-intro">
					To get started, edit <code>src/App.js</code> and save to reload.
				</p>
			</div>
		);
	}
}
const mapDispatchToProps = (dispatch) => {
	return bindActionCreators({apiTest}, dispatch);
}
const mapStateToProps = (state) => {
	return {testReducer: state.test, apiTestReducer: state.apiTest}
}
export default connect(mapStateToProps, mapDispatchToProps)(App);
