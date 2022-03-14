from typing import List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import neteja_diccionari, genera_info


class Estacions:
    def estacions_metadades_x_1_estacio(self, codi_estacio: str) -> List[dict]:
        # TODO: Validar codi localment
        """
        Retorna les metadades de l'estació especificada.

        Args:
            codi_estacio (str): Codi identificatiu de l'estació meteorològica que es vol consultar.

        Returns:
            List[dict]: [
                            {
                                "codi": "UG",
                                "nom": "Viladecans",
                                "tipus": "A",
                                "coordenades": {
                                    "latitud": 41.3003497898,
                                    "longitud": 2.03904453099
                                },
                                "emplacament": "Planters Gusi, ctra. antiga de València, km 14",
                                "altitud": 3,
                                "municipi": {
                                    "codi": "083015",
                                    "nom": "Viladecans"
                                },
                                "comarca": {
                                    "codi": 11,
                                    "nom": "Baix Llobregat"
                                },
                                "provincia": {
                                    "codi": 8,
                                    "nom": "Barcelona"
                                },
                                "xarxa": {
                                    "codi": 1,
                                    "nom": "XEMA"
                                },
                                "estats": [
                                    {
                                        "codi": 2,
                                        "dataInici": "1993-04-29T00:00Z",
                                        "dataFi": null
                                    }
                                ]
                            }
                        ]
        """
        recurs = f"estacions/{codi_estacio}/metadades"
        return self._aconsegueix(recurs)

    def estacions_metadades(self, estat: str = None, data: str = None) -> List[dict]:
        # TODO: Convertir data a objecte datetime
        # TODO: Validar data i estat
        # TODO: Si no s'informa la data, fer servir la data actual
        """
        Retorna una llista de metadades de totes les estacions. Si s'especifiquen els paràmetres, filtra per estat i data especificada.

        Args:
            estat (str, optional): Data a consultar en què les estacions estaven segons l'estat indicat. yyyy-MM-DDZ. Per defecte None.
            data (str, optional): Estat de l'estació. Possibles valors: [ope, des, bte]. Per defecte None.

        Raises:
            MeteocatLocalError: Tracta localment errors en les peticions, abans d'executar la consulta a l'API del Meteocat.
        Returns:
            List[dict]: [
                            {
                                "codi": "CC",
                                "nom": "Orís",
                                "tipus": "A",
                                "coordenades": {
                                "latitud": 42.075052799,
                                "longitud": 2.20980884646
                                },
                                "emplacament": "Abocador comarcal",
                                "altitud": 626,
                                "municipi": {
                                "codi": "081509",
                                "nom": "Orís"
                                },
                                "comarca": {
                                "codi": 24,
                                "nom": "Osona"
                                },
                                "provincia": {
                                "codi": 8,
                                "nom": "Barcelona"
                                },
                                "xarxa": {
                                "codi": 1,
                                "nom": "XEMA"
                                },
                                "estats": [
                                {
                                    "codi": 2,
                                    "dataInici": "1995-11-15T10:00Z",
                                    "dataFi": null
                                }
                                ]
                            },
                            ...
                            {
                                "codi": "Z9",
                                "nom": "Cadí Nord (2.143 m) - Prat d'Aguiló",
                                "tipus": "A",
                                "coordenades": {
                                "latitud": 42.2944985154999,
                                "longitud": 1.716072258350664
                                },
                                "emplacament": "Cadí Nord - Prat d'Aguiló",
                                "altitud": 2143,
                                "municipi": {
                                "codi": "251399",
                                "nom": "Montellà i Martinet"
                                },
                                "comarca": {
                                "codi": 15,
                                "nom": "Cerdanya"
                                },
                                "provincia": {
                                "codi": 25,
                                "nom": "Lleida"
                                },
                                "xarxa": {
                                "codi": 1,
                                "nom": "XEMA"
                                },
                                "estats": [
                                {
                                    "codi": 2,
                                    "dataInici": "2003-11-06T13:00Z",
                                    "dataFi": null
                                }
                                ]
                            }
                        ]
        """

        recurs = "estacions/metadades"
        params = None
        if (estat and not data) or (not estat and data):
            codi_error = 400
            missatge_error = "Falta l'estat o la data"
            params = neteja_diccionari(locals(), "self", "recurs")
            info = genera_info(
                self.__class__.__name__, self.estacions_metadades.__name__, params
            )
            raise MeteocatLocalError(codi_error, missatge_error, info)
        else:
            if estat and data:
                params = neteja_diccionari(locals(), "self")
        return self._aconsegueix(recurs, params)
