document.addEventListener('DOMContentLoaded', function () {
    fetch('/get_data')
        .then(response => response.json())
        .then(data => {
            let times = data.map(d => d[0]);
            let packetCounts = data.map(d => d[1]);
            let anomalyScores = data.map(d => d[2]);
            let packetSizes = data.map(d => d[3]);

            let trace = {
                x: times,
                y: packetCounts,
                z: anomalyScores,
                mode: 'markers',
                marker: {
                    size: packetSizes,
                    color: anomalyScores,
                    colorscale: 'Viridis',
                    showscale: true
                },
                type: 'scatter3d'
            };

            let layout = {
                title: 'Packet Traffic 3D Visualization',
                scene: {
                    xaxis: { title: 'Time (s)' },
                    yaxis: { title: 'Packet Count' },
                    zaxis: { title: 'Anomaly Score' }
                }
            };

            Plotly.newPlot('graph', [trace], layout);
        });
});
