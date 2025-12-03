import requests

url = "http://127.0.0.1:8000"

payload = {
    "casos": [
        {
            "caso": "15050073916",
            "fecha": "2025-02-04",
            "gestor": "alexander.ramirez.gutierrez@segurosbolivar.com"
        },
        {
            "caso": "15400065439",
            "fecha": "2025-02-05",
            "gestor": "alexander.ramirez.gutierrez@segurosbolivar.com"
        }
    ]
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response JSON:", response.json())
