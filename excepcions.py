import json
from requests.models import Response


class MeteocatBaseError(Exception):
    """
    Classe de la que hereden la resta d'excepcions i que conté el mètode __str__ que permet representar-les com a string.
    """

    def __str__(self):
        return f"\n- Codi d'error: {self.codi_error}\n- Descripció de l'error:\n{json.dumps(self.descripcio_error, indent=4)}"


class MeteocatApiError(MeteocatBaseError):
    """
    Tracta les respostes amb error de l'API del Meteocat.
    """

    def __init__(self, resposta: Response):
        self.codi_error = resposta.status_code
        self.descripcio_error = resposta.json()


class MeteocatLocalError(MeteocatBaseError):
    """
    Tracta localment errors en les peticions, abans d'executar la consulta a l'API del Meteocat.
    """

    def __init__(self, codi_error: int, missatge: str, info: dict):
        self.codi_error = codi_error
        self.descripcio_error = {"message": missatge, "local": info}
