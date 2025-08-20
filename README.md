# Git User Manager

🚀 A Python-based tool for easily managing your git user profiles with simple commands.

## Features

- 🔄 Save multiple git profiles
- ⚡ Switch profiles with a single command  
- 📋 List saved profiles with active profile indicator
- 👤 View current git user
- 🗑️ Remove profiles
- 🍺 Easy installation via Homebrew
- 💻 Cross-platform (macOS/Linux)

## Installation

### Homebrew (Recommended)
```bash
# Add the tap
brew tap farukbey09/tap

# Install guser
brew install guser
```

### Manual Installation
```bash
# Download the script
curl -O https://raw.githubusercontent.com/farukbey09/guser/main/git-user-manager.py

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

After installation, you can use these commands:

| Command | Description |
|---------|-------------|
| `guser help` | Show main help menu |
| `guser-add <profile> <name> <email>` | Add new profile |
| `guser-list` | List all profiles (shows active profile with 👤) |
| `guser-switch <profile>` | Switch to profile |
| `guser-current` | Show current user |
| `guser-remove <profile>` | Remove profile |
| `guser-help` | Show help (same as `guser help`) |

## Real Usage Example

```bash
# Install via Homebrew
brew tap farukbey09/tap
brew install guser

# Add work profile
guser-add work "John Doe" "john@company.com"

# Add personal profile  
guser-add personal "John Smith" "john@gmail.com"

# List profiles (see which is active)
guser-list
# Output:
# 📋 Saved Profiles:
# --------------------------------------------------
# 🔹 work: John Doe <john@company.com> 👤 (Active)
# 🔹 personal: John Smith <john@gmail.com>

# Switch to personal profile
guser-switch personal

## Configuration

- **Profiles storage**: `~/.git-user-manager/profiles.json`
- **Git configuration**: Global git config is modified when switching profiles
- **No conflicts**: Safely switches between different git identities

## How It Works

1. **Save profiles**: Store multiple git user configurations with custom names
2. **Quick switching**: Change git user.name and user.email globally with one command
3. **Visual feedback**: See which profile is currently active with 👤 indicator
4. **Persistent storage**: Profiles are saved in JSON format for reliability

## Requirements

- **Python**: 3.6+ (automatically installed with Homebrew)
- **Git**: Must be installed on system
- **Platform**: macOS/Linux

## Contributing

Issues and pull requests are welcome on [GitHub](https://github.com/farukbey09/guser).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
