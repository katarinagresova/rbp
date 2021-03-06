"""
This example shows a standard way to parse arguments and get an input file handler.

Usage:
    echo -e "Whenever\nWhatever" | python examples/parsing_input_file.py
    echo -e "Whenever\nWhatever" | python examples/parsing_input_file.py -q
    python examples/parsing_input_file.py -h

Petr Simecek, January 2020
"""

from rbp.utils import get_argument_parser, get_input_file

parser = get_argument_parser()
parser.add_argument('--extra_option', '-e', type=str,
                    help='You can add an extra option if needed.', default='')
args = parser.parse_args()

verbose = args.verbose

if verbose:
    print(args.input_file)
    print(args.output_file)
    print(args.verbose)

with get_input_file(args) as fr:
    number_of_lines = 0

    for line in fr:
        number_of_lines += 1
        if verbose:
            print(line)

print(f"Number of lines: {number_of_lines}")
