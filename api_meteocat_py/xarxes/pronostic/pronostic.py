from ..base import XarxaBase
from .prediccio import Prediccio
from .uvi import UVI
from .pirineu import Pirineu
from .platges import Platges
from .smp import SMP


class Pronostic(
    Prediccio,
    UVI,
    Pirineu,
    Platges,
    SMP,
    XarxaBase,
):
    """
    Predicció

    Tipus d'operacions possibles:
        - Predicció
    """

    pass
