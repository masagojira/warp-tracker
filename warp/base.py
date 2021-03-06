""" Base classes """

import logging
from warp.lib import Singleton

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

INIT = 'initialization'


class Server(object, metaclass=Singleton):
    """ Base server class """
    def __init__(self):
        self.state = INIT
        self._log_state()

    def _log_state(self):
        logger.debug('%s state: %s', self.__class__.__name__, self.state)

    def serve(self):
        """ run server """
        raise NotImplementedError
