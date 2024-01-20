import json
from textblob import TextBlob

def lambda_handler(event, context):
    # Parse the incoming JSON to get the text
    try:
        body = json.loads(event['body'])
        text = body['text']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('No text provided')
        }

    # Analyze sentiment
    blob = TextBlob(text)
    sentiment = blob.sentiment

    # Create response
    response = {
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response)
    }

# Example test event
if __name__ == "__main__":
    test_event = {
        'body': json.dumps({'text': 'TextBlob is amazingly simple to use. What a great fun!'})
    }
    print(lambda_handler(test_event, None))
