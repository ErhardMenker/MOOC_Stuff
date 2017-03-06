## Testing Code
# Code should be written in pieces and tested for accuracy before moving on to the next part of the project.
# "POC SimpleTest" allows the automation of testing and can be found here: https://www.coursera.org/learn/principles-of-computing-1/supplement/bUWIL/building-tests-for-python-programs
# The module to import is poc_format_testsuite.

"""
Format function for a stopwatch
"""

import poc_format_testsuite
    
def stopwatch_format(ticks):
    """
    Convert tenths of seconds to formatted time
    """
    
    minutes = ticks // 600
    # minutes = ticks // 60
    tens_seconds =  (ticks // 100) % 6
    seconds = (ticks // 10) % 10
    tenths = ticks % 10
    return str(minutes) + ':' + str(tens_seconds) + \
           str(seconds) + '.' + str(tenths)
    
# run the testing suite for our format function
poc_format_testsuite.run_suite(stopwatch_format)
# note that this suite runs 13 tests and finds 0 failures.


"""
Test suite for format function in "Stopwatch - The game"
"""

import poc_simpletest

def run_suite(format_function):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test format_function on various inputs
    suite.run_test(format_function(0), "0:00.0", "Test #1:")
    suite.run_test(format_function(7), "0:00.7", "Test #2:")
    suite.run_test(format_function(17), "0:01.7", "Test #3:")
    suite.run_test(format_function(60), "0:06.0", "Test #4:")
    suite.run_test(format_function(63), "0:06.3", "Test #5:")
    suite.run_test(format_function(214), "0:21.4", "Test #6:")
    suite.run_test(format_function(599), "0:59.9", "Test #7:")
    suite.run_test(format_function(600), "1:00.0", "Test #8:")
    suite.run_test(format_function(602), "1:00.2", "Test #9:")
    suite.run_test(format_function(667), "1:06.7", "Test #10:")
    suite.run_test(format_function(1325), "2:12.5", "Test #11:")
    suite.run_test(format_function(4567), "7:36.7", "Test #12:")
    suite.run_test(format_function(5999), "9:59.9", "Test #13:")
    
    suite.report_results()
    