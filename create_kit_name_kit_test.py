import sender_stand_request
import data


# Función para obtener un token de usuario
def get_new_user_token():
    return get_token()

# Funciones de aserción positiva y negativa
def positive_assert(kit_body, auth_token):
    response = post_product_kits(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    response = post_product_kits(kit_body, auth_token)
    assert response.status_code == 400

# Pruebas
def test_create_kit_with_1_char():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("a")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_511_chars():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("a" * 511)
    positive_assert(kit_body, auth_token)

def test_create_kit_with_0_chars():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_with_512_chars():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("a" * 512)
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_with_special_chars():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("!@#$%^&*()")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_spaces():
    auth_token = get_new_user_token()
    kit_body = get_kit_body(" A Kit Name ")
    positive_assert(kit_body, auth_token)