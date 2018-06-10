import Chart from 'chart.js';
import io from 'socket.io-client';
import { redditBackgroundColor, redditBorderColor } from './chartsettings.js';

// Psuedocode of what needs to happen:
// A chart needs to load after the page is ready.
// Data needs to be sent that populates the full chart.
// Methods needs to be created that update the data within the chart.


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
    data: [1, 1, 1, 1, 0]
};

export default function main () {
    // const socket = io('http://localhost:5000');

    var ctx = document.getElementById("myChart").getContext('2d');
    
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['00:00:00', '00:00:05', '00:00:10', '00:00:15', '00:00:20'],
            datasets: [redditData, cryptoData]
        },
        options: {
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
                min: 0
                }
            }]
            }
        }
    });

    function addData(chart, label, data, idx) {
        chart.data.labels.push(label);
        chart.data.datasets[idx].push(data)
        chart.update();
    }
    

    socket.on('connect_response', function (data) {
        console.log(data)
        
    });
    
    socket.on('reddit', function (data) {
        // socket.send(msg);
        console.log(data)
    });
    
}
