const reducer = (state = {html: null}, action)=>{
    switch (action.type) {
        case "UPLOAD_FILE":
            return {...state, html: action?.payload } ;
        default:
            return state
    }
}
export default reducer