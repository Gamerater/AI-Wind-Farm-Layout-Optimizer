#!/usr/bin/env python3
"""
Quick Start Script for AI Wind Farm Optimizer

This script provides a quick demonstration of the visualization capabilities
for team members to get started immediately.
"""

import sys
import os
sys.path.append('.')

import numpy as np
import matplotlib.pyplot as plt
from src.visualization.basic_plots import WindFarmVisualizer
from src.visualization.interactive_plots import InteractiveVisualizer
from src.visualization.wind_analysis import WindDataVisualizer
from src.utils.data_generator import generate_sample_wind_data, generate_turbine_positions

def main():
    """Quick start demonstration."""
    print("🚀 AI Wind Farm Optimizer - Quick Start")
    print("=" * 50)
    
    # Generate sample data
    print("📊 Generating sample data...")
    wind_speeds, wind_directions, timestamps = generate_sample_wind_data(n_points=1000)
    turbine_positions = generate_turbine_positions(n_turbines=10, random_seed=42)
    
    # Initialize visualizers
    print("🎨 Initializing visualizers...")
    basic_viz = WindFarmVisualizer()
    interactive_viz = InteractiveVisualizer()
    wind_viz = WindDataVisualizer()
    
    # Create sample plots
    print("📈 Creating sample visualizations...")
    
    # 1. Wind data analysis
    fig1 = basic_viz.plot_wind_data(wind_speeds, wind_directions, 
                                   title="Quick Start - Wind Data Analysis")
    plt.savefig('results/plots/quick_start_wind_data.png', dpi=300, bbox_inches='tight')
    plt.close(fig1)
    
    # 2. Turbine layout
    fig2 = basic_viz.plot_turbine_layout(turbine_positions, 
                                        title="Quick Start - Turbine Layout")
    plt.savefig('results/plots/quick_start_turbine_layout.png', dpi=300, bbox_inches='tight')
    plt.close(fig2)
    
    # 3. Performance comparison
    methods = ['Grid', 'AI', 'Random']
    performance = [42.6, 47.8, 38.2]
    fig3 = basic_viz.plot_performance_comparison(methods, performance,
                                                title="Quick Start - Performance Comparison")
    plt.savefig('results/plots/quick_start_performance.png', dpi=300, bbox_inches='tight')
    plt.close(fig3)
    
    # 4. Wind rose
    fig4 = wind_viz.plot_wind_rose(wind_speeds, wind_directions, 
                                   title="Quick Start - Wind Rose")
    plt.savefig('results/plots/quick_start_wind_rose.png', dpi=300, bbox_inches='tight')
    plt.close(fig4)
    
    # 5. Interactive plot (save as HTML)
    fig5 = interactive_viz.create_interactive_wind_analysis(wind_speeds, wind_directions,
                                                           title="Quick Start - Interactive Analysis")
    interactive_viz.show_plot(fig5, 'results/plots/quick_start_interactive.html')
    
    print("✅ Quick start completed!")
    print("\n📁 Generated files:")
    print("   - results/plots/quick_start_wind_data.png")
    print("   - results/plots/quick_start_turbine_layout.png")
    print("   - results/plots/quick_start_performance.png")
    print("   - results/plots/quick_start_wind_rose.png")
    print("   - results/plots/quick_start_interactive.html")
    
    print("\n🎯 Next steps:")
    print("   1. Explore the generated plots")
    print("   2. Open the interactive HTML file in your browser")
    print("   3. Check out notebooks/visualization_demo.ipynb for detailed examples")
    print("   4. Start developing in your assigned module")
    
    print("\n📚 Documentation:")
    print("   - docs/TEAM_GUIDE.md - Team collaboration guide")
    print("   - docs/API_REFERENCE.md - API documentation")
    print("   - docs/DEVELOPMENT_GUIDE.md - Development guidelines")

if __name__ == "__main__":
    main() 