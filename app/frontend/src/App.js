import React from "react";

import { Route, Routes } from "react-router-dom";

import { Landing, Register, Agricultor, Vendedor, Pdf } from "./containers"

const App = () => {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Landing />} />
        <Route exact path="/register" element={<Register />} />
        <Route exact path="/produtor" element={<Agricultor />} />
        <Route exact path="/vendedor" element={<Vendedor />} />
        <Route exact path="/pdf" element={<Pdf />} />
      </Routes>
    </div>
  );
};

export default App;
