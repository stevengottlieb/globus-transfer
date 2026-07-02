# globus-transfer

`globus-transfer` is a Python 3.11+ command-line utility for managing Globus transfers.
Milestone 1 establishes the production package structure, command surface, quality checks,
and CI foundation.

The executable is named `gtransfer`.

## Installation

```bash
python -m pip install .
```

For local development:

```bash
python -m pip install -e ".[dev]"
```

## Usage

```bash
gtransfer --help
gtransfer doctor
```

The following command groups are present as placeholders for future Globus integration:

- `login`
- `logout`
- `endpoint`
- `copy`
- `sync`
- `status`
- `history`
- `resume`
- `doctor`

## Development

Run the local checks:

```bash
ruff check .
mypy src
pytest
python -m build
```

## License

This project is licensed under the MIT License.
