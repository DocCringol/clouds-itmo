from fastapi import FastAPI
import requests
import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI()

CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

@app.get("/random-cat")
async def get_random_cat():
	response = requests.get(CAT_API_URL)
	if response.status_code == 200:
		data = response.json()
		image_url = data[0]["url"]
		html_content = f"""
		<html>
			<body>
				<h1>Random Cat</h1>
				<img src="{image_url}" alt="Random Cat" style="max-width: 100%; height: auto;">
			</body>
		</html>
		"""
		return HTMLResponse(content=html_content)
	return {"error": "Failed to fetch a cat image"}

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8080)