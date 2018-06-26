export default (state=false, action) => {
	switch(action.type){
		case "apiTestCallFinished":
			return action.payload;
		default:
			return state;
	}
}