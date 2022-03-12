class XarxaBase:
    def __init__(self, connexio):
        self._connexio = connexio
        self.xarxa = self.__class__.__name__.lower()

    def _aconsegueix(self, recurs, params=None):
        return self._connexio.demana(self.xarxa, recurs, params)
