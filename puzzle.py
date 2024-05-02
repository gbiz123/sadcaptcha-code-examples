import requests
import base64

BASE_URL = "https://www.sadcaptcha.com/api/v1"
LICENSE_KEY = "YOUR_API_KEY_HERE"


# Build the puzzle URL
puzzle_url = f"{BASE_URL}/puzzle?licenseKey={LICENSE_KEY}"

# Convert the images to base64 encoding
with open("images/puzzle.jpg", "rb") as f:
    puzzle = base64.b64encode(f.read()).decode()
with open("images/piece.png", "rb") as f:
    piece = base64.b64encode(f.read()).decode()

# Prepare the request
data = {
    "puzzleImageB64": puzzle,
    "pieceImageB64": piece
}

# Get the answer
r = requests.post(puzzle_url, json=data)

print(r.json())
