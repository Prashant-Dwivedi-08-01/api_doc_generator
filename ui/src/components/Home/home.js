import React, { useState, useRef, useEffect } from "react";
import { uploadFile } from "../../actions/home"
import { useDispatch } from "react-redux";
import { useSelector } from 'react-redux';
import "./home.css"

const Home = () => {

    const uploadedFile = useRef(null);
    const dispatch = useDispatch();

    const html_doc = useSelector(state => state.html)

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData()
        formData.append('collection', uploadedFile.current.files[0])

        const requestOptions = {
            method: 'POST',
            body: formData
        };

        fetch('http://localhost:5000/upload', requestOptions)
            .then(response => {
                response.blob().then(blob => {
                    let url = window.URL.createObjectURL(blob);
                    let a = document.createElement('a');
                    a.href = url;
                    a.download = 'doc.html';
                    a.click();
                });
            });
    }


    return (
        <>
            {/* <form onSubmit={handleSubmit}>
                <label>
                    File:
                    <input type="file" ref={uploadedFile} />
                </label>
                <input type="submit" value="Submit" />
            </form> */}
            <div class="v684_4074"><h1 class="v712_4145">API COLLECTION</h1><h1 class="v802_4026">TO</h1><h1
                class="v712_4146">HTML DOC</h1>
                <div class="v712_4147">
                    <div class="v714_4082"></div>
                    <div class="v714_4080"></div>
                    <div class="v712_4150">
                        <div class="v712_4151"></div>
                        <div class="v712_4152"></div>
                    </div>
                </div>
                <form onSubmit={handleSubmit}>
                    {/* <label>
                        File:
                        <input type="file" ref={uploadedFile} />
                    </label>
                    <input type="submit" value="Submit" /> */}
                <input type="file" className="file-input" ref={uploadedFile} />
                <div class="v802_4027"></div>
                <span class="v802_4028" onClick={handleSubmit} style={{"cursor":"pointer"}}>Upload</span>
                <span class="v802_4029" >Upload your Postman collection here</span>
                </form> 
            </div>
        </>
    )
}

export default Home