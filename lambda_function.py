import json
import uuid
import requests


# Define Lok's Supabase credentials
#SUPABASE_URL = "https://tmztgmqmrpbyehsadbkr.supabase.co"
#SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRtenRnbXFtcnBieWVoc2FkYmtyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjA3NTQwOTQsImV4cCI6MjAzNjMzMDA5NH0.pIzuo5c39jH7LSnhqI8P-#imlFXU1-LY5Nf-dMtYs14Y"

# Define Shikha's Supabase credentials
SUPABASE_URL = "https://xgxgmqodxqrfvumguvxc.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhneGdtcW9keHFyZnZ1bWd1dnhjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjA3NTQyMDYsImV4cCI6MjAzNjMzMDIwNn0.Cq7UNNtnoTtsQpIA1kCtUkOk9n8j8Qh5ugSofRuYKnk"

# Define the headers for the HTTP request
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# Define the endpoint for the HTTP request
endpoint = f"{SUPABASE_URL}/rest/v1/customer_feedback"

def get_feedback():
    """
    Retrieve details of customer feedback
    """
    try:
        # Make the HTTP request
        response = requests.get(endpoint, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4))
            return data
        else:
            print(response.text)
            return {'message': response.text}
    except Exception as e:
        print(str(e))
        return {'error': str(e)}


def lambda_handler(event, context):
    # get the action group used during the invocation of the lambda function
    actionGroup = event.get('actionGroup', '')
    
    # name of the function that should be invoked
    function = event.get('function', '')
    
    # parameters to invoke function with
    parameters = event.get('parameters', [])

    if function == 'get_feedback':
        response = str(get_feedback())
        responseBody = {'TEXT': {'body': json.dumps(response)}}

    else:
        responseBody = {'TEXT': {'body': 'Invalid function'}}

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }
    }

    function_response = {'response': action_response, 'messageVersion': event['messageVersion']}
    print("Response: {}".format(function_response))

    return function_response
