from typing import Protocol
from git_config import GitConfig


class GitConfigGetter(Protocol):
    """Protocol for classes that can get Git configuration."""

    def get(self) -> GitConfig:
        """
        Get the Git configuration.

        Returns:
            A GitConfig instance with name and email attributes
        """
        ...  # Protocol doesn't implement anything
