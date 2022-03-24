import * as api from "../api/index";

export const uploadFile = (formData) => async (dispatch) => {
    try{
        const data = await api.uploadFile(formData);
        console.log(data["data"])
        const action = {
            type : "UPLOAD_FILE",
            payload: data["data"]
        }
        dispatch(action);
    } catch(error){
        console.log("Error in uploading the file. Error: ", error.message);
    }
}