# Git Config Getter

This project provides a structured way to handle Git configuration data using Python classes and protocols.

## Overview

The project consists of three main components:

1. **GitConfig Class**: A class that represents Git configuration with name and email attributes. The attributes are private and accessed through properties.

2. **GitConfigGetter Protocol**: A protocol (interface-like) definition for classes that can retrieve Git configuration.

3. **Concrete Implementations**: Two implementations of the GitConfigGetter protocol:
   - `GitConfigFromGitCommand`: Gets Git configuration from the local git config using `git config` command
   - `GitConfigFromEnvVars`: Gets Git configuration from environment variables `GIT_USER_NAME` and `GIT_USER_EMAIL`

## Why Protocols Shouldn't Be Tested

Protocols in Python serve as interfaces - they define what methods a class should implement but don't contain any implementation themselves. Testing protocols directly doesn't make sense because:

1. **They don't have behavior**: Protocols only define the interface contract, not the actual implementation.
2. **They're meant to be implemented**: The real value comes from testing concrete implementations that conform to the protocol.
3. **They're type hints**: Protocols are primarily used for static type checking and runtime introspection, not for execution.

Instead of testing protocols, you should test concrete classes that implement the protocol. This ensures that the actual implementation works as expected while maintaining the flexibility of the interface.

## Why Relative Imports Are Not Allowed

Relative imports (like `from .git_config import GitConfig`) are generally discouraged in Python for several reasons:

1. **Code Organization**: They create tight coupling between modules and make the code harder to understand and maintain.
2. **Reusability**: Modules with relative imports are harder to reuse in different contexts or as standalone scripts.
3. **Clarity**: Absolute imports make it clear where each module comes from, improving code readability.
4. **Compatibility**: Relative imports can cause issues when modules are run as scripts or in certain packaging scenarios.

In this project, we've used absolute imports (like `from git_config import GitConfig`) to maintain better code organization and reusability.

## Project Structure

- `git_config.py`: Contains the GitConfig class with name and email attributes
- `git_config_getter.py`: Contains the GitConfigGetter protocol definition  
- `git_config_from_git_command.py`: Implementation that gets Git configuration from git config command
- `git_config_from_env_vars.py`: Implementation that gets Git configuration from environment variables
- `test_git_config.py`: Contains tests for the GitConfig class

## Usage Examples

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

## Testing

Only concrete implementations should be tested. The `test_git_config.py` file contains tests for the GitConfig class to ensure it behaves as expected.

## Installation

This project uses Pipenv for dependency management. To install dependencies:

```bash
pipenv install
pipenv install mkdocs  # For documentation generation
```

## Documentation

Documentation can be built and served using MkDocs:

```bash
pipenv run mkdocs serve
