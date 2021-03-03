import React, { useState, useEffect } from "react";

function App() {
  const [resultText, setResultText] = useState("Loading...");
  useEffect(() => {
    fetch('/api/predictions/latest')
      .then(r => r.text())
      .then(data => {
        console.log(data);
        setResultText(data);
      });
  });

  return (
    <div className="App">
      {resultText}
    </div>
  );
}

export default App;
