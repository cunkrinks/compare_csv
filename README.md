# compare_csv

Compare two CSV files and export differences using database-style operations (DELETED / INSERTED / UPDATED).

## Features

- Compare two CSV files by primary key (default: all columns).
- Report rows only in reference (DELETED), only in compare-to (INSERTED), and rows with changed values (UPDATED).
- Export CSV outputs and an optional human-readable text report.
- Optional side-by-side Excel export with color highlighting (requires `openpyxl`).
- Automatically uses the larger table as the reference table.

## Requirements

- Python 3.8+
- pandas
- openpyxl (optional, required for `--excel`)

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install the package (provides `compare-csv` script):

```bash
pip install .
```

## Usage

Run the script directly:

```bash
python compare_csv.py <fileA.csv> <fileB.csv> --name <output_dir_or_name> [options]
```

Or, after installing the package, use the console script:

```bash
compare-csv <fileA.csv> <fileB.csv> --name <output_dir_or_name> [options]
```

Required flags:
- `--name`: name used for the output directory (also used as default outdir).

Options:
- `--key`: comma-separated primary key columns (default: all columns)
- `--outdir`: explicitly set output directory (defaults to `--name`)
- `--prefix`: filename prefix for outputs (default: `diff`)
- `--report`: write a database-style text report (DELETED/INSERTED/UPDATED)
- `--excel`: write a side-by-side Excel comparison (requires `openpyxl`)

Example using sample files in this repository:

```bash
python compare_csv.py linux.csv Unix.csv --name sample_out --report --excel
```

Program behavior notes:
- If one file is larger, it will be used as the reference (A) and the other as compare-to (B).
- Both CSVs must contain the same set of columns (order may differ).
- String columns are trimmed of whitespace before comparison.

## Outputs

Given `--name sample_out` and `--prefix diff`, outputs written to `sample_out/` include:

- `diff_deleted.csv` — rows only present in reference (DELETED)
- `diff_inserted.csv` — rows only present in compare-to (INSERTED)
- `diff_updated.csv` — rows with same key but different values (UPDATED)
- `diff_combined.csv` — full outer-join with `status` column (`SAME`/`UPDATED`/`DELETED`/`INSERTED`)
- `diff_report.txt` (when `--report`) — human-readable operation-style report
- `diff_comparison.xlsx` (when `--excel`) — side-by-side Excel with highlighted differences

The Excel file includes a Summary and Legend sheet and highlights UPDATED rows in yellow and INSERTED/DELETED rows in orange.

## Examples

- Compare by an explicit key:

```bash
python compare_csv.py a.csv b.csv --key id --name result --report
```

- Use multiple key columns:

```bash
python compare_csv.py a.csv b.csv --key snap,inst --name result --report
```

- Programmatic usage example is provided in `sample_usage.py`.

## Troubleshooting

- If you get `Error: CSV column mismatch`, check that both CSV files have the same column names.
- If `--excel` fails, install `openpyxl` (see `requirements.txt`).

## License

This project is licensed under the GNU General Public License v3.0. See the `LICENSE` file for details.

---

If you'd like, I can add a basic usage example to `sample_usage.py` or add a small GitHub Action to run linting or tests.
