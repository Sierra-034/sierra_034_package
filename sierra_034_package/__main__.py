import logging
from sierra_034_package import unreleased

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    logging.debug('>> Comienza ejecución de paquete')
    workshops = unreleased()
    logging.debug(workshops)
    logging.debug('>> Termina ejecución de paquete')
