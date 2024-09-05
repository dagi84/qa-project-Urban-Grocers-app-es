# data.py

# Define los encabezados HTTP que se utilizarán en las solicitudes
headers = {
    "Content-Type": "application/json"
}

# Este diccionario contiene los datos necesarios para crear un nuevo usuario
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

#  Este diccionario contiene los datos para definir un kit de productos.
kit_body = {
       "name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }
