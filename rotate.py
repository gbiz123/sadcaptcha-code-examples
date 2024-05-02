import requests
import base64

BASE_URL = "https://www.sadcaptcha.com/api/v1"
LICENSE_KEY = "YOUR_API_KEY_HERE"


# Build the rotate URL
rotate_url = f"{BASE_URL}/rotate?licenseKey={LICENSE_KEY}"

# Convert the images to base64 encoding
with open("images/outer_tt.png", "rb") as f:
    outer = base64.b64encode(f.read()).decode()
with open("images/inner_tt.png", "rb") as f:
    inner = base64.b64encode(f.read()).decode()

# Prepare the request
data = {
    "outerImageB64": outer,
    "innerImageB64": inner
}

# Get the answer as the solution angle
r = requests.post(rotate_url, json=data)

print(r.json())
