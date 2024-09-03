import sender_stand_request
import data

# Función para obtener el cuerpo del kit con un nombre específico
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Función para obtener el token de un nuevo usuario
def get_new_user_token():
    return sender_stand_request.get_token()

# Funciones de aserción positiva y negativa
def positive_assert(kit_body):
    assert "name" in kit_body and isinstance(kit_body["name"], str), "Invalid name in kit_body"

    user_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, user_token)

    if response.status_code != 201:
        print(f"Failed request: {response.status_code}, {response.json()}")

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    user_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, user_token)
    if response.status_code != 400:
        print(f"Failed request: {response.status_code}, {response.json()}")
    assert response.status_code == 400


# Lista de comprobación de pruebas
def test_kit_name_minimum_characters():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)