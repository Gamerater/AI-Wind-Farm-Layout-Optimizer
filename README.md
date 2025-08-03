# AI Wind Farm Optimization Project

A collaborative AI system for optimizing wind turbine placement to maximize power output using machine learning techniques.

## Team Members
- **Yuvraj Singh Shekhawat**: Physics & ML Specialist (Jensen wake model, power calculations)
- **Kaushal Yadav**: Environment & Systems Specialist (Reinforcement Learning environment)
- **Daksh Bansal**: Data Visualization Specialist (Visualization and analysis tools)

## Project Overview

This project implements an AI-driven wind farm optimization system that:
- Analyzes wind resource data and patterns
- Optimizes turbine placement using machine learning
- Visualizes results and performance comparisons
- Provides interactive tools for wind farm planning

## Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-wind-farm-optimizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run setup script**
   ```bash
   python setup.py
   ```

5. **Test installation**
   ```bash
   python -m pytest tests/ -v
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

## Core Features

### Visualization Module
- Wind resource analysis plots
- 2D turbine layout visualization
- Performance comparison charts
- Interactive Plotly visualizations

### Example Usage

```python
from src.visualization.basic_plots import WindFarmVisualizer

# Initialize visualizer
viz = WindFarmVisualizer()

# Plot turbine layout
turbine_positions = [(100, 200), (300, 400), (500, 600)]
viz.plot_turbine_layout(turbine_positions)

# Compare optimization methods
methods = ['Grid', 'AI', 'Random']
performance = [42.6, 47.8, 38.2]
viz.plot_performance_comparison(methods, performance)
```

## Development Workflow

1. **Environment Setup**: Use the provided setup scripts
2. **Development**: Work in `notebooks/` for exploration
3. **Testing**: Run tests before committing changes
4. **Documentation**: Update docs for new features

## Team Collaboration

- **Member 1**: Focus on physics models in `src/models/`
- **Member 2**: Develop RL environment in `src/models/`
- **Member 3**: Enhance visualizations in `src/visualization/`

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Contact


For questions or issues, please create an issue in the repository. 
