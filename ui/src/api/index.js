import axios from "axios";

const API = axios.create({ baseURL: "http://localhost:5000" });

export const uploadFile = (data) => API.post('/upload', data, {
    headers: {
        "Content-type": "multipart/form-data"
    }
});