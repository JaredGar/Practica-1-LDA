import requests

class SWAPIClient:
    def __init__(self, base_url="https://swapi.dev/api/"):
        self.base_url = base_url

    def get_resource(self, resource):
        url = f"{self.base_url}{resource}/"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener el recurso {resource}: {response.status_code}")
            return None

    def get_person(self, person_id):
        return self.get_resource(f"people/{person_id}")

    def get_film(self, film_id):
        return self.get_resource(f"films/{film_id}")

    # Añade más métodos según los recursos que quieras acceder, como get_planet, get_species, etc.

# Ejemplo de uso:
client = SWAPIClient()
person = client.get_person(1)
print("Información sobre el personaje:")
print(person)
