const url = process.env.NODE_ENV === 'development' ? 'http://localhost:5000/admin/' : '/admin/';

const request = (endPoint, callback) => {
	fetch(url+endPoint).then((response) => response.json()).then(callback);
}

export {request};