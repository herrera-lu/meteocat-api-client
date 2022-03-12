from ..base import XarxaBase
from .auxiliars import Auxiliars
from .estadistics import Estadistics
from .calcul_multivariable import CalculMultivariable
from .estacions import Estacions
from .mesurades import Mesurades
from .representatives import Representatives


class XEMA(
    Auxiliars,
    CalculMultivariable,
    Estacions,
    Estadistics,
    Mesurades,
    Representatives,
    XarxaBase,
):
    """
    Xarxa d'Estacions Meteorològiques Automàtiques

    Tipus d'operacions possibles:
        - Representatives
        - Estacions
        - Mesurades
        - Estadístics
        - Càlcul multivariable
        - Auxiliars
    """

    pass
