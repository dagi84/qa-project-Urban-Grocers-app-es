import configuration
import requests
import data

# Definir la función post_new_user que envía una solicitud POST para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de la solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def get_token():
    user_response = post_new_user(data.user_body)
    return user_response.json()["authToken"]

authorization = get_token()
header_auto = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer [authorization_   Token]'
}

def post_product_kits(product_kit):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=product_kit,
                         headers=header_auto)

response = post_product_kits(data.product_kit)
print(response.status_code)
print(response.json())
