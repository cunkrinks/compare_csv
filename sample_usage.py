# sample_usage.py
# Demo usage: programmatically invoke compare_csv.main() to compare linux.csv and Unix.csv

import sys
from pathlib import Path

# Adjust the path to the project root if you run this from a different folder
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Build sys.argv similar to how command-line would pass parameters
sys.argv = [
    'compare_csv.py',
    'linux.csv',
    'Unix.csv',
    '--report',
    '--excel',
    '--outdir',
    'out_sections'
]

# Run!
import compare_csv
compare_csv.main()
print('sample usage completed; check out_sections folder')
