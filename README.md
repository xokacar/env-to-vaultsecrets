
# env-to-secret-converter

This script converts environment variable definitions into a specific YAML format for use with Kubernetes secrets. The script reads environment variables in the form `KEY = 'value'` and outputs them in the format:

```yaml
- name: KEY
  secretName: vc-fs-to-ts-dev-secrets
  secretKey: value
```

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/env-to-secret-converter.git
cd env-to-secret-converter
```

2. Ensure you have Python 3.x installed on your system.

## Usage

1. Edit the `env_values` variable in the script to include your environment variable definitions.

2. Run the script:

```bash
python convert_env.py
```

3. The script will output the converted values to the console. You can redirect this output to a file if needed:

```bash
python convert_env.py > output.yaml
```

## Example

### Input

```python
env_values = """
EXAMPLE_VAL  = 'asdasd'
EXAMPLE_VAL2  = 'asdasd'
EXAMPLE_VAL3  = 'asdasd'
"""
```

### Output

```yaml
- name: EXAMPLE_VAL
  secretName: vc-fs-to-ts-dev-secrets
  secretKey: asdasd
- name: EXAMPLE_VAL2
  secretName: vc-fs-to-ts-dev-secrets
  secretKey: asdasd
- name: EXAMPLE_VAL3
  secretName: vc-fs-to-ts-dev-secrets
  secretKey: asdasd
```
