from typing import Union, List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import formateja_valors_data, neteja_diccionari, genera_info


class Auxiliars:
    def auxiliars_x_1_variable_d_1_estacio(
        self, codi_estacio: str, codi_variable: int, any: int, mes: int, dia: int
    ) -> Union[dict, List[dict]]:
        """
        Retorna un cálcul auxiliars d'una variable a una estació per una dia determinat.

        Args:
            codi_variable (int): Codi de l'estació a consultar.
            codi_estacio (str): Codi de la variable a consultar.
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD.
        Returns:
            Union[dict, List[dict]]: [
                                        {
                                            "codi": "CC",
                                            "variables": [
                                            {
                                                "codi": 900,
                                                "lectures": [
                                                {
                                                    "data": "2017-03-10T00:02Z",
                                                    "valor": 0.2,
                                                    "estat": "V",
                                                    "baseHoraria": "MI"
                                                },
                                                ...
                                                {
                                                    "data": "2017-03-10T23:34Z",
                                                    "valor": 0.2,
                                                    "estat": "V",
                                                    "baseHoraria": "MI"
                                                }
                                                ]
                                            }
                                            ]
                                        }
                                    ]
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"variables/auxiliars/{codi_variable}/{any}/{mes}/{dia}"
        params = {"codiEstacio": codi_estacio}
        return self._aconsegueix(recurs, params)

    def auxiliars_metadades_x_totes_variables_d_1_estacio(
        self, codi_estacio: str, data: str = None, estat: str = None
    ) -> List[dict]:
        # TODO: Utilitzar objecte datetime per la data.
        """
        Retorna les metadades de totes les variables de l'estació especificada, filtrades per estat i data si així s'indica.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.
            data (str, optional): Data a consultar què les variables estaven segons l'estat indicat a consultar. yyyy-MM-DDZ. Per defecte None.
            estat (str, optional): Estat de la variable. Possibles valors: [ope, des, bte]. Per defecte None.

        Raises:
            MeteocatLocalError: Tracta localment errors en les peticions, abans d'executar la consulta a l'API del Meteocat.

        Returns:
            List[dict]: [
                            {
                                "codi": 900,
                                "nom": "Precipitació acumulada en 10 min",
                                "unitat": "mm",
                                "acronim": "PPT10min",
                                "tipus": "AUX",
                                "decimals": 1,
                                "estats": [
                                            {
                                                "codi": 2,
                                                "dataInici": "1993-09-22T00:40Z",
                                                "dataFi": null
                                            }
                                        ],
                                "basesTemporals": [
                                                    {
                                                        "codi": "DM",
                                                        "dataInici": "1993-09-22T00:40Z",
                                                        "dataFi": null
                                                    }
                                                ]
                            },
                            {
                                "codi": 901,
                                "nom": "Precipitació acumulada en 1 min",
                                "unitat": "mm",
                                "acronim": "PPT1min",
                                "tipus": "AUX",
                                "decimals": 1,
                                "estats": [
                                            {
                                                "codi": 2,
                                                "dataInici": "2009-08-25T17:22Z",
                                                "dataFi": null
                                            }
                                        ],
                                "basesTemporals": [
                                                    {
                                                        "codi": "MI",
                                                        "dataInici": "2009-08-25T17:22Z",
                                                        "dataFi": null
                                                    }
                                                ]
                            }
                        ]
        """
        recurs = f"estacions/{codi_estacio}/variables/auxiliars/metadades"
        params = None
        if (estat and not data) or (not estat and data):
            codi_error = 400
            missatge_error = "Falta l'estat o la data"
            params = neteja_diccionari(locals(), "self", "recurs")
            info = genera_info(
                self.__class__.__name__,
                self.auxiliars_metadades_x_totes_variables_d_1_estacio.__name__,
                params,
            )
            raise MeteocatLocalError(codi_error, missatge_error, info)
        else:
            if data and estat:
                params = neteja_diccionari(locals(), "self", "codi_estacio")
        return self._aconsegueix(recurs, params)

    def auxiliars_metadades_x_1_variable_d_1_estacio(
        self, codi_estacio: str, codi_variable: int
    ) -> dict:
        """
        Retorna les metadades d'una variable de l'estació especificada.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: {
                        "codi": 900,
                        "nom": "Precipitació acumulada en 10 min",
                        "unitat": "mm",
                        "acronim": "PPT10min",
                        "tipus": "AUX",
                        "decimals": 1,
                        "estats": [
                                    {
                                    "codi": 2,
                                    "dataInici": "2007-07-01T20:00Z",
                                    "dataFi": null
                                    }
                                ],
                        "basesTemporals": [
                                            {
                                            "codi": "DM",
                                            "dataInici": "2007-07-01T20:00Z",
                                            "dataFi": null
                                            }
                                        ]
                    }
        """
        recurs = (
            f"estacions/{codi_estacio}/variables/auxiliars/{codi_variable}/metadades"
        )
        return self._aconsegueix(recurs)

    def auxiliars_metadades_x_totes_variables(self) -> List[dict]:
        """
        Retorna les metadades de totes les variables independentment de les estacions en les que es mesurin.

        Returns:
            List[dict]: [
                            {
                                "codi": 900,
                                "nom": "Precipitació acumulada en 10 min",
                                "unitat": "mm",
                                "acronim": "PPT10min",
                                "tipus": "AUX",
                                "decimals": 1
                            },
                            {
                                "codi": 901,
                                "nom": "Precipitació acumulada en 1 min",
                                "unitat": "mm",
                                "acronim": "PPT1min",
                                "tipus": "AUX",
                                "decimals": 1
                            }
                        ]
        """
        recurs = "variables/auxiliars/metadades"
        return self._aconsegueix(recurs)

    def auxiliars_metadades_x_1_variable(self, codi_variable: int) -> dict:
        """
        Retorna les metadades d'una variable independentment de les estacions en les que es mesuri.

        Args:
            codi_variable (int): Codi de l'estació a consultar.

        Returns:
            dict: {
                    "codi": 900,
                    "nom": "Precipitació acumulada en 10 min",
                    "unitat": "mm",
                    "acronim": "PPT10min",
                    "tipus": "AUX",
                    "decimals": 1
                }
        """
        recurs = f"variables/auxiliars/{codi_variable}/metadades"
        return self._aconsegueix(recurs)
