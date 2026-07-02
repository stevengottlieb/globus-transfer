# gtransfer Architecture

## Overview

`gtransfer` is a command-line utility for transferring scientific data
using the Globus Transfer service.

The primary design goals are

- Reliability
- Simplicity
- Excellent diagnostics
- HPC-friendly workflows
- Modern Python architecture
- Extensibility

The project is intended to make common Globus transfers significantly
easier than using the general-purpose Globus CLI while remaining fully
compatible with the Globus Transfer service.

---

# Design Philosophy

The guiding principles are

1. Make the common case easy.

2. Never sacrifice reliability for convenience.

3. Preserve all data.

4. Verify everything.

5. Fail loudly and explain why.

6. Never require users to remember endpoint UUIDs.

7. Support unattended operation.

8. Produce logs that are useful months later.

9. Keep the code modular.

10. Make adding new commands straightforward.

---

# Overall Architecture

                    CLI
                     |
             Command Dispatcher
                     |
      +--------------+--------------+
      |              |              |
 Authentication   Configuration   Endpoint Manager
      |              |              |
      +--------------+--------------+
                     |
              Transfer Manager
                     |
             Globus Transfer API
                     |
                Globus Service

---

# Modules

cli.py

Responsible for

- parsing commands
- displaying help
- invoking library functions

Contains no business logic.

---

auth.py

Responsible for

- OAuth login
- refresh tokens
- logout
- secure token storage

Only this module communicates with the OAuth layer.

---

config.py

Loads and validates

~/.config/gtransfer/config.toml

Creates configuration directories if needed.

Stores

- endpoint aliases
- preferences
- default options

---

endpoint.py

Responsible for

- endpoint discovery
- endpoint aliases
- endpoint activation
- endpoint information

Provides

EndpointManager

---

transfer.py

Implements

TransferManager

Responsibilities

- submit transfers
- recursive copies
- synchronization
- retries
- polling
- completion

No user interface code.

---

progress.py

Displays

- progress bars
- ETA
- throughput
- file counts

Uses Rich.

---

history.py

Maintains

SQLite database

Stores

- task IDs
- completion status
- elapsed time
- bytes transferred
- endpoints
- timestamps

Supports

gtransfer history

and

gtransfer resume

---

logging.py

Creates

~/.local/state/gtransfer/

Writes rotating log files.

---

doctor.py

Runs diagnostics.

Checks

- authentication
- endpoint activation
- network connectivity
- configuration
- SDK version

Produces a human-readable report.

---

util.py

Small reusable helper functions.

No Globus-specific code.

---

# Configuration

Configuration lives in

~/.config/gtransfer/

Example

config.toml

[ranch]
endpoint = "UUID"
root = "/corral-repl/tacc/NONE/project"

[laptop]
endpoint = "UUID"
root = "/Users/steve"

---

# Cache

Cached information

~/.cache/gtransfer/

Contains

history.sqlite

task cache

temporary files

---

# Logging

Logs

~/.local/state/gtransfer/

Each run receives

timestamp

command

PID

log level

---

# Command Flow

Example

gtransfer copy foo.dat ranch:foo.dat

#

CLI parses arguments

#

Configuration loaded

#

Authentication checked

#

Endpoints resolved

#

Endpoints activated

#

Transfer submitted

#

Progress displayed

#

History recorded

#

Exit

---

# Error Handling

Errors are represented by custom exceptions.

AuthenticationError

ConfigurationError

EndpointError

TransferError

ValidationError

The CLI catches these and presents friendly messages.

---

# Testing

pytest

Unit tests

Configuration

Authentication

Endpoint parsing

Transfer submission

Mock Globus API

Continuous integration runs all tests.

---

# Coding Standards

Python 3.11+

Type hints everywhere.

ruff

mypy

pytest

Black-compatible formatting.

---

# Future Extensions

Synchronization

Scheduled transfers

Email notification

Webhook support

Bandwidth limiting

Transfer manifests

Checksum reports

Transfer statistics

JSON output

REST API

GUI

---

# Non-goals

This project is not intended to replace

- Globus CLI
- Globus Connect

Instead it provides a workflow optimized for researchers and HPC users.

---

# License

MIT
