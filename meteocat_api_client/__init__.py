"""
meteocat-api-client.

Client que consumeix dades de l'API REST del Servei Meteorològic de Catalunya.
"""

__version__ = "0.1.0"
__author__ = "Lluís Herrera"
__credits__ = "Martí Batlles per les tasques de testeig"

from .connexio.connexio import Connexio
from .connexio.memoria_cau import habilita_memoria_cau
from .xarxes.pronostic import Pronostic
from .xarxes.quotes import Quotes
from .xarxes.referencia import Referencia
from .xarxes.xdde import XDDE
from .xarxes.xema import XEMA
