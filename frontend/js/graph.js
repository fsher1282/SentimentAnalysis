document.addEventListener('DOMContentLoaded', function() {
    // Example data
    var individual_score = { 'polarity': 0.5, 'subjectivity': 0.7 };
    var other_surveyors = [
        { 'polarity': 0.2, 'subjectivity': 0.4 },
        { 'polarity': -0.6, 'subjectivity': 0.3 },
        { 'polarity': 0.1, 'subjectivity': 0.5 }
    ];

    // Preparing data for plotting
    var trace0 = {
        x: other_surveyors.map(s => s.polarity),
        y: other_surveyors.map(s => s.subjectivity),
        mode: 'markers',
        name: 'Other Surveyors'
    };

    var trace1 = {
        x: [individual_score.polarity],
        y: [individual_score.subjectivity],
        mode: 'markers',
        marker: { color: 'red' },
        name: 'Individual'
    };

    // Lines at X=0 and Y=0
    var line_x = {
        x: [0, 0],
        y: [-1, 1],
        mode: 'lines',
        line: { dash: 'solid', color: 'grey' },
        showlegend: false
    };

    var line_y = {
        x: [-1, 1],
        y: [0, 0],
        mode: 'lines',
        line: { dash: 'solid', color: 'grey' },
        showlegend: false
    };

    var data = [trace0, trace1, line_x, line_y];

    // Layout
    var layout = {
        title: 'Sentiment Analysis Comparison',
        xaxis: { title: 'Polarity (-1 to 1)', range: [-1, 1] },
        yaxis: { title: 'Subjectivity (0 to 1)', range: [0, 1] },
        hovermode: 'closest'
    };

    // Create the figure and plot it
    Plotly.newPlot('myDiv', data, layout);
});
