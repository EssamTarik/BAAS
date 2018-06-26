import {combineReducers, createStore, applyMiddleware} from 'redux';
import thunk from 'redux-thunk';
import apiTestReducer from './apiTestReducer';

const testReducer = (state='defaultReducer') => state;
const rootReducer = combineReducers({
	test: testReducer,
	apiTest: apiTestReducer,
});

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;