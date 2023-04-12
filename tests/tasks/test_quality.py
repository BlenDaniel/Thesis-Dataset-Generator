from analysis.tasks.outputs.quality import calculate_code_quality


def test_calculate_code_quality():
    # Test case 1: all values are zero
    assert calculate_code_quality(0, 0, 0, 0, 0, 0, False) == 0.0
    
    # Test case 2: some values are non-zero
    assert calculate_code_quality(1, 2, 100, 50, 1, 0, False) == 3.8
    
    # Test case 3: all values are non-zero
    assert calculate_code_quality(5, 10, 500, 200, 2, 1, True) == 3.8
    
    # Test case 4: total_files_affected and total_files_changed are zero
    assert calculate_code_quality(0, 10, 500, 200, 2, 1, False) == 0.0
    
    # Test case 5: total_files_changed is zero
    assert calculate_code_quality(5, 0, 500, 200, 2, 1, False) == 0.0
    
    # Test case 6: file_additions and file_deletions are both zero
    assert calculate_code_quality(5, 10, 500, 200, 0, 1, False) == 2.5

