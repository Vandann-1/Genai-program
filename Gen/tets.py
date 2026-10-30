import os
from google import genai

api_key = os.getenv("AQ.Ab8RN6Io05C_Ef-1us1eSDZGLgUM8X1mCENn4yC47_sS2rTokw")

print("API KEY FOUND:", bool(api_key))

try:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Reply with only: API WORKING"
    )

    print("SUCCESS:", response.text)

except Exception as e:
    print("ERROR:", type(e).__name__, str(e))