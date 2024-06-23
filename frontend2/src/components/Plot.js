import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';

const PlotComponent = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/data')
            .then(response => response.json())
            .then(data => {
                const plotData = [
                    {
                        x: data.map(item => item.SurveyDate),
                        y: data.map(item => item.Regular_Hokkaido),
                        type: 'scatter',
                        mode: 'lines+markers',
                        marker: { color: 'red' },
                    },
                ];
                setData(plotData);
            })
            .catch(error => console.error('Error fetching plot data:', error));
    }, []);

    return (
        <div>
            <h1>Plotly Graph</h1>
            <Plot
                data={data}
                layout={{ width: 720, height: 440, title: 'Regular Hokkaido Prices Over Time' }}
            />
        </div>
    );
};

export default PlotComponent;
