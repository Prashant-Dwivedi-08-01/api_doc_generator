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
        alert(`Selected File: ${uploadedFile.current.files[0].name}`)

        // const formData = JSON.stringify({ "collection": uploadedFile.current.files[0] });
        const formData = new FormData()
        formData.append('collection', uploadedFile.current.files[0])
        await dispatch(uploadFile(formData));
    } 
    useEffect(() => {
        console.log(html_doc)
    }, [html_doc])




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