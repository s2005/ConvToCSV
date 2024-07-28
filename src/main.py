import argparse
import csv
import sys

def detect_header_type(header):
    return '\t' in header

def convert_tab_to_csv(input_file, output_file, encoding='utf-8', header_lines=1):
    with open(input_file, 'r', encoding=encoding) as infile, \
         open(output_file, 'w', newline='', encoding=encoding) as outfile:

        # Read the header lines
        header = [next(infile).strip() for _ in range(header_lines)]

        # Determine the type of the header
        is_tab_header = any(detect_header_type(h) for h in header)

        # Process the header
        if is_tab_header:
            header = [h.split('\t') for h in header]
            header = [item for sublist in header for item in sublist]
        else:
            header_dialect = csv.Sniffer().sniff(''.join(header))
            header_reader = csv.reader(header, dialect=header_dialect)
            header = [item for row in header_reader for item in row]

        # Set up the reader and writer
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

        # Write the header
        if header:
            writer.writerow(header)

        # Write the rest of the file
        for row in reader:
            if row:  # Skip empty lines
                writer.writerow(row)

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
        convert_tab_to_csv(args.input_file, args.output_file, args.encoding, args.header_lines)
        print(f"Conversion completed: {args.input_file} -> {args.output_file}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()