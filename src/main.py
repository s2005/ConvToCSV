import argparse
import csv
import sys
import io

def detect_header_type(header):
    return '\t' in header

def convert_tab_to_csv(input_file, output_file, encoding='utf-8', header_lines=1):
    debug_output = io.StringIO()

    with open(input_file, 'r', encoding=encoding) as infile, \
         open(output_file, 'w', newline='', encoding=encoding) as outfile:

        print(f"Debug: Input file contents:", file=debug_output)
        print(infile.read(), file=debug_output)
        infile.seek(0)  # Reset file pointer to beginning

        # Read the header lines
        header = [next(infile).strip() for _ in range(header_lines)]
        print(f"Debug: Header: {header}", file=debug_output)

        # Determine the type of the header
        is_tab_header = any(detect_header_type(h) for h in header)
        print(f"Debug: Is tab header: {is_tab_header}", file=debug_output)

        # Process the header
        if is_tab_header:
            header = [h.split('\t') for h in header]
            header = [item for sublist in header for item in sublist]  # Flatten the list
        else:
            header_dialect = csv.Sniffer().sniff(''.join(header))
            header_reader = csv.reader(header, dialect=header_dialect)
            header = [item for row in header_reader for item in row]  # Flatten the list

        print(f"Debug: Processed header: {header}", file=debug_output)

        # Write the header
        if header:
            outfile.write(','.join(header) + '\n')

        # Write the rest of the file
        for line in infile:
            if line.strip():  # Skip empty lines
                row = line.strip().split('\t')
                print(f"Debug: Writing row: {row}", file=debug_output)
                # Ensure fields with spaces or commas are quoted
                quoted_row = [f'"{field}"' if ' ' in field or ',' in field else field for field in row]
                outfile.write(','.join(quoted_row) + '\n')

    # Read the output file contents
    with open(output_file, 'r', encoding=encoding) as outfile:
        output_contents = outfile.read()
        print(f"Debug: Output file contents:", file=debug_output)
        print(output_contents, file=debug_output)

    return debug_output.getvalue()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert TAB-delimited file to CSV')
    parser.add_argument('input_file', help='Input file')
    parser.add_argument('output_file', help='Output CSV file')
    parser.add_argument('--encoding', default='utf-8', help='File encoding (default: utf-8)')
    parser.add_argument('--header-lines', type=int, default=1, help='Number of header lines (default: 1)')

    return parser.parse_args()

def main():
    args = parse_arguments()

    try:
        debug_info = convert_tab_to_csv(args.input_file, args.output_file, args.encoding, args.header_lines)
        print(debug_info)  # Print debug information
        print(f"Conversion completed: {args.input_file} -> {args.output_file}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()