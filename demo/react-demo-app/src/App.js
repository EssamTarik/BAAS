import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import baas from 'baas-library'
import uuid from 'uuid/v4';

var token = 'e642c88c-dba8-474e-ace5-7530126e7432';

class App extends Component {
	constructor(props){
		super(props);
		this.state = {data: [], text: ''}
	}
	componentDidMount(){
		baas.listen("sessiondb.testCollection", token, (response) => {
			if(response.code === 1){
				console.log(response.message);
				this.setState({data: response.message});
			}
			else
				console.log(response);
		});
	}
	removeRecord(name){
		baas.remove('sessiondb.testCollection', token, {name});
	}
	insertRecord(){
		let name = prompt("Enter student's name :");
		if (name && name.length > 0)
			baas.insert('sessiondb.testCollection', token, {name});
	}
	render() {
		return (
		  <div className="App">
			<header className="App-header">
			  <img src={logo} className="App-logo" alt="logo" />
			  <h1 className="App-title">Welcome to BaaS demo</h1>
			</header>
			<div style={{marginTop: 10}}>
				<div style={{textAlign: 'center'}}>
					<button className="btn btn-success btn-md" onClick={this.insertRecord.bind(this)}>Add student</button>
				</div>
				<div style={{margin: 10, textAlign: 'left'}}>
					<h4>Users: </h4>
					{this.state.data.map((record) => {
						return (
							<div key={uuid()} style={{margin: 10}} className="row alert alert-info">
								<div className="col-xs-6">{record.name}</div>
								<div className="col-xs-6" style={{textAlign: 'right'}}>
									<a href="javascript://" onClick={() => this.removeRecord(record.name)}><span style={{color: 'red'}} className="glyphicon glyphicon-remove-sign" aria-hidden="true"></span></a>
								</div>
							</div>
						);
					})}
				</div>
			</div>
		  </div>
		);
	}
}

export default App;
