import os
import sys
import pytest
from glob import glob


def pytest_generate_tests(metafunc):
    if 'day' in metafunc.fixturenames:
        days = []
        for script in glob('**/day*.py', recursive=True):
            day = os.path.splitext(script)[0]
            days.append(day)
        metafunc.parametrize("day", days)


def test_all(day):
    day = day.replace('\\', '/')
    if day in ('2016/day05', '2016/day14', '2016/day16', '2016/day18', '2016/day19'):
        pytest.skip('Too long day')
    retcode = os.system('{python} {day}.py {day}_input > {day}_output'.format(python=sys.executable, day=day))
    assert retcode == 0

    output_filename = day + '_output'
    with open(day + '_expected') as expected, open(output_filename) as output_file:
        expected_output = expected.read().strip()
        output = output_file.read().strip()

    assert expected_output == output

    os.remove(output_filename)
