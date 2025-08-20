#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Git User Manager - Easy management of git user profiles
"""

import os
import json
import subprocess
import sys
from pathlib import Path

class GitUserManager:
    def __init__(self):
        self.config_dir = Path.home() / '.git-user-manager'
        self.config_file = self.config_dir / 'profiles.json'
        self.ensure_config_dir()
        
    def ensure_config_dir(self):
        """Create configuration directory"""
        self.config_dir.mkdir(exist_ok=True)
        if not self.config_file.exists():
            self.save_profiles({})
    
    def load_profiles(self):
        """Load profiles"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_profiles(self, profiles):
        """Save profiles"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(profiles, f, indent=2, ensure_ascii=False)
    
    def run_git_command(self, command):
        """Run git command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
        except Exception as e:
            return False, "", str(e)
    
    def get_current_user(self):
        """Get current git user"""
        success_name, name, _ = self.run_git_command("git config --global user.name")
        success_email, email, _ = self.run_git_command("git config --global user.email")
        
        if success_name and success_email:
            return name, email
        return None, None
    
    def set_git_user(self, name, email):
        """Set git user"""
        commands = [
            f'git config --global user.name "{name}"',
            f'git config --global user.email "{email}"'
        ]
        
        for cmd in commands:
            success, _, error = self.run_git_command(cmd)
            if not success:
                print(f"❌ Error: {error}")
                return False
        return True
    
    def add_profile(self, profile_name, name, email):
        """Add new profile"""
        profiles = self.load_profiles()
        profiles[profile_name] = {
            'name': name,
            'email': email
        }
        self.save_profiles(profiles)
        print(f"✅ Profile '{profile_name}' added!")
    
    def remove_profile(self, profile_name):
        """Remove profile"""
        profiles = self.load_profiles()
        if profile_name in profiles:
            del profiles[profile_name]
            self.save_profiles(profiles)
            print(f"✅ Profile '{profile_name}' removed!")
        else:
            print(f"❌ Profile '{profile_name}' not found!")
    
    def list_profiles(self):
        """List profiles"""
        profiles = self.load_profiles()
        current_name, current_email = self.get_current_user()
        
        print("\n📋 Saved Profiles:")
        print("-" * 50)
        
        if not profiles:
            print("❌ No profiles added yet.")
            return
        
        for profile_name, profile_data in profiles.items():
            name = profile_data['name']
            email = profile_data['email']
            
            # Mark current profile
            current_marker = "👤 (Active)" if (name == current_name and email == current_email) else ""
            
            print(f"🔹 {profile_name}: {name} <{email}> {current_marker}")
    
    def switch_profile(self, profile_name):
        """Switch profile"""
        profiles = self.load_profiles()
        
        if profile_name not in profiles:
            print(f"❌ Profile '{profile_name}' not found!")
            self.list_profiles()
            return
        
        profile = profiles[profile_name]
        name = profile['name']
        email = profile['email']
        
        if self.set_git_user(name, email):
            print(f"✅ Git user switched to '{profile_name}' profile!")
            print(f"👤 {name} <{email}>")
        else:
            print("❌ Failed to switch git user!")
    
    def show_current(self):
        """Show current git user"""
        name, email = self.get_current_user()
        
        if name and email:
            print(f"\n👤 Current Git User:")
            print(f"📛 Name: {name}")
            print(f"📧 Email: {email}")
        else:
            print("❌ Git user information not found!")
    
    def show_help(self):
        """Show help menu"""
        print("""
🚀 Git User Manager - Help

Usage:
  python git-user-manager.py <command> [parameters]

Commands:
  add <profile_name> <name> <email>  - Add new profile
  remove <profile_name>              - Remove profile  
  list                               - List profiles
  switch <profile_name>              - Switch profile
  current                            - Show current user
  help                               - Show this help menu

Examples:
  python git-user-manager.py add work "Work Name" "work@company.com"
  python git-user-manager.py add personal "Personal Name" "personal@email.com"
  python git-user-manager.py switch work
  python git-user-manager.py list
  python git-user-manager.py current
""")

def main():
    manager = GitUserManager()
    
    if len(sys.argv) < 2:
        manager.show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'add':
        if len(sys.argv) != 5:
            print("❌ Usage: add <profile_name> <name> <email>")
            return
        profile_name, name, email = sys.argv[2], sys.argv[3], sys.argv[4]
        manager.add_profile(profile_name, name, email)
        
    elif command == 'remove':
        if len(sys.argv) != 3:
            print("❌ Usage: remove <profile_name>")
            return
        profile_name = sys.argv[2]
        manager.remove_profile(profile_name)
        
    elif command == 'list':
        manager.list_profiles()
        
    elif command == 'switch':
        if len(sys.argv) != 3:
            print("❌ Usage: switch <profile_name>")
            return
        profile_name = sys.argv[2]
        manager.switch_profile(profile_name)
        
    elif command == 'current':
        manager.show_current()
        
    elif command == 'help':
        manager.show_help()
        
    else:
        print(f"❌ Unknown command: {command}")
        manager.show_help()

if __name__ == "__main__":
    main()
