import plotly.graph_objs as go
import plotly.offline as pyo

# Example data
individual_score = {'polarity': 0.5, 'subjectivity': 0.7}
other_surveyors = [
    {'polarity': 0.2, 'subjectivity': 0.4},
    {'polarity': -0.6, 'subjectivity': 0.3},
    {'polarity': 0.1, 'subjectivity': 0.5}
]

# Preparing data for plotting
trace0 = go.Scatter(
    x=[s['polarity'] for s in other_surveyors],
    y=[s['subjectivity'] for s in other_surveyors],
    mode='markers',
    name='Other Surveyors'
)

trace1 = go.Scatter(
    x=[individual_score['polarity']],
    y=[individual_score['subjectivity']],
    mode='markers',
    marker=dict(color='red'),
    name='Individual'
)

# Lines at X=0 and Y=0
line_x = go.Scatter(
    x=[0, 0],
    y=[-1, 1],
    mode='lines',
    line=dict(dash='solid', color='grey'),
    showlegend=False
)

line_y = go.Scatter(
    x=[-1, 1],
    y=[0, 0],
    mode='lines',
    line=dict(dash='solid', color='grey'),
    showlegend=False
)

data = [trace0, trace1, line_x, line_y]

# Layout
layout = go.Layout(
    title='Sentiment Analysis Comparison',
    xaxis=dict(title='Polarity (-1 to 1)', range=[-1, 1]),
    yaxis=dict(title='Subjectivity (0 to 1)', range=[0, 1]),
    hovermode='closest'
)

# Create the figure
fig = go.Figure(data=data, layout=layout)

# Plot the figure
pyo.plot(fig, filename='sentiment_analysis_comparison.html')