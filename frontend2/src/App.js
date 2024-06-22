import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/plot')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
      });
  }, []);

  return (
    <div>
      <h1>Data Table</h1>
      <table border="1">
        <thead>
        <title>Plotly Graph</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </thead>
        <tbody>
          {data.map((row) => (
            <tr key={row.id}>
              <td>{row.SurveyDate}</td>
              <td>{row.Regular_Hokkaido}</td>
              <td>{row.High_octane_Hokkaido}</td>
              <td>{row.light_oil_Hokkaido}</td>
              <td>{row.Kerosene_Hokkaido}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
