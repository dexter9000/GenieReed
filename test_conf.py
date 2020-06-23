from unittest import TestCase
from conf import Config

class TestConfig(TestCase):

    conf = Config()

    conf.read_config()
    version = conf.get("version")
    print(version)
    conf.set("es_version", "1.0")
    conf.save_config()

    pass
