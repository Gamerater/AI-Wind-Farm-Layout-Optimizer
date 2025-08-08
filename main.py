#!/usr/bin/env python3
"""
Main application for the AI Wind Farm Optimizer Prototype.

This script demonstrates the core functionality of the wind farm optimizer
including data generation, analysis, optimization, and visualization.
"""

import sys
import os
import logging
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / 'src'))

from src.utils.config_loader import ConfigLoader
from src.utils.file_utils import FileUtils
from src.data.wind_data import WindDataProcessor
from src.data.data_generator import DataGenerator
from src.visualization.basic_plots import WindFarmVisualizer
from src.visualization.interactive_plots import InteractiveVisualizer
from src.visualization.wind_analysis import WindDataVisualizer


def print_banner():
    """Print application banner."""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                AI Wind Farm Optimizer Prototype              ║
    ║                                                              ║
    ║  Features:                                                   ║
    ║  • Wind data generation and analysis                        ║
    ║  • Turbine placement optimization                           ║
    ║  • Advanced visualization capabilities                       ║
    ║  • Performance evaluation and comparison                     ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    """Main application function."""
    print_banner()
    
    # Initialize components
    print("🔧 Initializing components...")
    
    # Load configuration
    config_loader = ConfigLoader("config.yaml")
    if not config_loader.validate_config():
        print("❌ Configuration validation failed")
        return
    
    # Initialize utilities
    file_utils = FileUtils()
    
    # Initialize data processors
    wind_processor = WindDataProcessor(config_loader.get_wind_data_config())
    data_generator = DataGenerator(config_loader.get_wind_farm_config())
    
    # Initialize visualizers
    viz_config = config_loader.get_visualization_config()
    basic_viz = WindFarmVisualizer(viz_config)
    interactive_viz = InteractiveVisualizer(viz_config)
    wind_viz = WindDataVisualizer(viz_config)
    
    print("✅ Components initialized successfully")
    
    # Generate sample data
    print("\n📊 Generating sample data...")
    
    # Generate wind data
    wind_speeds, wind_directions = wind_processor.generate_time_series_data(
        n_points=1000, random_state=42
    )
    
    # Generate turbine positions
    turbine_positions = data_generator.generate_turbine_positions(
        n_turbines=12, method='optimized', random_state=42
    )
    
    # Generate optimization data
    optimization_data = data_generator.generate_sample_optimization_data(
        n_scenarios=5, random_state=42
    )
    
    print(f"✅ Generated {len(wind_speeds)} wind data points")
    print(f"✅ Generated {len(turbine_positions)} turbine positions")
    print(f"✅ Generated {len(optimization_data['scenarios'])} optimization scenarios")
    
    # Analyze wind data
    print("\n📈 Analyzing wind data...")
    
    wind_summary = wind_processor.get_wind_data_summary(wind_speeds, wind_directions)
    
    print(f"   Mean wind speed: {wind_summary['wind_speed_analysis']['mean']:.2f} m/s")
    print(f"   Power density: {wind_summary['power_density_w_m2']:.0f} W/m²")
    print(f"   Capacity factor: {wind_summary['capacity_factor']:.3f}")
    
    # Create visualizations
    print("\n🎨 Creating visualizations...")
    
    # 1. Wind data analysis
    fig1 = basic_viz.plot_wind_data(
        wind_speeds, wind_directions, 
        title="Wind Data Analysis - Prototype"
    )
    file_utils.save_plot(fig1, "results/plots/wind_data_analysis.png")
    
    # 2. Turbine layout
    fig2 = basic_viz.plot_turbine_layout(
        turbine_positions, 
        title="Wind Farm Layout - Prototype"
    )
    file_utils.save_plot(fig2, "results/plots/turbine_layout.png")
    
    # 3. Performance comparison
    comparison = optimization_data['comparison']
    fig3 = basic_viz.plot_performance_comparison(
        comparison['methods'], 
        comparison['power_outputs'],
        title="Performance Comparison - Prototype"
    )
    file_utils.save_plot(fig3, "results/plots/performance_comparison.png")
    
    # 4. Wind rose
    fig4 = wind_viz.plot_wind_rose(
        wind_speeds, wind_directions,
        title="Wind Rose - Prototype"
    )
    file_utils.save_plot(fig4, "results/plots/wind_rose.png")
    
    # 5. Optimization results
    fig5 = basic_viz.plot_optimization_results(
        optimization_data,
        title="Optimization Results - Prototype"
    )
    file_utils.save_plot(fig5, "results/plots/optimization_results.png")
    
    # 6. Interactive visualization
    fig6 = interactive_viz.create_interactive_wind_analysis(
        wind_speeds, wind_directions,
        title="Interactive Wind Analysis - Prototype"
    )
    file_utils.save_interactive_plot(fig6, "results/plots/interactive_analysis.html")
    
    # 7. Dashboard
    fig7 = basic_viz.create_summary_dashboard(
        wind_speeds, wind_directions, turbine_positions, optimization_data,
        title="Wind Farm Dashboard - Prototype"
    )
    file_utils.save_plot(fig7, "results/plots/dashboard.png")
    
    print("✅ All visualizations created successfully")
    
    # Save results
    print("\n💾 Saving results...")
    
    # Save wind data
    wind_data_df = wind_processor.create_wind_data_dataframe(
        wind_speeds, wind_directions
    )
    file_utils.save_data(wind_data_df, "data/wind_data.csv", "csv")
    
    # Save optimization results
    file_utils.save_results(optimization_data, "optimization_results")
    
    # Save turbine positions
    file_utils.save_data(turbine_positions, "data/turbine_positions.json", "json")
    
    print("✅ Results saved successfully")
    
    # Print summary
    print("\n📋 Summary:")
    print("=" * 50)
    print(f"   Wind data points: {len(wind_speeds)}")
    print(f"   Turbine positions: {len(turbine_positions)}")
    print(f"   Optimization scenarios: {len(optimization_data['scenarios'])}")
    print(f"   Generated plots: 7")
    print(f"   Saved files: 4")
    
    print("\n📁 Generated files:")
    print("   - results/plots/wind_data_analysis.png")
    print("   - results/plots/turbine_layout.png")
    print("   - results/plots/performance_comparison.png")
    print("   - results/plots/wind_rose.png")
    print("   - results/plots/optimization_results.png")
    print("   - results/plots/interactive_analysis.html")
    print("   - results/plots/dashboard.png")
    print("   - data/wind_data.csv")
    print("   - data/turbine_positions.json")
    print("   - results/optimization_results_*.json")
    
    print("\n🎯 Next steps:")
    print("   1. Explore the generated plots in results/plots/")
    print("   2. Open interactive_analysis.html in your browser")
    print("   3. Check the data files in data/")
    print("   4. Modify config.yaml to experiment with different parameters")
    print("   5. Extend the functionality in src/ modules")
    
    print("\n🚀 Prototype demonstration completed successfully!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Application interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        logging.error(f"Application error: {e}", exc_info=True)
        sys.exit(1) 