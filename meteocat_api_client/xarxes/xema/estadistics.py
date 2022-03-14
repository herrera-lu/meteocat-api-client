from typing import Union, List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import formateja_valors_data, neteja_diccionari, genera_info


class Estadistics:
    def estadistics_anuals_x_1_variable_d_totes_estacions_o_1_estacio(
        self, codi_variable: int, codi_estacio: str = None
    ) -> Union[dict, List[dict]]:
        """
        Retorna els estadístics anuals d'una variable per a totes les estacions, si s'informa el codi de la estació, retorna les dades de la variable per a l'estació sol·licitada.

        Args:
            codi_variable (int): Codi de la variable a consultar.
            codi_estacio (str, optional): Codi de l'estació a consultar. Per defecte None.

        Returns:
            Union[dict, List[dict]]: {
                                        "codi": "UG",
                                        "variables": [
                                                        {
                                                        "codi": 3000,
                                                        "estadistics": [
                                                                            {
                                                                            "data": "1994Z",
                                                                            "valor": 16.3,
                                                                            "percentatge": 100
                                                                            },
                                                                            {
                                                                            "data": "1995Z",
                                                                            "valor": 16.2,
                                                                            "percentatge": 97.5
                                                                            },
                                                                            ...
                                                                            {
                                                                            "data": "2013Z",
                                                                            "valor": 16.2,
                                                                            "percentatge": 100
                                                                            },
                                                                            {
                                                                            "data": "2014Z",
                                                                            "valor": 10,
                                                                            "percentatge": 6.3
                                                                            }
                                                                        ]
                                                        }
                                                    ]
                                        }
        """
        recurs = f"variables/estadistics/anuals/{codi_variable}"
        if codi_estacio:
            params = {"codiEstacio": codi_estacio}
        else:
            params = None
        return self._aconsegueix(recurs, params)

    def estadistics_mensuals_x_1_variable_d_totes_estacions_o_1_estacio(
        self, codi_variable: int, any: int, codi_estacio: str = None
    ) -> Union[dict, List[dict]]:
        """
        Retorna els estadístics mensuals d'una variable per a totes les estacions per un mes concret, si s'informa el codi de la estació, retorna les dades de la variable per a l'estació sol·licitada.

        Args:
            codi_variable (int): Codi de la variable a consultar.
            any (int): Any de consulta en format numèric YYYY.
            codi_estacio (str, optional): Codi de l'estació a consultar. Per defecte None.

        Returns:
            Union[dict, List[dict]]: {
                                        "codi": "UG",
                                        "variables": [
                                                        {
                                                            "codi": 2000,
                                                            "estadistics": [
                                                                                {
                                                                                "data": "2013-01Z",
                                                                                "valor": 9.1,
                                                                                "percentatge": 100
                                                                                },
                                                                                ...
                                                                                {
                                                                                "data": "2013-11Z",
                                                                                "valor": 12.4,
                                                                                "percentatge": 100
                                                                                },
                                                                                {
                                                                                "data": "2013-12Z",
                                                                                "valor": 9.1,
                                                                                "percentatge": 100
                                                                                }
                                                                            ]
                                                        }
                                                    ]
                                        }
        """
        recurs = f"variables/estadistics/mensuals/{codi_variable}"
        params = {"any": any}
        if codi_estacio:
            params = {**params, "codiEstacio": codi_estacio}
        return self._aconsegueix(recurs, params)

    def estadistics_diaris_x_1_variable_d_totes_estacions_o_1_estacio(
        self, codi_variable: int, any: int, mes: int, codi_estacio: str = None
    ) -> Union[dict, List[dict]]:
        """
        Retorna els estadístics diaris d'una variable per a totes les estacions per un mes concret, si s'informa el codi de la estació, retorna les dades de la variable per a l'estació sol·licitada.

        Nota: si la consulta és del mes actual, només retorna dades fins a tres dies anteriors a la data actual (e.g. si la data actual és 22/10/2018 i es consulten els estadístics diaris pel 10/2018, es retornaran dades fins al dia 19/10/2018).

        Args:
            codi_variable (int): Codi de la variable a consultar.
            any (int): Any de consulta en format numèric YYYY.
            mes (int): Mes de consulta en format numèric MM.
            codi_estacio (str, optional): Codi de l'estació a consultar. Per defecte None.

        Returns:
            Union[dict, List[dict]]: {
                                        "codi": "UG",
                                        "variables": [
                                                        {
                                                        "codi": 1000,
                                                        "estadistics": [
                                                                            {
                                                                            "data": "2013-12-01Z",
                                                                            "valor": 8.8,
                                                                            "percentatge": 100
                                                                            },
                                                                            {
                                                                            "data": "2013-12-02Z",
                                                                            "valor": 7.7,
                                                                            "percentatge": 100
                                                                            },
                                                                            ...
                                                                            {
                                                                            "data": "2013-12-30Z",
                                                                            "valor": 6.5,
                                                                            "percentatge": 100
                                                                            },
                                                                            {
                                                                            "data": "2013-12-31Z",
                                                                            "valor": 6.9,
                                                                            "percentatge": 100
                                                                            }
                                                                        ]
                                                        }
                                                    ]
                                    }
        """
        recurs = f"variables/estadistics/mensuals/{codi_variable}"
        any, mes, _ = formateja_valors_data(any, mes)
        params = {"any": any, "mes": mes}
        if codi_estacio:
            params = {**params, "codiEstacio": codi_estacio}
        return self._aconsegueix(recurs, params)

    def estadistics_metadades_anuals_x_totes_variables(self) -> List[dict]:
        """
        Retorna les metadades de les variables dels estadístics anuals.

        Returns:
            List[dict]: [
                            {
                                "codi": 3000,
                                "nom": "Temperatura mitjana anual",
                                "unitat": "°C",
                                "acronim": "TMM",
                                "tipus": "AN",
                                "decimals": 1
                            },
                            ...
                            {
                                "codi": 3601,
                                "nom": "Gruix de neu màxima anual + data",
                                "unitat": "mm",
                                "acronim": "GNEUXX",
                                "tipus": "AN",
                                "decimals": 0
                            }
                        ]
        """
        recurs = "variables/estadistics/anuals/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_anuals_x_1_variable(self, codi_variable: int) -> dict:
        """
        Retorna les metadades dels estadístics anuals per la variable seleccionada.

        Args:
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: {
                    "codi": 3001,
                    "nom": "Pressió atmosfèrica màxima",
                    "unitat": "hPa",
                    "acronim": "Px",
                    "tipus": "DAT",
                    "decimals": 1
                }
        """
        recurs = f"variables/estadistics/anuals/{codi_variable}/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_mensuals_x_totes_variables(self) -> List[dict]:
        """
        Retorna les metadades de les variables dels estadístics mensuals.

        Returns:
            List[dict]: [
                            {
                                "codi": 2000,
                                "nom": "Temperatura mitjana mensual",
                                "unitat": "°C",
                                "acronim": "TMm",
                                "tipus": "EM",
                                "decimals": 1
                            },
                            ...
                            {
                                "codi": 2601,
                                "nom": "Gruix de neu màxim mensual + data",
                                "unitat": "mm",
                                "acronim": "GNEUXx",
                                "tipus": "EM",
                                "decimals": 0
                            }
                        ]
        """
        recurs = "variables/estadistics/mensuals/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_mensuals_x_1_variable(self, codi_variable: int) -> dict:
        """
        Retorna les metadades dels estadístics mensuals per la variable seleccionada.

        Args:
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: {
                    "codi": 2001,
                    "nom": "Pressió atmosfèrica màxima",
                    "unitat": "hPa",
                    "acronim": "Px",
                    "tipus": "DAT",
                    "decimals": 1
                }
        """
        recurs = f"variables/estadistics/mensuals/{codi_variable}/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_diaris_x_totes_variables(self) -> List[dict]:
        """
        Retorna les metadades de les variables dels estadístics diaris.

        Returns:
            List[dict]: [
                            {
                                "codi": 1000,
                                "nom": "Temperatura mitjana diària",
                                "unitat": "°C",
                                "acronim": "TM",
                                "tipus": "AD",
                                "decimals": 1
                            },
                            ...
                            {
                                "codi": 1700,
                                "nom": "Evapotranspiració de referència",
                                "unitat": "mm",
                                "acronim": "ETo",
                                "tipus": "AD",
                                "decimals": 2
                            }
                        ]
        """
        recurs = "variables/estadistics/diaris/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_diaris_x_1_variable(self, codi_variable: int) -> dict:
        """
        Retorna les metadades dels estadístics diaris per la variable seleccionada.

        Args:
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: {
                    "codi": 1001,
                    "nom": "Pressió atmosfèrica màxima",
                    "unitat": "hPa",
                    "acronim": "Px",
                    "tipus": "DAT",
                    "decimals": 1
                }
        """
        recurs = f"variables/estadistics/diaris/{codi_variable}/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_anuals_x_totes_variables_d_1_estacio(
        self, codi_estacio: str
    ) -> List[dict]:
        """
        Retorna les metadades dels estadístics anuals mesurats en una estació concreta.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.

        Returns:
            List[dict]: [
                            {
                                "codi": 3000,
                                "nom": "Temperatura mitjana anual",
                                "unitat": "°C",
                                "acronim": "TMM",
                                "tipus": "AN",
                                "decimals": 1
                            },
                            ...
                            {
                                "codi": 3518,
                                "nom": "Ratxa màxima mitjana anual del vent 10 m",
                                "unitat": "m/s",
                                "acronim": "VVXM10",
                                "tipus": "AN",
                                "decimals": 1
                            }
                        ]
        """
        recurs = f"estacions/{codi_estacio}/variables/estadistics/anuals/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_anuals_x_1_variable_d_1_estacio(
        self, codi_estacio: str, codi_variable: int
    ) -> dict:
        """
        Retorna les metadades dels estadístics anuals d'una variable mesurada en una estació concreta.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: {
                    "codi": 3000,
                    "nom": "Temperatura mitjana anual",
                    "unitat": "°C",
                    "acronim": "TMM",
                    "tipus": "AN",
                    "decimals": 1
                }
        """
        recurs = f"estacions/{codi_estacio}/variables/estadistics/anuals/{codi_variable}/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_mensuals_x_totes_variables_d_1_estacio(
        self, codi_estacio: str
    ) -> List[dict]:
        """
        Retorna les metadades dels estadístics mensuals mesurats en una estació concreta.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.

        Returns:
            List[dict]: [
                            {
                                "codi": 2000,
                                "nom": "Temperatura mitjana mensual",
                                "unitat": "°C",
                                "acronim": "TMm",
                                "tipus": "EM",
                                "decimals": 1
                            },
                            ...
                            {
                                "codi": 2518,
                                "nom": "Ratxa màxima mitjana mensual de vent 10 m",
                                "unitat": "m/s",
                                "acronim": "VVXm10",
                                "tipus": "EM",
                                "decimals": 1
                            }
                        ]
        """
        recurs = f"estacions/{codi_estacio}/variables/estadistics/mensuals/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_mensuals_x_1_variable_d_1_estacio(
        self, codi_estacio: str, codi_variable: int
    ) -> dict:
        """
        Retorna les metadades dels estadístics mensuals d'una variable mesurada en una estació concreta.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: {
                    "codi": 2000,
                    "nom": "Temperatura mitjana mensual",
                    "unitat": "°C",
                    "acronim": "TMm",
                    "tipus": "EM",
                    "decimals": 1
                }
        """
        recurs = f"estacions/{codi_estacio}/variables/estadistics/mensuals/{codi_variable}/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_diaris_x_totes_variables_d_1_estacio(
        self, codi_estacio: str
    ) -> List[dict]:
        """
        Retorna les metadades dels estadístics diaris mesurats en una estació concreta.


        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.

        Returns:
            List[dict]: [
                            {
                                "codi": 1000,
                                "nom": "Temperatura mitjana diària",
                                "unitat": "°C",
                                "acronim": "TM",
                                "tipus": "AD",
                                "decimals": 1
                            },
                            ...
                            {
                                "codi": 1700,
                                "nom": "Evapotranspiració de referència",
                                "unitat": "mm",
                                "acronim": "ETo",
                                "tipus": "AD",
                                "decimals": 2
                            }
                        ]
        """
        recurs = f"estacions/{codi_estacio}/variables/estadistics/diaris/metadades"
        return self._aconsegueix(recurs)

    def estadistics_metadades_diaris_x_1_variable_d_1_estacio(
        self, codi_estacio: str, codi_variable: int
    ) -> dict:
        """
        Retorna les metadades dels estadístics mensuals d'una variable mesurada en una estació concreta.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.
            codi_variable (int): Codi identificatiu de la variable que es vol consultar.

        Returns:
            dict: _description_
        """
        recurs = f"estacions/{codi_estacio}/variables/estadistics/diaris/{codi_variable}/metadades"
        return self._aconsegueix(recurs)
