from typing import List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import formateja_valors_data, neteja_diccionari, genera_info


class UVI:
    def uvi_prediccio_municipal(self, codi_municipi: str) -> dict:
        """
        Retorna la predicció de l'Índex Ultraviolat (UVI) per al municipi indicat per als pròxims 3 dies.

        Args:
            codi_municipi (str): Codi del municipi a consultar.

        Returns:
            dict: {
                    "ine": "080018",
                    "nom": "Abrera",
                    "comarca": 11,
                    "capital": false,
                    "uvi": [
                        {
                            "date": "2018-10-18",
                            "hours": [
                                {
                                    "hour": 0,
                                    "uvi": 0,
                                    "uvi_clouds": 0
                                },
                                ...
                                {
                                    "hour": 23,
                                    "uvi": 0,
                                    "uvi_clouds": 0
                                }
                            ]
                        },
                        {
                            "date": "2018-10-19",
                            "hours": [
                                {
                                    "hour": 0,
                                    "uvi": 2,
                                    "uvi_clouds": 1
                                },
                                ...
                                {
                                    "hour": 23,
                                    "uvi": 0,
                                    "uvi_clouds": 0
                                }
                            ]
                        },
                        {
                            "date": "2018-10-20",
                            "hours": [
                                {
                                    "hour": 0,
                                    "uvi": 0,
                                    "uvi_clouds": 0
                                },
                                ...
                                {
                                    "hour": 23,
                                    "uvi": 0,
                                    "uvi_clouds": 0
                                }
                            ]
                        }
                    ]
                }
            }
        """
        recurs = f"uvi/{codi_municipi}"
        return self._aconsegueix(recurs)
