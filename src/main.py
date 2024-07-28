import argparse
import csv
import sys
import io

def detect_header_type(header, delimiter):
    return delimiter in header

def convert_tab_to_csv(input_file, output_file, encoding='utf-8', header_lines=1, delimiter='\t', debug=False):
    debug_output = io.StringIO() if debug else None

    def debug_print(*args, **kwargs):
        if debug:
            print(*args, file=debug_output, **kwargs)

    with open(input_file, 'r', encoding=encoding) as infile, \
         open(output_file, 'w', newline='', encoding=encoding) as outfile:

        debug_print(f"Debug: Input file contents:")
        debug_print(infile.read())
        infile.seek(0)  # Reset file pointer to beginning

        # Read the header lines if any
        header = []
        if header_lines > 0:
            header = [next(infile).strip() for _ in range(header_lines)]
            debug_print(f"Debug: Header: {header}")

            # Determine the type of the header
            is_delimited_header = any(detect_header_type(h, delimiter) for h in header)
            debug_print(f"Debug: Is delimited header: {is_delimited_header}")

            # Process the header
            if is_delimited_header:
                header = [h.split(delimiter) for h in header]
                header = [item for sublist in header for item in sublist]  # Flatten the list
            else:
                header_dialect = csv.Sniffer().sniff(''.join(header))
                header_reader = csv.reader(header, dialect=header_dialect)
                header = [item for row in header_reader for item in row]  # Flatten the list

            debug_print(f"Debug: Processed header: {header}")

            # Write the header
            outfile.write(','.join(header) + '\n')

        # Write the rest of the file
        for line in infile:
            if line.strip():  # Skip empty lines
                row = line.strip().split(delimiter)
                debug_print(f"Debug: Writing row: {row}")
                # Ensure fields with spaces or commas are quoted
                quoted_row = [f'"{field}"' if ' ' in field or ',' in field else field for field in row]
                outfile.write(','.join(quoted_row) + '\n')

    # Read the output file contents
    if debug:
        with open(output_file, 'r', encoding=encoding) as outfile:
            output_contents = outfile.read()
            debug_print(f"Debug: Output file contents:")
            debug_print(output_contents)

    return debug_output.getvalue() if debug else None

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert delimited file to CSV')
    parser.add_argument('input_file', help='Input file')
    parser.add_argument('output_file', help='Output CSV file')
    parser.add_argument('--encoding', default='utf-8', help='File encoding (default: utf-8)')
    parser.add_argument('--header-lines', type=int, default=1, help='Number of header lines (default: 1)')
    parser.add_argument('--delimiter', default='\t', help='Input file delimiter (default: \\t)')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')

    return parser.parse_args()

def main():
    args = parse_arguments()

    try:
        debug_info = convert_tab_to_csv(args.input_file, args.output_file, args.encoding, args.header_lines, args.delimiter, args.debug)
        if args.debug and debug_info:
            print(debug_info)  # Print debug information
        print(f"Conversion completed: {args.input_file} -> {args.output_file}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()