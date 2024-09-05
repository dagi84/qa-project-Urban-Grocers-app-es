import sender_stand_request
import data

# Función para obtener el cuerpo del kit con un nombre específico
def get_kit_body(name):
    current_user_body = data.kit_body.copy()
    current_user_body["name"] = name
    return current_user_body

# Funciones de aserción positiva y negativa
def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_body['name']

def negative_assert(kit_body):
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 400

# Lista de comprobación de pruebas
# test 1 Verifica que un nombre con 1 carácter sea aceptado
def test_kit_name_minimum_characters():
    kit_body = get_kit_body("a")
    # Pasar auth_token a la función de aserción
    positive_assert(kit_body)

# test 2 Verifica que un nombre con el máximo permitido de 511 caracteres sea aceptado
def test_kit_name_maximum_characters():
    kit_body = get_kit_body("Abcd" * 127 + "abC")
    positive_assert(kit_body)

# test 3 Verifica que un nombre vacío genere un error
def test_kit_name_below_minimum_characters():
    kit_body = get_kit_body("")
    negative_assert(kit_body)

# test 4 Verifica que un nombre con más de 511 caracteres genere un error
def test_kit_name_above_maximum_characters():
    kit_body = get_kit_body("Abcd" * 128 + "abcD")
    positive_assert(kit_body)

# test 5 Verifica que un nombre con caracteres especiales sea aceptado.
def test_kit_name_special_characters():
    kit_body = get_kit_body("$@/&%$")
    positive_assert(kit_body)

# test 6 Verifica que un nombre con espacios sea aceptado.
def test_kit_name_with_spaces():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

# test 7 Verifica que al no pasar el campo name se genere un error.
def test_kit_name_not_passed():
    kit_body = data.kit_body.copy()
    kit_body.pop("name", None)
    negative_assert(kit_body)

# test 8 Verifica que un nombre numérico genere un error
def test_kit_name_as_number():
    kit_body = get_kit_body(123456)
    negative_assert(kit_body)


