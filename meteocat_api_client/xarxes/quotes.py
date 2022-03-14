from .base import XarxaBase


class Quotes(XarxaBase):
    """
    Quotes

    Tipus d'operacions possibles:
        - Quotes
    """

    def consum_actual(self) -> dict:
        """
        Retorna el consum actual dels diferents plans contractats.

        Returns:
            dict: {
                    "client": {
                        "nom": "Client1",
                        "apiKey": "xx...xxx"
                    },
                    "plans": [
                                {
                                "nom": "Quotes"
                                },
                                {
                                "nom": "Referencia Bàsic",
                                "periode": "Mensual",
                                "maxConsultes": 1000,
                                "consultesRestants": 982,
                                "consultesRealitzades": 18
                                }
                            ]
                    }
        """
        recurs = "consum-actual"
        return self._aconsegueix(recurs)
