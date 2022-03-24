import * as api from "../api/index";

export const uploadFile = (formData) => async (dispatch) => {
    try{
        const response = await api.uploadFile(formData);

        const action = {
            type : "UPLOAD_FILE",
            payload: response
        }
        dispatch(action);
    } catch(error){
        console.log("Error in uploading the file. Error: ", error.message);
    }
}