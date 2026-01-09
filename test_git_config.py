import pytest
from git_config import GitConfig


def test_git_config_initialization() -> None:
    """Test that GitConfig can be initialized with name and email."""
    config = GitConfig(name="John Doe", email="john@example.com")
    
    assert config.name == "John Doe"
    assert config.email == "john@example.com"


def test_git_config_properties() -> None:
    """Test that the property methods return the correct values."""
    config = GitConfig(name="Jane Smith", email="jane@example.com")
    
    assert config.name == "Jane Smith"
    assert config.email == "jane@example.com"


def test_git_config_repr() -> None:
    """Test that the __repr__ method returns the expected string."""
    config = GitConfig(name="Alice Brown", email="alice@example.com")
    
    expected = "GitConfig(name='Alice Brown', email='alice@example.com')"
    assert repr(config) == expected


def test_git_config_to_dict() -> None:
    """Test that the to_dict method returns the expected dictionary."""
    config = GitConfig(name="Bob White", email="bob@example.com")
    
    expected = {
        "name": "Bob White",
        "email": "bob@example.com"
    }
    assert config.to_dict() == expected


def test_git_config_unique_instances() -> None:
    """Test that different instances have different values."""
    config1 = GitConfig(name="User One", email="user1@example.com")
    config2 = GitConfig(name="User Two", email="user2@example.com")
    
    assert config1.name != config2.name
    assert config1.email != config2.email
    assert config1.to_dict() != config2.to_dict()


if __name__ == "__main__":
    pytest.main()
