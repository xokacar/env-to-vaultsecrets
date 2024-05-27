import re

# Input environment values
env_values = """
EXAMPLE_VALUE1 = "test111"
EXAMPLE_VALUE2 = "test222"
EXAMPLE_VALUE3 = "test333"
"""


def convert_env_values(env_values):
    def transform_key(key):

        return key.lower().replace('_', '-')
    
    env_lines = env_values.strip().split('\n')
    result = []
    for line in env_lines:
        match = re.match(r'(\w+)\s*=\s*"([^"]*)"', line)
        if match:
            key = match.group(1)
            transformed_key = transform_key(key)
            result.append(f" - name: {key}\n    secretName: secret-Name\n    secretKey: {transformed_key}")

    return '\n'.join(result)


converted_values = convert_env_values(env_values)
print(converted_values)
