import requests
import base64

BASE_URL = "https://www.sadcaptcha.com/api/v1"
LICENSE_KEY = "YOUR_API_KEY_HERE"


# Build the shapes URL
shapes_url = f"{BASE_URL}/shapes?licenseKey={LICENSE_KEY}"

# Convert the images to base64 encoding
with open("images/tiktok3d.png", "rb") as f:
    shapes = base64.b64encode(f.read()).decode()

# Prepare the request
data = {"imageB64": shapes}

# Get the answer as point ratios
r = requests.post(shapes_url, json=data)

print(r.json())
