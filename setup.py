#!/usr/bin/env python3
"""
Setup script for the AI Wind Farm Optimizer Prototype.

This script helps users set up the environment and run the prototype.
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """Print setup banner."""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                AI Wind Farm Optimizer Prototype              ║
    ║                        Setup Script                          ║
    ║                                                              ║
    ║  This script will help you set up the prototype environment ║
    ║  and run the demonstration.                                 ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required.")
        print(f"   Current version: {sys.version}")
        return False
    else:
        print(f"✅ Python version: {sys.version.split()[0]}")
        return True

def install_dependencies():
    """Install project dependencies."""
    print("\n📦 Installing dependencies...")
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        print("   Please install dependencies manually:")
        print("   pip install -r requirements.txt")
        return False

def create_directories():
    """Create necessary directories."""
    print("\n📁 Creating directories...")
    
    directories = [
        'data',
        'results',
        'results/plots',
        'models',
        'logs',
        'notebooks',
        'tests'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   Created: {directory}/")

def run_tests():
    """Run the test suite."""
    print("\n🧪 Running tests...")
    
    try:
        subprocess.check_call([sys.executable, 'test_prototype.py'])
        print("✅ Tests passed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed: {e}")
        return False

def run_prototype():
    """Run the prototype."""
    print("\n🚀 Running prototype...")
    
    try:
        subprocess.check_call([sys.executable, 'main.py'])
        print("✅ Prototype completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Prototype failed: {e}")
        return False

def main():
    """Main setup function."""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Install dependencies
    if not install_dependencies():
        print("\n⚠️  Please install dependencies manually and try again.")
        sys.exit(1)
    
    # Run tests
    if not run_tests():
        print("\n⚠️  Tests failed. Please check the errors above.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    # Ask user if they want to run the prototype
    print("\n🎯 Setup completed successfully!")
    print("\nOptions:")
    print("1. Run the full prototype demonstration")
    print("2. Run tests only")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == '1':
        run_prototype()
    elif choice == '2':
        run_tests()
    elif choice == '3':
        print("👋 Goodbye!")
    else:
        print("Invalid choice. Exiting.")
    
    print("\n📚 Next steps:")
    print("   • Explore the generated plots in results/plots/")
    print("   • Open interactive_analysis.html in your browser")
    print("   • Check the data files in data/")
    print("   • Modify config.yaml to experiment with different parameters")
    print("   • Extend the functionality in src/ modules")

if __name__ == "__main__":
    main() 