import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import {Provider} from 'react-redux';
import store from './reducers';
import { BrowserRouter as Router, Route } from "react-router-dom";


ReactDOM.render(<Provider store={store}>
	<Router>
		<div>
			<Route exact path='/' component={App} />
			<Route path='/test' component={App} />
		</div>
	</Router>
	</Provider>, document.getElementById('root'));
registerServiceWorker();
