import {request} from '../services/backend';

export default () => {
	return (dispatch) => {
		request('test', (response) => {
			dispatch({
				type: 'apiTestCallFinished',
				payload: response
			})
		})
	}
}