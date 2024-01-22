import json
from textblob import TextBlob

def interpret_polarity(score):
    if score <= -0.6:
        return "Very Negative"
    elif -0.6 < score <= -0.2:
        return "Negative"
    elif -0.2 < score <= 0.2:
        return "Neutral"
    elif 0.2 < score <= 0.6:
        return "Positive"
    else:
        return "Very Positive"

def interpret_subjectivity(score):
    if score <= 0.2:
        return "Very Objective"
    elif 0.2 < score <= 0.4:
        return "Somewhat Objective"
    elif 0.4 < score <= 0.6:
        return "Neutral"
    elif 0.6 < score <= 0.8:
        return "Somewhat Subjective"
    else:
        return "Very Subjective"
    
def generate_summary(polarity_desc, subjectivity_desc):
    # First sentence describes the polarity
    polarity_sentence = f"The sentiment of the text is {polarity_desc}."
    
    # Second sentence describes the subjectivity
    subjectivity_sentence = f"The text is {subjectivity_desc} in nature."
    
    # Combine sentences for the full summary
    summary = f"{polarity_sentence} {subjectivity_sentence}"
    
    return summary


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
    polarity_desc = interpret_polarity(sentiment.polarity)
    subjectivity_desc = interpret_subjectivity(sentiment.subjectivity)

    # Generate the summary
    summary = generate_summary(polarity_desc, subjectivity_desc)



    # Create response
    response = {
        'polarity': sentiment.polarity,
            'polarity_description': polarity_desc,
            'subjectivity': sentiment.subjectivity,
            'subjectivity_description': subjectivity_desc,
            'summary': summary

    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response)
    }


if __name__ == "__main__":
    test_event = {
        'body': json.dumps({'text': 'TextBlob is amazingly simple to use. What a great fun!'})
    }
    print(lambda_handler(test_event, None))
