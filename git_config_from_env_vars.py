import os
from git_config import GitConfig

class GitConfigFromEnvVars:
    """Gets Git configuration from environment variables GIT_USER_NAME and GIT_USER_EMAIL."""

    def get(self) -> GitConfig:
        """
        Get the Git configuration from environment variables.

        Returns:
            A GitConfig instance with name and email attributes
        """
        name = os.environ.get('GIT_USER_NAME')
        email = os.environ.get('GIT_USER_EMAIL')
        
        if name is None or email is None:
            raise ValueError("Both GIT_USER_NAME and GIT_USER_EMAIL environment variables must be set")
            
        return GitConfig(name=name, email=email)
