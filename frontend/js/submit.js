function analyzeSentiment() {
    var text = document.getElementById('inputText').value;
    var apiURL = 'https://k429vsoeb8.execute-api.us-west-1.amazonaws.com/prod/'
    var apiKey = 'MXZBQ8gpq54uCdJqMnmVS7hef24rEoJX70wXUjQZ';

    fetch(apiURL, {
            method: 'POST',
            body: JSON.stringify({ text: text }),
            headers: {
                'x-api-key': apiKey,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('API call failed with HTTP status ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            document.getElementById('result').textContent = 'Sentiment Score: ' + data.sentimentScore; // Display success message
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById('result').textContent = 'Error: ' + error.message; // Display error message
        });
    }