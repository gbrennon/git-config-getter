from typing import Any


class GitConfig:
    """Represents Git configuration with name and email attributes."""

    def __init__(self, name: str, email: str) -> None:
        """
        Initialize a GitConfig instance.

        Args:
            name: The user's name for Git configuration
            email: The user's email for Git configuration
        """
        self._name: str = name
        self._email: str = email

    @property
    def name(self) -> str:
        """Get the name attribute."""
        return self._name

    @property
    def email(self) -> str:
        """Get the email attribute."""
        return self._email

    def __repr__(self) -> str:
        """Return a string representation of the GitConfig instance."""
        return f"GitConfig(name='{self._name}', email='{self._email}')"

    def to_dict(self) -> dict[str, str]:
        """Convert the GitConfig instance to a dictionary."""
        return {
            "name": self._name,
            "email": self._email
        }
