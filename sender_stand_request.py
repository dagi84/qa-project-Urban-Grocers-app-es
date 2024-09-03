import configuration
import requests
import data

# Definir la función post_new_user que envía una solicitud POST para crear un nuevo usuario
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=user_body,  # inserta el cuerpo de la solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

# Obtener el token de autorización
def get_token():
    user_response = post_new_user(data.user_body)
    return user_response.json()["authToken"]

# Definir la función para enviar la solicitud POST para crear un kit de productos
def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {auth_token}'
    }
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=headers)