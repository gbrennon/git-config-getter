# Git Config Getter

## Project Overview

Git Config Getter is a Python library that provides a structured way to handle Git configuration data. The project offers two implementations for retrieving Git configuration:

1. **GitConfigFromGitCommand**: Retrieves configuration from the local git config using the `git config` command
2. **GitConfigFromEnvVars**: Retrieves configuration from environment variables `GIT_USER_NAME` and `GIT_USER_EMAIL`

## Usage Instructions

### Using GitConfigFromGitCommand

```python
from git_config_from_git_command import GitConfigFromGitCommand
from git_config import GitConfig

# Create an instance of the implementation
getter = GitConfigFromGitCommand()

# Get the Git configuration
config: GitConfig = getter.get()

# Access the configuration values through properties
print(f"Name: {config.name}, Email: {config.email}")
```

### Using GitConfigFromEnvVars

```python
import os
from git_config_from_env_vars import GitConfigFromEnvVars
from git_config import GitConfig

# Set environment variables
os.environ['GIT_USER_NAME'] = 'John Doe'
os.environ['GIT_USER_EMAIL'] = 'john@example.com'

# Create an instance of the implementation
getter = GitConfigFromEnvVars()

# Get the Git configuration
config: GitConfig = getter.get()

# Access the configuration values through properties
print(f"Name: {config.name}, Email: {config.email}")
```

## Features

- **Type Hints**: All methods and classes include proper type hints for better code clarity and IDE support
- **Private Attributes**: Configuration values are stored as private attributes with property methods for access
- **Flexible Implementation**: Choose between two different ways to retrieve Git configuration based on your needs
- **Well-Documented**: Comprehensive documentation explaining project structure and usage
