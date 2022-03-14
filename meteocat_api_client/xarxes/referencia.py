from typing import List
from .base import XarxaBase


class Referencia(XarxaBase):
    """
    Referència

    Tipus d'operacions possibles:
        - Referència
    """

    def comarques(self) -> List[dict]:
        """
        Retorna tota la informació de referència de les comarques de Catalunya.

        Returns:
            List[dict]: [
                            {
                                "codi": 5,
                                "nom": "Alta Ribagorça"
                            },
                            {
                                "codi": 1,
                                "nom": "Alt Camp"
                            },
                            ...
                            {
                                "codi": 41,
                                "nom": "Vallès Oriental"
                            }
                        ]
        """

        recurs = "comarques"
        return self._aconsegueix(recurs)

    def municipis(self) -> List[dict]:
        """
        Retorna tota la informació de referència dels municipis de Catalunya.

        Returns:
            List[dict]: [
                            {
                                "codi": "250019",
                                "nom": "Abella de la Conca",
                                "coordenades": {
                                    "latitud": 42.16239244076299,
                                    "longitud": 1.0928929183862726
                                },
                                "comarca": {
                                    "codi": 25,
                                    "nom": "Pallars Jussà"
                                }
                            },
                            ...
                            {
                                "codi": "430521",
                                "nom": "Xerta",
                                "coordenades": {
                                    "latitud": 40.90796337891453,
                                    "longitud": 0.49184755773298194
                                },
                                "comarca": {
                                    "codi": 9,
                                    "nom": "Baix Ebre"
                                }
                            }
                        ]
        """
        recurs = "municipis"
        return self._aconsegueix(recurs)

    def simbols(self) -> List[dict]:
        """
        Retorna tota la informació de referència dels símbols meteorològics.

        Returns:
            List[dict]: [
                    {
                        "nom": "cel",
                        "descripcio": "estat del cel",
                        "valors": [
                                    {
                                        "codi": "1",
                                        "nom": "Cel ser&egrave;",
                                        "descripcio": "",
                                        "categoria": "nuvolositat",
                                        "icona": "https://.../estatcel/1.svg",
                                        "icona_nit": "https://.../estatcel/1n.svg"
                                    },
                                    ...
                                    ]
                    },
                    ...
                    {
                        "nom": "acumulacio de neu",
                        "descripcio": "acumulació de neu",
                        "valors": [
                                    {
                                        "codi": "1",
                                        "nom": "Inapreciable",
                                        "descripcio": "inferior a 2 cm en 24 hores",
                                        "icona": "https://.../quantitat_1.png",
                                        "icona_nit": ""
                                    },
                                    ...
                                    ]
                    }
                    ]
        """
        recurs = "simbols"
        return self._aconsegueix(recurs)
