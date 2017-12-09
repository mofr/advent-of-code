import os
import sys
import pytest
from glob import glob


def pytest_generate_tests(metafunc):
    if 'day' in metafunc.fixturenames:
        days = []
        for script in glob('day*.py'):
            day = os.path.splitext(script)[0]
            days.append(day)
        metafunc.parametrize("day", days)


def test_all(day):
    if day in ('day05', 'day14', 'day16', 'day18', 'day19'):
        pytest.skip('Too long day')
    retcode = os.system('{python} {day}.py > {day}_output'.format(python=sys.executable, day=day))
    assert retcode == 0

    with open(day + '_expected') as expected, open(day + '_output') as output:
        assert expected.read().strip() == output.read().strip()
