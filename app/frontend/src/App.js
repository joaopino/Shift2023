import React from "react";

import { Route, Routes } from "react-router-dom";

import { Landing, Register, Agricultor, Vendedor, Pdf, List } from "./containers"

const App = () => {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Landing />} />
        <Route exact path="/register" element={<Register />} />
        <Route exact path="/produtor" element={<Agricultor />} />
        <Route exact path="/revendedor" element={<Vendedor />} />
        <Route exact path="/pdf" element={<Pdf />} />
        <Route exact path="/list" element={<List />} />
      </Routes>
    </div>
  );
};

export default App;
