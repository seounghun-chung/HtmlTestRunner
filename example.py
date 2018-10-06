from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from tests.test import TestStringMethods
from tests.test2 import My_Tests

example_tests = TestLoader().loadTestsFromTestCase(TestStringMethods)
example2_tests = TestLoader().loadTestsFromTestCase(My_Tests)

suite = TestSuite([example_tests, example2_tests])
template_args = {'Note' : 'test sample'}
runner = HTMLTestRunner(output='example_suite', 
                        report_name='Test Result V0.0.1', 
                        report_title='Test Result V0.0.1',
                        template_args=template_args, 
                        combine_reports = True)
runner.run(suite)