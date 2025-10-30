## uv Cheat Sheet

### Install uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# Make uv available in the current shell
source $HOME/.local/bin/env
```

### Project setup (this repo)
```bash
# Install runtime deps from pyproject.toml and create .venv
uv sync

# Install dev/test tools declared in dependency group
uv sync --group test
```

### Running commands inside the environment
```bash
# Run tests
uv run pytest -q

# Run CLI without installing the package
uv run vendas-cli vendas_ficticias_reais.csv --format text
```

### Managing dependencies
```bash
# Add a runtime dependency
uv add <package>             # e.g., uv add tabulate

# Add a dev/test dependency to the "test" group
uv add --group test <package>  # e.g., uv add --group test pytest

# Remove a dependency
uv remove <package>
```

### Installing the package locally
```bash
# Editable install (develop mode)
uv pip install -e .

# Regular install
uv pip install .
```

### Environment management
```bash
# Recreate the environment from lock/pyproject
uv sync --reinstall

# Update dependencies to latest compatible versions
uv sync --upgrade
```

### Tips
- If a new terminal can’t find `uv`, run:
```bash
source $HOME/.local/bin/env
```
- Keep project dependencies in `pyproject.toml`. Dev/test tools go in the `dependency-groups.test` section.
