import subprocess
from git_config import GitConfig

class GitConfigFromGitCommand:
    """Gets Git configuration from the local git config using git config command."""

    def get(self) -> GitConfig:
        """
        Get the Git configuration from git config command.

        Returns:
            A GitConfig instance with name and email attributes
        """
        try:
            # Get name from git config
            name_process = subprocess.run(
                ['git', 'config', '--global', 'user.name'],
                capture_output=True,
                text=True,
                check=True
            )
            name = name_process.stdout.strip()
            
            # Get email from git config
            email_process = subprocess.run(
                ['git', 'config', '--global', 'user.email'],
                capture_output=True,
                text=True,
                check=True
            )
            email = email_process.stdout.strip()
            
            return GitConfig(name=name, email=email)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to get git configuration: {e}") from e
