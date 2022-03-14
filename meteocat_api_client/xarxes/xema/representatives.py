from typing import List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import neteja_diccionari, genera_info


class Representatives:
    def representatives_metadades_x_totes_variables(self) -> List[dict]:
        """
        Retorna les metadades de totes les variables amb dades d'estacions representatives.

        Returns:
            List[dict]: [
                            {
                                "codi": 32,
                                "nom": "Temperatura",
                                "unitat": "°C",
                                "acronim": "T",
                                "tipus": "DAT",
                                "decimals": 1
                            }
                        ]
        """
        recurs = "representatives/metadades/variables"
        return self._aconsegueix(recurs)

    def representatives_codis_estacions_x_1_municipi_i_1_variable(
        self, codi_municipi: str, codi_variable: int
    ) -> List[dict]:
        # TODO: Validar codis localment (utilitzar ENUMs)
        """
        Retorna els codis de les estacions representatives per a un municipi i una variable determinats.

        Args:
            codi_municipi (str): Codi del municipi a consultar.
            codi_variable (int): Codi de la variable a consultar.

        Returns:
            List[dict]: [
                            {
                                "codi": "080057",
                                "variables": [
                                                {
                                                    "codi": 32,
                                                    "estacions": [
                                                        {
                                                            "codi": "X9",
                                                            "ordre": 1
                                                        },
                                                        {
                                                            "codi": "XG",
                                                            "ordre": 2
                                                        }
                                                    ]
                                                }
                                            ]
                            }
                        ]
        """

        recurs = f"representatives/metadades/municipis/{codi_municipi}/variables/{codi_variable}"
        return self._aconsegueix(recurs)
