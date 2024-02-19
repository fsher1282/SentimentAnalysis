# Sentiment Analyzer [In Progress]

## Overview
This project is a sentiment analysis web application that processes user-submitted text, analyzes its sentiment, and visualizes the results. It leverages AWS services, including Lambda for processing and AWS RDS for storing the analysis results. The frontend consists of a simple webpage (`home.html`) that embeds a YouTube video and includes a text box for user input. After processing, users are redirected to `results.html`, where their sentiment score is highlighted within a D3 graph along with other scores. The application offers an intuitive demonstration of cloud-based sentiment analysis and data visualization.

### Components
- **Frontend**: A simple HTML page (`home.html`) with an embedded YouTube video and a text box for user input.
- **Backend**: AWS Lambda function for sentiment analysis.
- **Database**: AWS RDS for storing sentiment analysis results.
- **Visualization**: D3.js for displaying sentiment scores on `results.html`.

## Setup Instructions

### Requirements
- AWS Account
- AWS CLI configured
- Node.js and npm (for D3.js and other JavaScript dependencies)
- Python 3.x

### Configuring AWS Services

#### AWS RDS
1. Set up an AWS RDS instance.
2. Configure the database schema with the following columns: `id`, `user_text`, `polarity`, `subjectivity`, `created_at`, `summary`.

#### AWS Lambda
1. Create a new Lambda function for sentiment analysis processing.
2. Install the `textblob` Python package locally and include it in your Lambda deployment package.
3. Set up an API Gateway to trigger the Lambda function upon user input submission.

### Deploying the Frontend
1. Host `home.html` and `results.html` on a static web hosting service or your server.
2. Ensure the form in `home.html` correctly points to your AWS API Gateway endpoint.

### Local Development
- For local development, ensure Python 3.x is installed for Lambda function testing.
- Use a local server to test `home.html` and `results.html` to circumvent CORS issues.

## Usage

1. **Submit Opinion**: Users navigate to `home.html`, watch the embedded YouTube video, and submit their opinion via the text box.
2. **Processing**: The input is sent to the AWS Lambda function via API Gateway for sentiment analysis. The results are stored in AWS RDS.
3. **View Results**: Users are redirected to `results.html`, where a D3.js graph displays their sentiment score alongside other stored scores. The page also provides explanations of the results.

