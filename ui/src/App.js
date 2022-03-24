import React from 'react';
import "./styles.css";
import Home from "./components/Home/home";

import { BrowserRouter, Route, Routes, Redirect } from "react-router-dom";

const App = () => {
  return (

    <BrowserRouter>
      <div>
        <Routes>
        <Route path="/" element={<Home/>} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App;