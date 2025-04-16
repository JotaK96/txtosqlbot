import os
from dotenv import load_dotenv
import groq

# Load environment variables from .env file
load_dotenv()

# Get the GROQ_API_KEY from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

print(f"Testing GROQ API key...")

if not groq_api_key:
    print("ERROR: GROQ_API_KEY not found in environment variables")
    print("Please make sure it's correctly set in your .env file")
    exit(1)

# Mask most of the API key for security
masked_key = groq_api_key[:5] + "..." + groq_api_key[-5:]
print(f"Found API key: {masked_key}")

# Test the API key with a simple request
try:
    client = groq.Groq(api_key=groq_api_key)
    models = client.models.list()
    print("API key is valid! Available models:")
    for model in models.data:
        print(f"- {model.id}")
    print("\nYour Groq API key is working correctly!")
except Exception as e:
    print(f"ERROR: Could not connect to Groq API: {str(e)}")
    print("Please check your API key and internet connection")
    exit(1)
