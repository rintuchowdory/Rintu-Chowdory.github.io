import json
import groq

def handler(event, context):
    try:
        # Your existing code to process the question
        client = groq.Client(api_key=os.environ.get("GROQ_API_KEY"))
        
        # ... your existing logic to generate response ...
        
        # Return response with CORS headers
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",  # This allows all domains
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "response": "Your generated response here"
            })
        }
    
    except Exception as e:
        # Error response with CORS headers
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
