import requests
from typing import Union, List
from ..excepcions import MeteocatApiError


class Connexio:
    PROTOCOL = "https"
    URL = "api.meteo.cat"
    VERSIO = 1

    @classmethod
    def genera_url(cls, xarxa: str) -> str:
        return f"{Connexio.PROTOCOL}://{Connexio.URL}/{xarxa}/v{Connexio.VERSIO}"

    @classmethod
    def genera_url_recurs(cls, url: str, recurs: str) -> str:
        return f"{url}/{recurs}"

    def __init__(self, key: str):
        self.key = key
        self.headers = {"Content-Type": "application/json", "X-Api-Key": self.key}

    def demana(
        self, xarxa: str, recurs: str, params: dict = None
    ) -> Union[dict, List[dict]]:
        url = Connexio.genera_url(xarxa)
        url_recurs = Connexio.genera_url_recurs(url, recurs)
        resposta = requests.get(url_recurs, headers=self.headers, params=params)
        self._comprovar_resposta(resposta)
        return resposta.json()

    def _comprovar_resposta(self, resposta: requests.models.Response) -> None:
        if resposta.status_code != 200:
            raise MeteocatApiError(resposta)
