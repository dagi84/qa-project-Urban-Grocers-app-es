import configuration
import requests
import data

# Definir la función post_new_user que envía una solicitud POST para crear un nuevo usuario
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=user_body,  # inserta el cuerpo de la solicitud
                         headers=data.headers)  # inserta los encabezados

# obtiene el authToken necesario para la autenticación en futuras solicitudes
user_response = post_new_user(data.user_body)
response_json = user_response.json()
auth_token = response_json.get("authToken")

# Definir la función para enviar la solicitud POST para crear un kit
def post_new_kit(new_kit):
    autorizacion = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {auth_token}'
    }
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT,
                         json=new_kit,
                         headers=autorizacion)
