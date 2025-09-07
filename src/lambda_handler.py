import json  # Assuming you meant JSON instead of 'gros'

def handle(event, context):
    try:
        # Your actual processing logic here
        # Example: client = some_client(api_key)
        response_data = {"response": "Your generated response here"}
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",  # Fixed typo
                "Access-Control-Allow-Methods": "GET, OPTIONS",  # Fixed typo
                "Access-Control-Allow-Headers": "Content-Type"  # Fixed typo
            },
            "body": json.dumps(response_data)
        }
    except Exception as e:  # Fixed exception handling
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"error": str(e)})  # Proper error message
        }
