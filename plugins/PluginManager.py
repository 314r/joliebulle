import logging

logger = logging.getLogger(__name__)

#Singleton class, should be in some common module
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class PluginMetaclass(Singleton):

    def __init__(cls, name, bases, dct):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)
        logger.debug("Initializing class", name)
        logger.debug('cls=%s bases=%s dct=%s', cls, bases, dct)

        super(PluginMetaclass, cls).__init__(name, bases, dct)

