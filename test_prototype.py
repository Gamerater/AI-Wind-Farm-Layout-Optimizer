#!/usr/bin/env python3
"""
Simple test script for the AI Wind Farm Optimizer Prototype.

This script tests the basic functionality without running the full application.
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / 'src'))

def test_imports():
    """Test that all modules can be imported."""
    print("🧪 Testing imports...")
    
    try:
        from src.utils.config_loader import ConfigLoader
        from src.utils.file_utils import FileUtils
        from src.data.wind_data import WindDataProcessor
        from src.data.data_generator import DataGenerator
        from src.visualization.basic_plots import WindFarmVisualizer
        from src.visualization.interactive_plots import InteractiveVisualizer
        from src.visualization.wind_analysis import WindDataVisualizer
        
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_config_loader():
    """Test configuration loader."""
    print("\n🔧 Testing configuration loader...")
    
    try:
        config_loader = ConfigLoader("config.yaml")
        print(f"✅ Configuration loaded successfully")
        print(f"   Wind farm width: {config_loader.get('wind_farm.farm_width')} m")
        print(f"   Weibull k: {config_loader.get('wind_data.weibull_k')}")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_data_generation():
    """Test data generation."""
    print("\n📊 Testing data generation...")
    
    try:
        wind_processor = WindDataProcessor()
        wind_speeds, wind_directions = wind_processor.generate_time_series_data(n_points=100)
        
        print(f"✅ Generated {len(wind_speeds)} wind data points")
        print(f"   Mean wind speed: {wind_speeds.mean():.2f} m/s")
        print(f"   Mean direction: {wind_directions.mean():.1f}°")
        return True
    except Exception as e:
        print(f"❌ Data generation error: {e}")
        return False

def test_visualization():
    """Test visualization."""
    print("\n🎨 Testing visualization...")
    
    try:
        # Generate test data
        wind_processor = WindDataProcessor()
        wind_speeds, wind_directions = wind_processor.generate_time_series_data(n_points=100)
        
        # Test basic visualizer
        basic_viz = WindFarmVisualizer()
        fig = basic_viz.plot_wind_data(wind_speeds, wind_directions, title="Test Plot")
        plt.close(fig)  # Close to free memory
        
        print("✅ Basic visualization successful")
        return True
    except Exception as e:
        print(f"❌ Visualization error: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 AI Wind Farm Optimizer Prototype - Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_config_loader,
        test_data_generation,
        test_visualization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📋 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Prototype is ready to run.")
        print("\nTo run the full prototype:")
        print("   python main.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    success = main()
    sys.exit(0 if success else 1) 