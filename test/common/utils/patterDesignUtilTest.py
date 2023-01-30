import unittest
from app.common.utils.patterDesignUtil import PatterDesignUtil


class PatterDesignUtilTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_patter_singleton(self) -> None:
        @PatterDesignUtil.singleton
        class User:
            pass
        instance1 = User()
        instance2 = User()
        self.assertEqual(instance1,instance2,"Error con el patron de diseño singleton")