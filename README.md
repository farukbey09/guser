# Git User Manager

A Python-based tool for easily managing your git user profiles.

## Features

- 🔄 Save multiple git profiles
- ⚡ Switch profiles with a single command  
- 📋 List saved profiles
- 👤 View current git user
- 🗑️ Remove profiles

## Installation

### Homebrew (Recommended)
```bash
# Add the tap
brew tap yourusername/tap

# Install guser
brew install guser
```

### Manual Installation
```bash
# Download the script
curl -O https://raw.githubusercontent.com/yourusername/git-user-manager/main/git-user-manager.py

# Make it executable and rename
chmod +x git-user-manager.py
mv git-user-manager.py guser

# Run directly
./guser help
```

## Usage

### Adding Profiles
```bash
guser-add work "Your Work Name" "work@company.com"
guser-add personal "Your Personal Name" "personal@email.com"
```

### Listing Profiles
```bash
guser-list
```

### Switching Profiles
```bash
guser-switch work      # Switch to work profile
guser-switch personal  # Switch to personal profile
```

### View Current User
```bash
guser-current
```

### Remove Profile
```bash
guser-remove work
```

### Help
```bash
guser-help
```

## Example Usage

```bash
# Add work profile
guser-add work "John Doe" "john@company.com"

# Add personal profile  
guser-add personal "John" "john@gmail.com"

# List profiles
guser-list

# Switch to work profile
guser-switch work

# Check current profile
guser-current
```

## Available Commands

| Command | Description |
|---------|-------------|
| `guser-add <profile> <name> <email>` | Add new profile |
| `guser-list` | List all profiles |
| `guser-switch <profile>` | Switch to profile |
| `guser-current` | Show current user |
| `guser-remove <profile>` | Remove profile |
| `guser-help` | Show help |

## Configuration

- Profiles are stored in: `~/.git-user-manager/profiles.json`
- Global git configuration is modified when switching profiles

## Requirements

- Python 3.6+
- Git (must be installed on system)
- macOS/Linux
