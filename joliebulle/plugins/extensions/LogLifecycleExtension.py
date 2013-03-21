import logging
from plugins.ExtensionPoints import AppLifecycleExtensionPoint
import globals

class LogLifecycleExtension(AppLifecycleExtensionPoint):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def startup(self):
        self.logger.info("---------------------");
        self.logger.info("Jolibulle %s", globals.VERSION_JOLIBULLE);

    def shutdown(self):
        self.logger.info("Joliebulle shutdown");
        self.logger.info("---------------------");
