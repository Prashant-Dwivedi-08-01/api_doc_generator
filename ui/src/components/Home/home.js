import React, { useState, useRef, useEffect } from "react";
import { uploadFile } from "../../actions/home"
import { useDispatch } from "react-redux";
import { useSelector } from 'react-redux';

const Home = () => {

    const uploadedFile = useRef(null);
    const dispatch = useDispatch();

    const html_doc = useSelector(state => state.html)

    const handleSubmit = async(e) => {
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
            <form onSubmit={handleSubmit}>
                <label>
                    File:
                    <input type="file" ref={uploadedFile} />
                </label>
                <input type="submit" value="Submit" />
            </form>
        </>
    )
}

export default Home