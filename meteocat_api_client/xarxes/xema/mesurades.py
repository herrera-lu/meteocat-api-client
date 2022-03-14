from typing import List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import formateja_valors_data, neteja_diccionari, genera_info


class Mesurades:
    def mesurades_x_1_variable_d_totes_estacions_o_1_estacio(
        self, codi_variable: int, any: int, mes: int, dia: int, codi_estacio: str = None
    ) -> dict:
        """
        Retorna informació d'una variable per a totes les estacions per una dia determinat, si s'informa el codi de la estació, retorna les dades de la variable per a l'estació sol·licitada.

        Args:
            codi_variable (int): Codi de la variable a consultar.
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD. Per defecte None.
            codi_estacio (str, optional): Codi de l'estació a consultar.

        Returns:
            dict: {
                    "codi": 32,
                    "lectures": [
                                    {
                                    "data": "2017-03-27T00:00Z",
                                    "valor": 8.3,
                                    "estat": "V",
                                    "baseHoraria": "SH"
                                    },
                                    ...
                                    {
                                    "data": "2017-03-27T23:30Z",
                                    "valor": 8.5,
                                    "estat": "V",
                                    "baseHoraria": "SH"
                                    }
                                ]
                }
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"variables/mesurades/{codi_variable}/{any}/{mes}/{dia}"
        if codi_estacio:
            params = {"codi_estacio": codi_estacio}
        else:
            params = None
        return self._aconsegueix(recurs, params)

    def mesurades_x_totes_variables_d_1_estacio(
        self, codi_estacio: str, any: int, mes: int, dia: int
    ) -> List[dict]:
        """
        Retorna informació de totes les variables per una estació per una dia determinat.

        Args:
            codi_estacio (str): Codi de l'estació a consultar.
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            dia (int): Dia de consulta en format numèric DD.

        Returns List[dict]: [
                                {
                                    "codi": "CC",
                                    "variables": [
                                        {
                                            "codi": 1,
                                            "lectures": [
                                                            {
                                                                "data": "2020-06-16T00:00Z",
                                                                "dataExtrem": "2020-06-16T00:05Z",
                                                                "valor": 947.3,
                                                                "estat": "V",
                                                                "baseHoraria": "SH"
                                                            },
                                                            ...
                                        {
                                            "codi": 30,
                                            "lectures": [
                                                            {
                                                                "data": "2020-06-16T00:00Z",
                                                                "valor": 0.6,
                                                                "estat": "V",
                                                                "baseHoraria": "SH"
                                                            },
                                                            {
                                                                "data": "2020-06-16T00:30Z",
                                                                "valor": 0.6,
                                                                "estat": "V",
                                                                "baseHoraria": "SH"
                                                            },
                                                            ...
                                                            {
                                                                "data": "2020-06-16T23:00Z",
                                                                "dataExtrem": "2020-06-16T23:00Z",
                                                                "valor": 0,
                                                                "estat": "V",
                                                                "baseHoraria": "SH"
                                                            },
                                                            {
                                                                "data": "2020-06-16T23:30Z",
                                                                "dataExtrem": "2020-06-16T23:30Z",
                                                                "valor": 0,
                                                                "estat": "V",
                                                                "baseHoraria": "SH"
                                                            }
                                                        ]
                                        }
                                    ]
                                }
                            ]
        """
        any, mes, dia = formateja_valors_data(any, mes, dia)
        recurs = f"estacions/mesurades/{codi_estacio}/{any}/{mes}/{dia}"
        return self._aconsegueix(recurs)

    def mesurades_ultimes_dades_x_1_variable_d_totes_estacions_o_1_estacio(
        self, codi_variable: int, codi_estacio: str = None
    ) -> dict:
        """
        Retorna l'última mesura de les últimes 4 hores per totes les estacions d'una variable, filtrada per estació si així s'indica.

        Args:
            codi_variable (int): Codi de la variable a consultar.
            codi_estacio (str, optional): Codi de l'estació a consultar. Per defecte None.

        Returns:
            dict: {
                    "codi": 5,
                    "lectures": [
                                    {
                                    "data": "2017-07-24T09:00Z",
                                    "dataExtrem": "2017-07-24T09:00Z",
                                    "valor": 24.7,
                                    "estat": " ",
                                    "baseHoraria": "SH"
                                    }
                                ]
                }
        """
        recurs = f"variables/mesurades/{codi_variable}/ultimes"
        params = None
        if codi_estacio:
            params = {"codiEstacio": codi_estacio}
        else:
            params = None
        return self._aconsegueix(recurs, params)

    def mesurades_metadades_x_totes_variables_d_1_estacio(
        self, codi_estacio: str, estat: str = None, data: str = None
    ) -> List[dict]:
        # TODO: Utlitizar objecte datetime per la data.
        """
        Retorna les metadades de totes les variables que mesura l'estació amb codi indicat a la URL, filtrades per estat i data si s'especifica.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.
            estat (str, optional): Estat de l'estació. Possibles valors: [ope, des, bte]. Per defecte None.
            data (str, optional): Codi identificatiu de l'estació meteorològica que es vol consultar. Per defecte None.

        Raises:
            MeteocatLocalError: Tracta localment errors en les peticions, abans d'executar la consulta a l'API del Meteocat.

        Returns:
            List[dict]: [
                            {
                                "codi": 3,
                                "nom": "Humitat relativa màxima",
                                "unitat": "%",
                                "acronim": "HRx",
                                "tipus": "DAT",
                                "decimals": 0,
                                "estats": [
                                            {
                                                "codi": 2,
                                                "dataInici": "2009-07-15T09:00Z",
                                                "dataFi": null
                                            }
                                            ],
                                            "basesTemporals": [
                                            {
                                                "codi": "HO",
                                                "dataInici": "2009-07-15T09:00Z",
                                                "dataFi": null
                                            }
                                        ]
                            },
                            ...
                            {
                                "codi": 72,
                                "nom": "Precipitació màxima en 1 minut",
                                "unitat": "mm",
                                "acronim": "PPTx1min",
                                "tipus": "DAT",
                                "decimals": 1,
                                "estats": [
                                            {
                                                "codi": 2,
                                                "dataInici": "2009-07-15T09:00Z",
                                                "dataFi": null
                                            }
                                            ],
                                            "basesTemporals": [
                                            {
                                                "codi": "HO",
                                                "dataInici": "2009-07-15T09:00Z",
                                                "dataFi": null
                                            }
                                        ]
                            }
                        ]
        """
        recurs = f"estacions/{codi_estacio}/variables/mesurades/metadades"
        # TODO: Refactoritzar creant funció utilitzable en tots els casos semblants a aquest.
        params = None
        if (estat and not data) or (not estat and data):
            codi_error = 400
            missatge_error = "Falta l'estat o la data"
            params = neteja_diccionari(locals(), "self", "recurs")
            info = genera_info(
                self.__class__.__name__,
                self.mesurades_metadades_x_totes_variables_d_1_estacio.__name__,
                params,
            )
            raise MeteocatLocalError(codi_error, missatge_error, info)
        else:
            if estat and data:
                params = neteja_diccionari(locals(), "self")
        return self._aconsegueix(recurs, params)

    def mesurades_metadades_x_1_variable_d_1_estacio(
        self, codi_estacio: str, codi_variable: int
    ) -> dict:
        """
        Retorna les metadades de la variable amb el codi indicat a la URL que mesura l'estació amb codi indicat a la URL.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: {
                    "codi": 3,
                    "nom": "Humitat relativa màxima",
                    "unitat": "%",
                    "acronim": "HRx",
                    "tipus": "DAT",
                    "decimals": 0,
                    "estats": [
                                {
                                "codi": 2,
                                "dataInici": "2009-07-15T09:00Z",
                                "dataFi": null
                                }
                            ],
                    "basesTemporals": [
                                        {
                                        "codi": "HO",
                                        "dataInici": "2009-07-15T09:00Z",
                                        "dataFi": null
                                        }
                                    ]
                }
        """
        recurs = (
            f"estacions/{codi_estacio}/variables/mesurades/{codi_variable}/metadades"
        )
        return self._aconsegueix(recurs)

    def mesurades_metadades_x_totes_variables(self) -> List[dict]:
        """
        Retorna les metadades de totes les variables independement de les estacions en les que es mesurin.

        Returns:
            List[dict]: [
                            {
                                "codi": 1,
                                "nom": "Pressió atmosfèrica màxima",
                                "unitat": "hPa",
                                "acronim": "Px",
                                "tipus": "DAT",
                                "decimals": 1
                            },
                            ...
                            {
                                "codi": 97,
                                "nom": "Temperatura superficial del mar",
                                "unitat": "°C",
                                "acronim": "TMAR",
                                "tipus": "DAT",
                                "decimals": 1
                            }
                        ]
        """
        recurs = "variables/mesurades/metadades"
        return self._aconsegueix(recurs)

    def mesurades_metadades_x_1_variable(self, codi_variable: int) -> dict:
        """
        Retorna les metadades de la variable amb codi indicat a la URL, independement de les estacions en les que es mesurin.

        Args:
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: {
                    "codi": 1,
                    "nom": "Pressió atmosfèrica màxima",
                    "unitat": "hPa",
                    "acronim": "Px",
                    "tipus": "DAT",
                    "decimals": 1
                }
        """
        recurs = f"variables/mesurades/{codi_variable}/metadades"
        return self._aconsegueix(recurs)
