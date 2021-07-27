import pytest


@pytest.fixture
def verbose_setting(request):
    """Fixture to assign self.VERBOSE if called by test class, or return boolean if called by test function
    This fixture is enabled for all tests in the pytest.ini file.
    """
    verbosity = request.config.getoption("--verbose") > 1
    if request.cls is not None:
        # LOGGER.info(f"Assigning class attribute, verbosity: {verbosity}")
        request.cls.VERBOSE = verbosity
    else:
        # LOGGER.info(f"Returning value to function, verbosity: {verbosity}")
        # Needs to be imported with: def test_func(verbose_setting):
        return verbosity
