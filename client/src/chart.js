import { Line } from 'react-chartjs-2';
import React from 'react';
import io from 'socket.io-client';

export const redditBackgroundColor = [
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)'
];

export const redditBorderColor = [
    'rgba(255,99,132,1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)'
];
let redditData = {
    label: 'Reddit',
    yAxisID: 'reddit',
    data: [100, 96, 84, 76, 69],
    borderColor: redditBorderColor,
    backgroundColor: redditBackgroundColor
}

let cryptoData = {
    label: 'Crypto',
    yAxisID: 'crypto',
    data: [.12, .44, -.1, -.21, 0]
};

const options = {
    scales: {
      yAxes: [{
        id: 'reddit',
        type: 'linear',
        position: 'left',
      }, {
        id: 'crypto',
        type: 'linear',
        position: 'right',
        ticks: {
          max: 1,
          min: -1
        }
      }]
    }   
};

const data = {
    labels: ['00:00:00', '00:00:05', '00:00:10', '00:00:15', '00:00:20'],
    datasets: [redditData, cryptoData]
};


const Chart = (props) => {
    var socket = io("http://localhost:3000/");
    socket.on('messages', function(data) {
        alert(data);
    });
    const chart = <Line data={data} options={options} />;
    return chart;
};

export default Chart;
