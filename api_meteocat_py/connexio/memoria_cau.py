from requests_cache import install_cache, DO_NOT_CACHE
from .connexio import Connexio


def habilita_memoria_cau(caducitat_cau: int = 3600) -> None:
    # TODO: Permetre que l'usuari pugui configurar el temps de caducitat
    # TODO: en funció de la xarxa i/o recurs
    # TODO: i on s'emmagatzema la bd de la memòria cau.
    """
    Habilita la memòria cau i configura el temps de caducitat de les dades que
    conté. La consulta de quotes no s'emmagatzema a la memòria cau i les consultes
    de referència s'emmagatzemen durant un dia (86400s).

    Args:
        caducitat_cau(int): Temps de caducitat de les dades de la memòria
                            cau en segons.
                            Valor per defecte = 3600s

    Returns:
        None
    """

    urls_expire_after = {
        Connexio.genera_url("quotes"): DO_NOT_CACHE,
        Connexio.genera_url("referencia"): 60 * 60 * 24,
        "*": caducitat_cau,
    }
    install_cache(
        cache_name="meteocat_cache",
        backend="sqlite",
        urls_expire_after=urls_expire_after,
    )
