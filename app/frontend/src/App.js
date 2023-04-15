import React from "react";

import { Route, Routes } from "react-router-dom";

import { Landing, Register } from "./containers"

const App = () => {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Landing />} />
        <Route exact path="/register" element={<Register />} />
      </Routes>
    </div>
  );
};

export default App;
