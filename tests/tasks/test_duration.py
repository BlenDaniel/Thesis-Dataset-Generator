import datetime
from analysis.tasks.outputs.duration import calculate_duration


def test_calculate_duration():
    authored_at = '04/01/2023, 09:00:00'
    committed_at = '04/02/2023, 09:00:00'
    expected_duration = 1

    # Call the function and assert the result
    assert calculate_duration(authored_at, committed_at) == expected_duration
