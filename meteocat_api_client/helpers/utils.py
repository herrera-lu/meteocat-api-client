from typing import List
from ..excepcions import MeteocatLocalError


def neteja_diccionari(diccionari: dict, *args: List[dict]) -> dict:
    """
    Treu les claus *args d'un diccionari i retorna el resultat.

    Args:
        diccionari (dict): Diccionari d'entrada

    Returns:
        dict: Diccionari sense les claus *args
    """

    for key in args:
        diccionari.pop(key, None)

    return diccionari


def genera_info(nom_classe: str, nom_funcio: str, params: dict) -> dict:
    """
    Retorna diccionari amb informació per depurar errors.

    Args:
        nom_classe (str): Nom de la classe.
        nom_funcio (str): Nom de la funció.
        params (dict): Paràmetres.

    Returns:
        dict: Diccionari amb informació per depurar errors.
    """

    info = {"className": nom_classe, "functionName": nom_funcio, "params": params}
    return info


def formateja_valor(valor: int, num_digits: int, nom_valor: str) -> str:
    # TODO: A banda de validar el format del valor, s'hauria de validar
    # TODO: que el valor està dins del rang admissible.
    try:
        valor = str(int(valor)).zfill(num_digits)
        if len(valor) == num_digits:
            return valor
        else:
            codi_error = 400
            missatge_error = f"{nom_valor} incorrecte!"
            params = {nom_valor: valor}
            info = genera_info(
                "",
                formateja_valor.__name__,
                params,
            )
            raise MeteocatLocalError(codi_error, missatge_error, info)

    except ValueError:
        codi_error = 400
        missatge_error = f"{nom_valor} incorrecte!"
        params = {nom_valor: valor}
        info = genera_info(
            "",
            formateja_valor.__name__,
            params,
        )
        raise MeteocatLocalError(codi_error, missatge_error, info)


def formateja_valors_data(any=None, mes=None, dia=None):
    if any:
        any = formateja_valor(any, 4, "Dia")
    if mes:
        mes = formateja_valor(mes, 2, "Mes")
    if dia:
        dia = formateja_valor(dia, 2, "Dia")

    return any, mes, dia
