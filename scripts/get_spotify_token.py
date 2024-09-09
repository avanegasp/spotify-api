import requests
import base64

client_id ='545902691fc74d87bc0a692ee6b44dd4'
client_secret = '9c9750951d244b2385d21b9441af07d6'

# Codificar las credenciales en base64
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# Encabezados para la solicitud
headers = {
    'Authorization': f'Basic {encoded_credentials}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Datos de la solicitud
data = {
    'grant_type':'client_credentials'
}

# Hacer la solicitud POST para obtener el token
response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
access_token = response.json().get('access_token')

print("Access Token", access_token)