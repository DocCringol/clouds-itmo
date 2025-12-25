from fastapi import FastAPI
import requests
import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI()

DOG_API_URL = "https://api.thedogapi.com/v1/images/search"

@app.get("/random-dog")
async def get_random_dog():
	response = requests.get(DOG_API_URL)
	if response.status_code == 200:
		data = response.json()
		image_url = data[0]["url"]
		html_content = f"""
		<html>
			<body>
				<h1>Random Dog</h1>
				<img src="{image_url}" alt="Random Dog" style="max-width: 100%; height: auto;">
			</body>
		</html>
		"""
		return HTMLResponse(content=html_content)
	return {"error": "Failed to fetch a dog image"}

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8080)