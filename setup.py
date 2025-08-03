#!/usr/bin/env python3
"""
Setup script for AI Wind Farm Optimizer.

This script initializes the project structure, creates necessary directories,
and sets up the development environment for team collaboration.
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """Print project setup banner."""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    AI Wind Farm Optimizer                    ║
    ║                        Setup Script                          ║
    ║                                                              ║
    ║  Team Members:                                               ║
    ║  • Yuvraj Singh Shekhawat: Physics & ML Specialist           ║
    ║  • Kaushal Yadav: Environment & Systems Specialist           ║
    ║  • Daksh Bansal: Data Visualization Specialist               ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required.")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    else:
        print(f"✅ Python version: {sys.version.split()[0]}")

def create_project_structure():
    """Create the complete project directory structure."""
    print("\n📁 Creating project structure...")
    
    directories = [
        'src/models',
        'src/data', 
        'src/visualization',
        'src/utils',
        'notebooks',
        'tests',
        'results/plots',
        'data',
        'models',
        'logs',
        'docs'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   Created: {directory}/")

def create_init_files():
    """Create __init__.py files for Python packages."""
    print("\n📄 Creating package initialization files...")
    
    init_files = [
        'src/__init__.py',
        'src/models/__init__.py',
        'src/data/__init__.py', 
        'src/visualization/__init__.py',
        'src/utils/__init__.py'
    ]
    
    for init_file in init_files:
        Path(init_file).touch(exist_ok=True)
        print(f"   Created: {init_file}")

def install_dependencies():
    """Install project dependencies."""
    print("\n📦 Installing dependencies...")
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        print("   Please install dependencies manually:")
        print("   pip install -r requirements.txt")

def run_tests():
    """Run the test suite."""
    print("\n🧪 Running tests...")
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pytest', 'tests/', '-v'])
        print("✅ Tests passed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Some tests failed: {e}")
        print("   This is normal for initial setup - tests will be added by team members")

def create_sample_data():
    """Create sample data for development."""
    print("\n📊 Creating sample data...")
    
    try:
        from src.utils.data_generator import create_sample_dataset
        create_sample_dataset()
        print("✅ Sample data created")
    except ImportError as e:
        print(f"⚠️  Could not create sample data: {e}")

def create_team_documentation():
    """Create team collaboration documentation."""
    print("\n📚 Creating team documentation...")
    
    docs = {
        'docs/TEAM_GUIDE.md': """# Team Collaboration Guide

## Quick Start for Team Members

### Member 1 (Physics & ML Specialist)
1. Work in `src/models/` directory
2. Implement Jensen wake model in `wake_models.py`
3. Create power calculations in `power_calculations.py`
4. Test your models using the visualization tools

### Member 2 (Environment & Systems Specialist)  
1. Work in `src/models/` directory
2. Implement RL environment in `rl_environment.py`
3. Create optimization algorithms
4. Integrate with Member 1's physics models

### Member 3 (Data Visualization Specialist)
1. Work in `src/visualization/` directory
2. Enhance visualization capabilities
3. Create interactive dashboards
4. Support team with data analysis

## Development Workflow
1. Create feature branches for your work
2. Test your code before committing
3. Use the visualization tools for validation
4. Update documentation as needed

## Testing
- Run tests: `python -m pytest tests/ -v`
- Create new tests in `tests/` directory
- Ensure all functions have test coverage

## Configuration
- Modify `config.yaml` for project parameters
- Use `src/utils/config_loader.py` to access config
- Update requirements.txt for new dependencies
""",
        
        'docs/API_REFERENCE.md': """# API Reference

## Visualization Module

### WindFarmVisualizer
Main visualization class for wind farm analysis.

```python
from src.visualization.basic_plots import WindFarmVisualizer

viz = WindFarmVisualizer()

# Plot wind data
viz.plot_wind_data(wind_speeds, wind_directions)

# Plot turbine layout
viz.plot_turbine_layout(turbine_positions)

# Compare performance
viz.plot_performance_comparison(methods, performance_values)
```

### InteractiveVisualizer
Interactive Plotly-based visualizations.

```python
from src.visualization.interactive_plots import InteractiveVisualizer

interactive_viz = InteractiveVisualizer()

# Create interactive plots
fig = interactive_viz.create_interactive_wind_analysis(wind_speeds, wind_directions)
interactive_viz.show_plot(fig)
```

### WindDataVisualizer
Specialized wind data analysis.

```python
from src.visualization.wind_analysis import WindDataVisualizer

wind_viz = WindDataVisualizer()

# Create wind rose
wind_viz.plot_wind_rose(wind_speeds, wind_directions)

# Analyze Weibull distribution
wind_viz.plot_weibull_analysis(wind_speeds)
```

## Utility Functions

### Data Generation
```python
from src.utils.data_generator import generate_sample_wind_data

wind_speeds, wind_directions, timestamps = generate_sample_wind_data()
```

### Configuration
```python
from src.utils.config_loader import ConfigLoader

config = ConfigLoader()
farm_config = config.get_wind_farm_config()
```
""",
        
        'docs/DEVELOPMENT_GUIDE.md': """# Development Guide

## Environment Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-wind-farm-optimizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run setup script**
   ```bash
   python setup.py
   ```

## Project Structure

```
ai-wind-farm-optimizer/
├── src/
│   ├── models/           # Physics & ML models
│   ├── data/             # Data management
│   ├── visualization/    # Visualization tools
│   └── utils/            # Shared utilities
├── notebooks/            # Development & demos
├── tests/                # Test suite
├── results/              # Output storage
├── docs/                 # Documentation
├── requirements.txt      # Dependencies
└── config.yaml          # Configuration
```

## Coding Standards

- Use type hints for all function parameters
- Write docstrings for all functions and classes
- Follow PEP 8 style guidelines
- Add tests for new functionality
- Update documentation as needed

## Testing

- Write unit tests for all functions
- Use pytest for testing framework
- Aim for >80% code coverage
- Test edge cases and error conditions

## Configuration Management

- Use `config.yaml` for all parameters
- Access config through `ConfigLoader` class
- Validate configuration on startup
- Document all configuration options

## Data Management

- Store sample data in `data/` directory
- Use synthetic data for testing
- Implement data validation
- Document data formats and schemas
"""
    }
    
    for filepath, content in docs.items():
        Path(filepath).write_text(content)
        print(f"   Created: {filepath}")

def main():
    """Main setup function."""
    print_banner()
    
    # Check Python version
    check_python_version()
    
    # Create project structure
    create_project_structure()
    create_init_files()
    
    # Install dependencies
    install_dependencies()
    
    # Create documentation
    create_team_documentation()
    
    # Create sample data
    create_sample_data()
    
    # Run tests
    run_tests()
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Activate your virtual environment")
    print("2. Explore the notebooks/ directory for examples")
    print("3. Check docs/ directory for team guides")
    print("4. Start developing in your assigned module")
    print("\nHappy coding! 🚀")

if __name__ == "__main__":
    main() 