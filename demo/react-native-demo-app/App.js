import React from 'react';
import { StyleSheet, Text, View, TextInput, Button, ScrollView, TouchableOpacity } from 'react-native';
// import Prompt from 'react-native-prompt';
import baas from 'baas-library';
import uuid from 'uuid/v4';

const token = 'e642c88c-dba8-474e-ace5-7530126e7432';

export default class App extends React.Component {
	constructor(props){
		super(props);
		this.state = {data: [], initialized: false, address: "", studentName: ""}
		this.prepareBaaS = this.prepareBaaS.bind(this);
	}
	prepareBaaS(addr){
		this.setState({initialized: true});
		baas.initialize(addr, token);

		baas.listen("sessiondb.testCollection", (response) => {
			if(response.code === 1){
				console.log(response.message);
				this.setState({data: response.message});
			}
			else
				console.log(response);
		});
	}
	removeRecord(name){
		baas.remove('sessiondb.testCollection', {name});
	}
	insertRecord(name){
		if (name && name.length > 0) 
			baas.insert('sessiondb.testCollection', {name});
	}
	render() {
		console.log(this.state.address);
		if(!this.state.initialized){
			return (
				<View style={{paddingTop: 100}}>
					<TextInput
						style={{paddingBottom: 5}}
					    placeholder="Enter BaaS address"
					    value={this.state.address}
					    onChangeText={(address) => this.setState({address})}
					    />
					<Button onPress={() => this.prepareBaaS(this.state.address.toLowerCase())} title="Set" />
				</View>	
			);
		}else{
			return (
			  <View style={styles.container}>
			  	<TextInput
			  		style={{paddingBottom: 5}}
			  		value={this.state.studentName}
			  	    placeholder="Enter new student's name"
			  	    onChangeText={(studentName) => this.setState({studentName})}
			  	    />
				<Button onPress={() => {this.setState({studentName: ''}); this.insertRecord(this.state.studentName)}} title="Add student" />
			  	<ScrollView>
			  		{this.state.data.map((record) => {
			  			return (
			  				<TouchableOpacity key={uuid()} onPress={() => {this.removeRecord(record.name)}}>
			  				<View style={{backgroundColor: 'grey', padding: 5}}>
			  					<Text style={{color: 'black'}}>{record.name}</Text>
			  				</View>
			  				</TouchableOpacity>
			  			);
			  		})}
			  	</ScrollView>
			  </View>
			);			
		}
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: 40,
  },
});
