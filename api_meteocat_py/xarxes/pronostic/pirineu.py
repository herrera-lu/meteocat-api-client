from typing import List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import formateja_valors_data, neteja_diccionari, genera_info

class Pirineu:
    def pirineu_pics_prediccio(self, slug_pic:str, any:int, mes:int, dia:int) -> List[dict]:
        """
        Retorna la predicció pel pic i el dia indicats.

        Args:
            slug_pic (str): Identificador del pic.
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD.

        Returns:
            List[dict]: [
                            {
                                "data": "2017-04-20T00:00Z",
                                "cotes": [
                                {
                                    "cota": "totes",
                                    "variables": [
                                    {
                                        "nom": "isozero",
                                        "valor": 1800
                                    },
                                    {
                                        "nom": "iso-10",
                                        "valor": 3700
                                    }
                                    ] 
                                },
                                {
                                    "cota": "1500",
                                    "variables": [
                                    {
                                        "nom": "humitat",
                                        "valor": 35
                                    },
                                    {
                                        "nom": "temperatura",
                                        "valor": 1
                                    },
                                    {
                                        "nom": "direccio vent",
                                        "valor": 356
                                    },
                                    {
                                        "nom": "velocitat vent",
                                        "valor": 43
                                    }
                                    ]
                                },
                                ...
                                {
                                    "cota": "3000",
                                    "variables": [ ... ]
                                }
                                ]
                            },
                            {
                                "data": "2017-04-20T03:00Z",
                                "cotes": [ ... ]
                            }
                            ]
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"pirineu/pics/{slug_pic}/{any}/{mes}/{dia}"
        return self._aconsegueix(recurs)

    def pirineu_pics_metadades(self) -> List[dict]:
        """
        Retorna les metadades dels pics del Pirineu.

        Returns:
            List[dict]: [
                            {
                                "codi": "5a69e26b",
                                "descripcio": "Pic de Montlude",
                                "coordenades": {
                                "latitud": 42.785239999990075,
                                "longitud": 0.7587399999918127
                                },
                                "slug": "pic-de-montlude",
                                "tipus": "Pics"
                            },
                            ...
                            {
                                "codi": "c82a286f",
                                "descripcio": "Pics de Bassiero",
                                "coordenades": {
                                "latitud": 42.60669999999494,
                                "longitud": 0.9953999999953725
                                },
                                "slug": "pics-de-bassiero",
                                "tipus": "Pics"
                            }
                        ]
        """
        recurs = "pirineu/pics/metadades"
        return self._aconsegueix(recurs)

    def pirineu_refugis_prediccio(self, slug_refugi:str, any:int, mes:int, dia:int ) -> List[dict]:
        """
        Retorna la predicció pel refugi i el dia indicats.

        Args:
            slug_refugi (str): Identificador del refugi.
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD.

        Returns:
            List[dict]: [
                            {
                                "data": "2017-04-20T00:00Z",
                                "cotes": [
                                {
                                    "cota": "totes",
                                    "variables": [
                                    {
                                        "nom": "isozero",
                                        "valor": 1800
                                    },
                                    {
                                        "nom": "iso-10",
                                        "valor": 3700
                                    }
                                    ] 
                                },
                                {
                                    "cota": "1500",
                                    "variables": [
                                    {
                                        "nom": "humitat",
                                        "valor": 35
                                    },
                                    {
                                        "nom": "temperatura",
                                        "valor": 1
                                    },
                                    {
                                        "nom": "direccio vent",
                                        "valor": 356
                                    },
                                    {
                                        "nom": "velocitat vent",
                                        "valor": 43
                                    }
                                    ]
                                },
                                ...
                                {
                                    "cota": "3000",
                                    "variables": [ ... ]
                                }
                                ]
                            },
                            {
                                "data": "2017-04-20T03:00Z",
                                "cotes": [ ... ]
                            }
                        ]
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"pirineu/refugis/{slug_refugi}/{any}/{mes}/{dia}"
        return self._aconsegueix(recurs)

    def pirineu_refugis_metadades(self)-> List[dict]:
        """
        Retorna les metadades dels refugis del Pirineu.

        Returns:
            List[dict]: [
                            {
                                "codi": "9cc1a507",
                                "descripcio": "Refugi Colomina",
                                "coordenades": {
                                "latitud": 42.51942999999505,
                                "longitud": 1.0012399999954205
                                },
                                "slug": "refugi-colomina",
                                "tipus": "Refugis"
                            },
                            ...
                            {
                                "codi": "64710fe2",
                                "descripcio": "Refugi Gall Fer (Bosc de Virós)",
                                "coordenades": {
                                "latitud": 42.52749999999814,
                                "longitud": 1.3027779999980433
                                },
                                "slug": "refugi-gall-fer-bosc-de-viros",
                                "tipus": "Refugis"
                            }
                        ]
        """
        recurs = f"pirineu/refugis/metadades"
        return self._aconsegueix(recurs)

    def pirineu_zones_prediccio(self, any:int, mes:int, dia:int) -> dict:
        """
        Retorna la predicció per zones del Pirineu el dia indicat.

        Args:
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD.

        Returns:
            dict: {
                    "dataPrediccio": "2017-04-19Z",
                    "dataPublicacio": "2017-04-17T13:57Z",
                    "franjes": [
                        {
                        "idTipusFranja": 2,
                        "nom": "06:00 - 12:00h",
                        "zones": [
                            {
                            "variablesValors": [
                                {
                                "nom": "comentari",
                                "periode": 2
                                },
                                {
                                "nom": "intensitat",
                                "periode": 1
                                },
                                {
                                "nom": "tempesta",
                                "valor": "1",
                                "periode": 1
                                },
                                {
                                "nom": "acumulacioNeu",
                                "periode": 2
                                },
                                {
                                "nom": "acumulacio",
                                "periode": 2
                                },
                                {
                                "nom": "visibilitat",
                                "valor": "2",
                                "periode": 1
                                },
                                {
                                "nom": "cota",
                                "periode": 1
                                },
                                {
                                "nom": "cel",
                                "valor": "2",
                                "periode": 1
                                },
                                {
                                "nom": "probabilitat",
                                "valor": "1",
                                "periode": 1
                                }
                            ], 
                            "nom": "Pirineu oriental",
                            "idZona": 4
                            },
                            ...
                            {
                            "variablesValors": [ ... ],
                            "nom": "Vessant nord Pirineu orie",
                            "idZona": 3
                            }
                        ]
                        },
                        ...
                        {
                        "idTipusFranja": 1,
                        "nom": "00:00h - 06:00h",
                        "zones": [ ... ]
                        }
                    ]
                }
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"pirineu/{any}/{mes}/{dia}"
        return self._aconsegueix(recurs)