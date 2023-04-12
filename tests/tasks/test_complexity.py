from analysis.tasks.outputs.complexity import calculate_task_complexity


def test_calculate_task_complexity():
    """
    Test case for the calculate_task_complexity function.
    """
    # Test case 1: A commit with no files affected or changed, no lines added or deleted, and no bug fixing
    assert calculate_task_complexity(0, 0, 0, 0, False) == 1.0
    
    # Test case 2: A commit with one file affected, one files changed, one lines added or deleted, and no bug fixing
    assert calculate_task_complexity(1, 1, 1, 1, False) == 1.0
    
    # Test case 3: A commit with one file affected, one file changed, no lines added or deleted, and no bug fixing
    assert calculate_task_complexity(1, 1, 0, 0, False) == 1.0
    
    # Test case 4: A commit with one file affected, one file changed, 100 lines added and no lines deleted, and no bug fixing
    assert calculate_task_complexity(1, 1, 100, 0, False) == 1.5
    
    # Test case 5: A commit with one file affected, one file changed, 100 lines added and no lines deleted, and with bug fixing
    assert calculate_task_complexity(1, 1, 100, 0, True) == 1.8
    
    # Test case 6: A commit with ten files affected, five files changed, 500 lines added and 100 lines deleted, and with bug fixing
    assert calculate_task_complexity(10, 5, 500, 100, True) == 4.2
    
    # Test case 7: A commit with ten files affected, five files changed, 500 lines added and 100 lines deleted, and no bug fixing
    assert calculate_task_complexity(10, 5, 500, 100, False) == 3.5
