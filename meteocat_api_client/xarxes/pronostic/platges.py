from typing import List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import formateja_valors_data, neteja_diccionari, genera_info


class Platges:
    def platges_prediccio(
        self, slug_platja: str, any: int, mes: int, dia: int
    ) -> dict:
        """
            Retorna la predicció per la platja i el dia indicats.

            Args:
                slug_platja (str): Identificador de la platja.
                any (int): Any de consulta en format numèric YYYY.
                mes (int): Mes de consulta en format numèric MM.
                dia (int): Dia de consulta en format numèric DD.

            Returns:
                dict: {
        "data": "2021-06-14Z",
        "prediccionsHora": [
                                {
                                    "data": "2021-06-14T00:00Z",
                                    "variables": {
                                                    "temperatura": {
                                                        "unitat": "°C",
                                                        "valor": "22.8"
                                                    },
                                                    "humitatRelativa": {
                                                        "unitat": "%",
                                                        "valor": "61.7"
                                                    },
                                                    "velVent": {
                                                        "unitat": "m/s",
                                                        "valor": "1.7"
                                                    },
                                                    "dirVent": {
                                                        "valor": "265.5"
                                                    },
                                                    "estatCel": {
                                                        "valor": 1
                                                    },
                                                    "alturaOna": {
                                                        "unitat": "m",
                                                        "valor": "0.3"
                                                    },
                                                    "direccioOna": {
                                                        "valor": "344.1"
                                                    },
                                                    "temperaturaAigua": {
                                                        "unitat": "ºC",
                                                        "valor": "23.8"
                                                    },
                                                    "uviMax": {
                                                        "valor": 0
                                                    },
                                                    "uviPrevist": {
                                                        "valor": 0
                                                    }
                                                }
                                },
                                {
                                    "data": "2021-06-14T01:00Z",
                                    "variables": {
                                                    "temperatura": {
                                                        "unitat": "°C",
                                                        "valor": "22.0"
                                                    },
                                                    "humitatRelativa": {
                                                        "unitat": "%",
                                                        "valor": "62.4"
                                                    },[ ... ]

                        ]
                        }
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"platges/{slug_platja}/{any}/{mes}/{dia}"
        return self._aconsegueix(recurs)

    def platges_metadades(self) -> List[dict]:
        """
        Retorna les metadades de les platges.

        Returns:
            List[dict]: [
                            {
                                "municipi": "Alcanar",
                                "nom": "del Marjal",
                                "coordenades": {
                                "latitud": 40.54525445,
                                "longitud": 0.524413744
                                },
                                "slug": "alcanar-del-marjal"
                            },
                            ...,
                            {
                                "municipi": "Portbou",
                                "nom": "de Portbou (Gran)",
                                "coordenades": {
                                "latitud": 42.42722691,
                                "longitud": 3.160763223
                                },
                                "slug": "portbou-de-portbou-gran"
                            }
                        ]
        """
        recurs = "platges/metadades"
        return self._aconsegueix(recurs)
