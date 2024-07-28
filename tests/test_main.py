import unittest
import tempfile
import os
import sys
from src.main import convert_tab_to_csv, parse_arguments

class TestDelimitedToCsvConverter(unittest.TestCase):
    def setUp(self):
        self.test_input_tab = "Header1\tHeader2\tHeader3\n" \
                              "Value1\tValue with spaces\tValue3\n" \
                              "\n" \
                              "Value4\tValue5\tValue6"

        self.test_input_csv_header = '"Header1","Header2","Header3"\n' \
                                     "Value1\tValue with spaces\tValue3\n" \
                                     "\n" \
                                     "Value4\tValue5\tValue6"

        self.test_input_multi_header = "Header1\tHeader2\tHeader3\n" \
                                       "SubHeader1\tSubHeader2\tSubHeader3\n" \
                                       "Value1\tValue with spaces\tValue3\n" \
                                       "\n" \
                                       "Value4\tValue5\tValue6"

        self.test_input_csv_multi_header = '"Header1","Header2","Header3"\n' \
                                           '"SubHeader1","SubHeader2","SubHeader3"\n' \
                                           "Value1\tValue with spaces\tValue3\n" \
                                           "\n" \
                                           "Value4\tValue5\tValue6"

        self.test_input_no_header = "Value1\tValue with spaces\tValue3\n" \
                                    "Value4\tValue5\tValue6"

        self.test_input_comma_delimited = "Header1|Header2|Header3\n" \
                                          "Value1|Value with spaces|Value3\n" \
                                          "\n" \
                                          "Value4|Value5|Value6"

    def test_conversion_tab_header(self):
        self._run_test(self.test_input_tab,
                       'Header1,Header2,Header3\n'
                       'Value1,"Value with spaces",Value3\n'
                       'Value4,Value5,Value6',
                       delimiter='\t')

    def test_conversion_csv_header(self):
        self._run_test(self.test_input_csv_header,
                       'Header1,Header2,Header3\n'
                       'Value1,"Value with spaces",Value3\n'
                       'Value4,Value5,Value6',
                       delimiter='\t')

    def test_conversion_multi_tab_header(self):
        self._run_test(self.test_input_multi_header,
                       'Header1,Header2,Header3,SubHeader1,SubHeader2,SubHeader3\n'
                       'Value1,"Value with spaces",Value3\n'
                       'Value4,Value5,Value6',
                       header_lines=2,
                       delimiter='\t')

    def test_conversion_multi_csv_header(self):
        self._run_test(self.test_input_csv_multi_header,
                       'Header1,Header2,Header3,SubHeader1,SubHeader2,SubHeader3\n'
                       'Value1,"Value with spaces",Value3\n'
                       'Value4,Value5,Value6',
                       header_lines=2,
                       delimiter='\t')

    def test_conversion_no_header(self):
        self._run_test(self.test_input_no_header,
                       'Value1,"Value with spaces",Value3\n'
                       'Value4,Value5,Value6',
                       header_lines=0,
                       delimiter='\t')

    def test_conversion_pipe_delimited(self):
        self._run_test(self.test_input_comma_delimited,
                       'Header1,Header2,Header3\n'
                       'Value1,"Value with spaces",Value3\n'
                       'Value4,Value5,Value6',
                       delimiter='|')

    def test_debug_output(self):
        input_content = "Header1\tHeader2\nValue1\tValue2"
        expected_output = "Header1,Header2\nValue1,Value2\n"

        with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as input_file, \
             tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as output_file:

            input_file.write(input_content)
            input_file.close()

            debug_info = convert_tab_to_csv(input_file.name, output_file.name, delimiter='\t', debug=True)

            self.assertIsNotNone(debug_info)
            self.assertIn("Debug: Input file contents:", debug_info)
            self.assertIn("Debug: Header:", debug_info)
            self.assertIn("Debug: Is delimited header:", debug_info)
            self.assertIn("Debug: Processed header:", debug_info)
            self.assertIn("Debug: Writing row:", debug_info)
            self.assertIn("Debug: Output file contents:", debug_info)

            output_file.close()

            with open(output_file.name, 'r', encoding='utf-8') as f:
                result = f.read()

            self.assertEqual(result, expected_output)

        os.unlink(input_file.name)
        os.unlink(output_file.name)

    def test_parse_arguments(self):
        # Test with minimum required arguments
        sys.argv = ['script_name', 'input.txt', 'output.csv']
        args = parse_arguments()
        self.assertEqual(args.input_file, 'input.txt')
        self.assertEqual(args.output_file, 'output.csv')
        self.assertEqual(args.encoding, 'utf-8')
        self.assertEqual(args.header_lines, 1)
        self.assertEqual(args.delimiter, '\t')
        self.assertFalse(args.debug)

        # Test with all arguments
        sys.argv = ['script_name', 'input.txt', 'output.csv', '--encoding', 'latin-1', '--header-lines', '2', '--delimiter', '|']
        args = parse_arguments()
        self.assertEqual(args.input_file, 'input.txt')
        self.assertEqual(args.output_file, 'output.csv')
        self.assertEqual(args.encoding, 'latin-1')
        self.assertEqual(args.header_lines, 2)
        self.assertEqual(args.delimiter, '|')
        self.assertFalse(args.debug)

        # Test with debug flag
        sys.argv = ['script_name', 'input.txt', 'output.csv', '--debug']
        args = parse_arguments()
        self.assertEqual(args.input_file, 'input.txt')
        self.assertEqual(args.output_file, 'output.csv')
        self.assertEqual(args.encoding, 'utf-8')
        self.assertEqual(args.header_lines, 1)
        self.assertEqual(args.delimiter, '\t')
        self.assertTrue(args.debug)

    def _run_test(self, input_content, expected_output, header_lines=1, delimiter='\t'):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as input_file, \
             tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as output_file:

            # Write test input
            input_file.write(input_content)
            input_file.close()

            # Convert and capture debug output
            debug_output = convert_tab_to_csv(input_file.name, output_file.name, header_lines=header_lines, delimiter=delimiter, debug=True)

            print(f"Debug output for {self._testMethodName}:")
            print(debug_output)

            output_file.close()

            # Read and check output
            with open(output_file.name, 'r', encoding='utf-8') as f:
                result = f.read().strip()

            self.assertEqual(result, expected_output)

        # Clean up temporary files
        os.unlink(input_file.name)
        os.unlink(output_file.name)

if __name__ == '__main__':
    unittest.main()