import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/data')
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
          <tr>
            <th>ID</th>
            <th>SurveyDate</th>
            <th>Regular_Hokkaido</th>
            <th>High_Octane_Hokkaido</th>
            <th>Light_Oil_Hokkaido</th>
            <th>Kerosene_Hokkaido</th>
          </tr>
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
