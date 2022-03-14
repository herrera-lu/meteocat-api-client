from typing import Union, List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import neteja_diccionari, genera_info, formateja_valors_data


class CalculMultivariable:
    def calcul_multivariable_x_1_variable_d_totes_estacions_o_1_estacio(
        self, codi_variable: int, any: int, mes: int, dia: int, codi_estacio: str = None
    ) -> Union[dict, List[dict]]:
        """
        Retorna un cálcul multivariable d'una variable per a totes les estacions per una dia determinat, si s'informa el codi de la estació, retorna les dades de la variable per a l'estació sol·licitada.

        Args:
            codi_variable (int): Codi de la variable a consultar.
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD.
            codi_estacio (str, optional): Codi de l'estació a consultar. Per defecte None.

        Returns:
            Union[dict, List[dict]]: [
                                        {
                                            "codi": "CC",
                                            "variables": [
                                                            {
                                                                "codi": 6006,
                                                                "lectures": [
                                                                    {
                                                                        "data": "2020-06-30T00:00Z",
                                                                        "valor": 0,
                                                                        "estat": " ",
                                                                        "baseHoraria": "HO"
                                                                    },
                                                                    {
                                                                        "data": "2020-06-30T01:00Z",
                                                                        "valor": 0,
                                                                        "estat": " ",
                                                                        "baseHoraria": "HO"
                                                                    },
                                                                    ...
                                        {
                                            "codi": "CD",
                                            "variables": [
                                                {
                                                    "codi": 6006,
                                                    "lectures": [
                                                                    {
                                                                        "data": "2020-06-30T00:00Z",
                                                                        "valor": 0,
                                                                        "estat": " ",
                                                                        "baseHoraria": "HO"
                                                                    },
                                                                    {
                                                                        "data": "2020-06-30T01:00Z",
                                                                        "valor": 0,
                                                                        "estat": " ",
                                                                        "baseHoraria": "HO"
                                                                    },
                                                                    ...
                                                                    {
                                                                        "data": "2020-06-30T21:00Z",
                                                                        "valor": 0,
                                                                        "estat": " ",
                                                                        "baseHoraria": "HO"
                                                                    },
                                                                    {
                                                                        "data": "2020-06-30T22:00Z",
                                                                        "valor": 0,
                                                                        "estat": " ",
                                                                        "baseHoraria": "HO"
                                                                    }
                                                                ]
                                                }
                                            ]
                                        }
                                    ]
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"variables/cmv/{codi_variable}/{any}/{mes}/{dia}"
        if codi_estacio:
            params = {"codiEstacio": codi_estacio}
        else:
            params = None
        return self._aconsegueix(recurs, params)

    def calcul_multivariable_metadades_x_totes_variables_d_1_estacio(
        self, codi_estacio: str
    ) -> List[dict]:
        """
        Retorna les metadades de totes les variables de l'estació especificada.

        Args:
            codi_estacio (str, optional): Codi de l'estació a consultar.

        Returns:
            List[dict]: [
                            {
                                "codi": 6006,
                                "nom": "Evapotranspiració de referència",
                                "unitat": "mm",
                                "acronim": "ETo",
                                "tipus": "CMV",
                                "decimals": 2,
                                "basesTemporals": [
                                {
                                    "codi": "HO",
                                    "dataInici": "1993-04-29T00:00Z",
                                    "dataFi": null
                                }
                                ]
                            }
                        ]
        """
        recurs = f"estacions/{codi_estacio}/variables/cmv/metadades"
        return self._aconsegueix(recurs)

    def calcul_multivariable_metadades_x_1_variable_d_1_estacio(
        self, codi_estacio: str, codi_variable: int
    ) -> dict:
        """
        Retorna les metadades d'una variable de l'estació especificada.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: {
                    "codi": 6006,
                    "nom": "Evapotranspiració de referència",
                    "unitat": "mm",
                    "acronim": "ETo",
                    "tipus": "CMV",
                    "decimals": 2,
                    "basesTemporals": [
                        {
                        "codi": "HO",
                        "dataInici": "1992-05-11T17:30Z",
                        "dataFi": null
                        }
                    ]
                }
        """
        recurs = f"estacions/{codi_estacio}/variables/cmv/{codi_variable}/metadades"
        return self._aconsegueix(recurs)

    def calcul_multivariable_metadades_x_totes_variables(self) -> List[dict]:
        """
        Retorna les metadades de totes les variables independentment de les estacions en les que es mesurin.

        Returns:
            List[dict]: [
                            {
                                "codi": 6006,
                                "nom": "Evapotranspiració de referència",
                                "unitat": "mm",
                                "acronim": "ETo",
                                "tipus": "CMV",
                                "decimals": 2
                            }
                        ]
        """
        recurs = "variables/cmv/metadades"
        return self._aconsegueix(recurs)

    def calcul_multivariable_metadades_x_1_variable(self, codi_variable: int) -> dict:
        """
        Retorna les metadades d'una variable independentment de les estacions en les que es mesuri.

        Args:
            codi_variable (int): Codi de la variable a consultar.

        Returns:
            dict: {
                    "codi": 6006,
                    "nom": "Evapotranspiració de referència",
                    "unitat": "mm",
                    "acronim": "ETo",
                    "tipus": "CMV",
                    "decimals": 2
                }
        """
        recurs = f"variables/cmv/{codi_variable}/metadades"
        return self._aconsegueix(recurs)
