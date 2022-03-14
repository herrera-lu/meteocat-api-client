from typing import List
from .base import XarxaBase
from ..helpers.utils import formateja_valors_data


class XDDE(XarxaBase):
    """
    Xarxa de Detecció de Descàrregues Elèctriques

    Tipus d'operacions possibles:
        - Descàrregues
    """

    def descarregues_x_tota_catalunya(
        self, any: int, mes: int, dia: int, hora: int
    ) -> List[dict]:
        # TODO: Utilitzar objecte datetime i validar-lo
        """
        Retorna tota la informació de llamps per a la hora especificada.

        Args:
            any (int): Any de consulta en format numèric YYYY
            mes (int): Mes de consulta en format numèric MM
            dia (int): Dia de consulta en format numèric DD
            hora (int): Hora de consulta en format numèric hh
        Returns:
            List[dict]: [
                            {
                                "id": 14861951,
                                "data": "2016-12-16T13:03:28.761993Z",
                                "correntPic": 7.58500004,
                                "chi2": 2.20000005,
                                "ellipse": {
                                "eixMajor": 400,
                                "eixMenor": 200,
                                "angle": 324.299988
                                },
                                "numSensors": 4,
                                "nuvolTerra": true,
                                "coordenades": {
                                "latitud": 40.9807,
                                "longitud": 1.3024377
                                }
                            },
                            ...
                        ]
        """

        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"catalunya/{any}/{mes}/{dia}/{hora}"
        return self._aconsegueix(recurs)

    def descarregues_resum_x_comarques(
        self, codi_comarca: int, any: int, mes: int, dia: int
    ) -> List[dict]:
        # TODO: Utilitzar objecte datetime, validar-lo i validar codi_comarca
        # TODO: abans crida a API
        """
        Retorna tota la informació de llamps per la comarca especificada.

        Args:
            codi_comarca (int): Codi de la comarca a consultar.
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD.

        Returns:
            List[dict]: [
                            {
                                "nom": "Queralbs",
                                "codi": "170433",
                                "descarregues": [
                                                    {
                                                        "tipus": "cg-",
                                                        "recompte": 1
                                                    }
                                                ]
                            },
                            {
                                "nom": "Toses",
                                "codi": "172018",
                                "descarregues": [
                                                    {
                                                        "tipus": "cc",
                                                        "recompte": 11
                                                    }
                                                ]
                            }
                        ]
        """

        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"informes/comarques/{codi_comarca}/{any}/{mes}/{dia}"
        return self._aconsegueix(recurs)
