import React from "react";

import { Route, Routes } from "react-router-dom";

import { Landing } from "./containers"

const App = () => {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Landing />} />
      </Routes>
    </div>
  );
};

export default App;
