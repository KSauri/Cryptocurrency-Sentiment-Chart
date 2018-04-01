import Chart from 'chart.js';
import io from 'socket.io-client';

export default function main () {
    const socket = io('http://localhost:5000');

    socket.on('message', function (data) {
        // socket.send(msg);
        console.log(data)
    });

    // socket.on('message', function(data) {
    //     $('#chat').val($('#chat').val() + data.msg + '\n');
    //     $('#chat').scrollTop($('#chat')[0].scrollHeight);
    // });
    
    var ctx = document.getElementById("myChart").getContext('2d');
    
    // needs start method
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00"],
            datasets: [{
                label: "dogecoin",
                data:[-0.5175897, -0.7580912, 0.4987275, 0.8438190, 0.1073900, -0.1808840, -0.4413588, 0.3021072],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
                fill:false
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:false
                    }
                }]
            }
        }
    });
    
}
