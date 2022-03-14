from typing import List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import formateja_valors_data, neteja_diccionari, genera_info


class Prediccio:
    def prediccio_catalunya_general(self, any: int, mes: int, dia: int) -> dict:
        """
        Retorna la predicció general de Catalunya per una dia determinat.

        Args:
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD.

        Returns:
            dict: {
                    "mati": {
                        "tendencies": [
                            {
                                "tipus": "tn",
                                "valor": 1
                            }
                        ],
                        "simbols": {
                            "estatDelCel": [
                                {
                                    "codi": 27,
                                    "coordenades": {
                                        "latitud": 42.68024961503846,
                                        "longitud": 0.8227643647956288
                                    }
                                }
                                ...
                            ],
                            "estatDelMar": [
                                {
                                    "codi": 52,
                                    "coordenades": {
                                        "latitud": 41.121699365079195,
                                        "longitud": 2.025928330418826
                                    }
                                }
                                ...
                            ],
                            "vent": [
                                {
                                    "direccio": 315,
                                    "velocitat": "10",
                                    "beaufort": "2/4",
                                    "coordenades": {
                                        "latitud": 41.014236440808624,
                                        "longitud": 1.7366308344546486
                                    }
                                }
                                ...
                            ]
                        }
                    },
                    "tarda": {
                        "tendencies": [
                            {
                                "tipus": "tx",
                                "valor": 1
                            }
                        ],
                        "simbols": {
                            "estatDelCel": [
                                {
                                    "codi": 3,
                                    "coordenades": {
                                        "latitud": 42.30439930123673,
                                        "longitud": 2.8907454221874413
                                    }
                                }
                                ...
                            ],
                            "estatDelMar": [
                                {
                                    "codi": 52,
                                    "coordenades": {
                                        "latitud": 41.433843423794386,
                                        "longitud": 2.687289078660136
                                    }
                                }
                                ...
                            ],
                            "vent": [
                                {
                                    "direccio": 0,
                                    "velocitat": "20",
                                    "beaufort": "3/5",
                                    "coordenades": {
                                        "latitud": 42.24314165722838,
                                        "longitud": 3.409668992379804
                                    }
                                }
                                ...
                            ]
                        }
                    },
                    "variables": {
                        "estatDelCel": "Al llarg del matí la nuvolositat ...",
                        "precipitacions": "A punts del quadrant nord-est ...",
                        "temperatures": "Les màximes seran semblants ...",
                        "visibilitat": "Entre bona i regular en general ...",
                        "vent": "Bufarà de component nord entre fluix i ..."
                    }
                }
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"catalunya/{any}/{mes}/{dia}"
        return self._aconsegueix(recurs)

    def prediccio_comarcal(self, any: int, mes: int, dia: int) -> dict:
        """
        Retorna la predicció comarcal de Catalunya per una dia determinat.

        Args:
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD.

        Returns:
            dict: {
                    "mati": {
                        "cel": [
                            {
                                "idComarca": 1,
                                "simbol": 2
                            },
                            ...
                            {
                                "idComarca": 41,
                                "simbol": 2
                            }
                        ],
                        "calamarsa": [
                            {
                                "idComarca": 1,
                                "nivell": 1
                            },
                            ...
                            {
                                "idComarca": 41,
                                "nivell": 1
                            }
                        ],
                        "precipitacio": [
                            {
                                "idComarca": 1,
                                "probabilitat": 1,
                                "intensitat": null,
                                "acumulacio": null
                            },
                            ...
                            {
                                "idComarca": 41,
                                "probabilitat": 1,
                                "intensitat": null,
                                "acumulacio": null
                            }
                        ]
                    },
                    "tarda": {
                        "cel": [
                            {
                                "idComarca": 18,
                                "simbol": 21
                            },
                            ...
                            {
                                "idComarca": 41,
                                "simbol": 2
                            }
                        ],
                        "calamarsa": [
                            {
                                "idComarca": 1,
                                "nivell": 1
                            },
                            ...
                            {
                                "idComarca": 41,
                                "nivell": 1
                            }
                        ],
                        "precipitacio": [
                            {
                                "idComarca": 1,
                                "probabilitat": 1,
                                "intensitat": null,
                                "acumulacio": null
                            },
                            ...
                            {
                                "idComarca": 41,
                                "probabilitat": 1,
                                "intensitat": null,
                                "acumulacio": null
                            }
                        ]
                    },
                    "maximes": [
                        {
                            "idComarca": 1,
                            "temperatura": 12
                        },
                        ...
                        {
                            "idComarca": 41,
                            "temperatura": 14
                        }
                    ],
                    "minimes": [
                        {
                            "idComarca": 1,
                            "temperatura": 3
                        },
                        ...
                        {
                            "idComarca": 41,
                            "temperatura": 0
                        }
                    ]
                }
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"comarcal/{any}/{mes}/{dia}"
        return self._aconsegueix(recurs)

    def prediccio_municipal_horaria_a_72_hores(self, codi_municipi: str) -> dict:
        """
        Retorna la predicció del municipi hora a hora a 72 hores vista.

        Args:
            codi_municipi (str): Codi del municipi a consultar.

        Returns:
            dict: {
                    "codiMunicipi": "250019",
                    "dies": [
                    {
                        "data": "2020-08-20Z",
                        "variables": {
                            "temp": {
                                "unitat": "°C",
                                "valors": [
                                    {
                                        "valor": "16.9",
                                        "data": "2020-08-20T00:00Z"
                                    },
                                    {
                                        "valor": "17.6",
                                        "data": "2020-08-20T01:00Z"
                                    },
                                    ...
                        "precipitacio": {
                                "unitat": "mm",
                                "valor": [
                                    {
                                        "valor": "0.0",
                                        "data": "2020-08-20T00:00Z"
                                    },
                                    {
                                        "valor": "0.0",
                                        "data": "2020-08-20T01:00Z"
                                    },
                                    ...
                                    {
                                        "valor": "60.5",
                                        "data": "2020-08-22T22:00Z"
                                    },
                                    {
                                        "valor": "62.4",
                                        "data": "2020-08-22T23:00Z"
                                    }
                                ]
                            }
                        }
                    }
                ]
            }
        """
        recurs = f"municipalHoraria/{codi_municipi}"
        return self._aconsegueix(recurs)

    def prediccio_municipal_a_8_dies(self, codi_municipi: str) -> dict:
        """
        Retorna la predicció del municipi indicat pels pròxims 8 dies.

        Args:
            codi_municipi (str): Codi del municipi a consultar.

        Returns:
            dict: {
                    "codiMunicipi": "250019",
                    "dies": [
                        {
                        "data": "2017-04-18Z",
                        "variables": {
                            "tmax": {
                            "unitat": "°C",
                            "valor": 22.5
                            },
                            "tmin": {
                            "unitat": "°C",
                            "valor": 5.6
                            },
                            "precipitacio": {
                            "unitat": "%",
                            "valor": 9.5
                            },
                            "estatCel": {
                            "valor": 1
                            }
                        }
                        },
                        ...
                        {
                        "data": "2017-04-25Z",
                        "variables": {
                            "tmax": {
                            "unitat": "°C",
                            "valor": 22.0
                            },
                            "tmin": {
                            "unitat": "°C",
                            "valor": 5.1
                            },
                            "precipitacio": {
                            "unitat": "%",
                            "valor": 11.9
                            },
                            "estatCel": {
                            "valor": 1
                            }
                        }
                        }
                    ]
            }
        """
        recurs = f"municipal/{codi_municipi}"
        return self._aconsegueix(recurs)
