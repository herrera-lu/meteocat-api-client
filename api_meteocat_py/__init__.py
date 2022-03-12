"""
api-meteocat-py.

Client que consumeix dades de l'API REST del Servei Meteorològic de Catalunya.
"""

__version__ = "0.1.0"
__author__ = "Lluís Herrera"
__credits__ = "Martí Batlles per les tasques de testeig"

from .connexio import Connexio
from .xarxes import Pronostic, Quotes, Referencia, XDDE, XEMA
