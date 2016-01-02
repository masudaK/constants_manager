from constants_manager.constants_manager import ConstantsManager
import os
import pytest


class TestConstantsManager():
    def test_get_default_value(self):
        __expected = 'val_only_default'

        consts = ConstantsManager()
        assert __expected == consts.get('val_only_default')

    def test_get_section_value(self):
        __expected = 'val_only_dev'

        os.environ["ENV"] = 'dev'
        consts = ConstantsManager()
        assert __expected == consts.get('val_only_dev')

    def test_get_default_value_witout_section_value(self):
        __expected = 'val_only_default'

        os.environ["ENV"] = 'dev'
        consts = ConstantsManager()
        assert __expected == consts.get('val_only_default')

    def test_change_os_environment(self):
        __expected = 'val_only_default'

        os.environ["ENV_DUMMY"] = 'dev'
        consts = ConstantsManager(constants_name='ENV_DUMMY')
        assert __expected == consts.get('val_only_default')

    def test_using_not_exists_os_environment(self):
        __expected = 'val_only_default'

        os.environ["ENV_DUMMY"] = 'dev'
        consts = ConstantsManager()
        assert __expected == consts.get('val_only_default')

    def test_using_not_exists_os_environment_and_not_find_key(self):
        os.environ["ENV_DUMMY"] = 'dev'
        consts = ConstantsManager(constants_name='DUMMY')
        with pytest.raises(Exception):
            consts.get('val_only_dev')
