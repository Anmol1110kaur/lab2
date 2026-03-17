"""
Python Data Visualization Starter Code

This is a starter template for creating data visualizations using matplotlib
and plotly. Implement functions to visualize different types of data.

Implement the functions below to practice data visualization skills.

Key concepts to implement:
- Static plots with matplotlib
- Interactive plots with plotly
- Customizing plot appearance and styling
- Creating multi-chart layouts and dashboards
- Visualizing statistical relationships
"""

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict, Tuple, Optional
import pandas as pd


# ============================================================================
# TASK 1: Static Visualizations with Matplotlib
# ============================================================================

def plot_line_graph(x_data: List, y_data: List, 
                    title: str = "Line Plot", 
                    xlabel: str = "X-axis", 
                    ylabel: str = "Y-axis",
                    output_file: Optional[str] = None) -> None:
    """
    Create a line plot with customizable labels and save to file if specified
    
    Example:
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        plot_line_graph(x, y, title="Sales Data", xlabel="Month", ylabel="Sales")
    """
    # TODO: Create figure and plot line
    # TODO: Set title, x-label, y-label
    # TODO: Add grid and legend
    # TODO: Save to file if output_file is provided
    pass


def plot_bar_chart(categories: List[str], values: List[float],
                   title: str = "Bar Chart",
                   xlabel: str = "Categories",
                   ylabel: str = "Values",
                   colors: Optional[List[str]] = None,
                   output_file: Optional[str] = None) -> None:
    """
    Create a bar chart for categorical data
    
    Example:
        categories = ["Q1", "Q2", "Q3", "Q4"]
        values = [100, 250, 180, 300]
        plot_bar_chart(categories, values, title="Quarterly Sales")
    """
    # TODO: Create bar chart with categories and values
    # TODO: Apply colors if provided
    # TODO: Customize appearance and save if needed
    pass


def plot_histogram(data: List[float], 
                   bins: int = 10,
                   title: str = "Histogram",
                   xlabel: str = "Value",
                   ylabel: str = "Frequency",
                   output_file: Optional[str] = None) -> None:
    """
    Create a histogram to visualize data distribution
    
    Example:
        data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
        plot_histogram(data, bins=5, title="Score Distribution")
    """
    # TODO: Create histogram with specified bins
    # TODO: Add labels and customize appearance
    # TODO: Save to file if needed
    pass


def plot_scatter(x_data: List[float], y_data: List[float],
                 sizes: Optional[List[float]] = None,
                 colors: Optional[List] = None,
                 title: str = "Scatter Plot",
                 xlabel: str = "X-axis",
                 ylabel: str = "Y-axis",
                 output_file: Optional[str] = None) -> None:
    """
    Create a scatter plot with optional size and color variations
    
    Example:
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 6]
        sizes = [50, 100, 75, 150, 100]
        plot_scatter(x, y, sizes=sizes, title="Data Points")
    """
    # TODO: Create scatter plot with x and y data
    # TODO: Apply sizes and colors if provided
    # TODO: Customize and save as needed
    pass


def plot_subplots(data_dict: Dict[str, Tuple[List, List]],
                  titles: Dict[str, str],
                  layout: Tuple[int, int] = (2, 2),
                  output_file: Optional[str] = None) -> None:
    """
    Create multiple subplots in a single figure
    
    Args:
        data_dict: Dictionary mapping subplot names to (x_data, y_data) tuples
        titles: Dictionary mapping subplot names to titles
        layout: Tuple (rows, cols) for subplot grid
        output_file: Optional file path to save figure
    
    Example:
        data = {
            'plot1': ([1, 2, 3], [1, 2, 3]),
            'plot2': ([1, 2, 3], [3, 2, 1])
        }
        titles = {'plot1': 'Increasing', 'plot2': 'Decreasing'}
        plot_subplots(data, titles, layout=(1, 2))
    """
    # TODO: Create figure with subplots
    # TODO: Plot each dataset in its own subplot
    # TODO: Add titles and labels to each
    # TODO: Save if output_file is provided
    pass


def customize_plot_style(style_name: str = "seaborn") -> None:
    """
    Apply a specific matplotlib style to plots
    
    Available styles: 'default', 'seaborn', 'ggplot', 'bmh', 'fivethirtyeight'
    """
    # TODO: Set matplotlib style
    pass


# ============================================================================
# TASK 2: Interactive Visualizations with Plotly
# ============================================================================

def create_interactive_line(x_data: List, y_data: List,
                           title: str = "Interactive Line Plot",
                           xlabel: str = "X-axis",
                           ylabel: str = "Y-axis",
                           output_file: Optional[str] = None) -> go.Figure:
    """
    Create an interactive line plot with hover tooltips
    
    Example:
        x = [1, 2, 3, 4, 5]
        y = [10, 15, 13, 17, 20]
        fig = create_interactive_line(x, y, title="Stock Price")
        fig.show()
    """
    # TODO: Create plotly Figure with line trace
    # TODO: Add hover tooltips with data information
    # TODO: Customize layout with title and axis labels
    # TODO: Save to HTML file if output_file is provided
    # TODO: Return figure
    pass


def create_interactive_bar(categories: List[str], values: List[float],
                          title: str = "Interactive Bar Chart",
                          xlabel: str = "Categories",
                          ylabel: str = "Values",
                          output_file: Optional[str] = None) -> go.Figure:
    """
    Create an interactive bar chart with plotly
    
    Example:
        categories = ["Product A", "Product B", "Product C"]
        values = [100, 150, 120]
        fig = create_interactive_bar(categories, values, title="Sales by Product")
    """
    # TODO: Create plotly bar chart
    # TODO: Add interactive hover information
    # TODO: Save to HTML file if needed
    # TODO: Return figure
    pass


def create_scatter_with_colors(x_data: List[float], y_data: List[float],
                               colors: List,
                               title: str = "Interactive Scatter",
                               xlabel: str = "X-axis",
                               ylabel: str = "Y-axis",
                               output_file: Optional[str] = None) -> go.Figure:
    """
    Create an interactive scatter plot with color coding
    
    Example:
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 6]
        colors = ['red', 'blue', 'green', 'blue', 'red']
        fig = create_scatter_with_colors(x, y, colors, title="Colored Data Points")
    """
    # TODO: Create plotly scatter plot with color coding
    # TODO: Add hover tooltips
    # TODO: Customize layout
    # TODO: Save and return figure
    pass


def create_dropdown_chart(data_dict: Dict[str, Tuple[List, List]],
                         title: str = "Multi-Dataset Chart",
                         output_file: Optional[str] = None) -> go.Figure:
    """
    Create an interactive chart with dropdown menu to switch between datasets
    
    Args:
        data_dict: Dictionary mapping dataset names to (x_data, y_data) tuples
        title: Chart title
        output_file: Optional file path to save
    
    Example:
        data = {
            'Dataset1': ([1, 2, 3], [1, 2, 3]),
            'Dataset2': ([1, 2, 3], [3, 2, 1])
        }
        fig = create_dropdown_chart(data, title="Switch Datasets")
    """
    # TODO: Create figure with first dataset
    # TODO: Create traces for all datasets
    # TODO: Add dropdown buttons to switch between datasets
    # TODO: Save and return figure
    pass


def create_box_plot(data_dict: Dict[str, List[float]],
                   title: str = "Box Plot Comparison",
                   ylabel: str = "Values",
                   output_file: Optional[str] = None) -> go.Figure:
    """
    Create an interactive box plot for distribution comparison
    
    Example:
        data = {
            'Group A': [1, 2, 3, 4, 5],
            'Group B': [2, 3, 4, 5, 6, 7, 8]
        }
        fig = create_box_plot(data, title="Distribution Comparison")
    """
    # TODO: Create box plot traces for each group
    # TODO: Customize layout and styling
    # TODO: Save and return figure
    pass


def create_heatmap(data: List[List[float]],
                   x_labels: List[str],
                   y_labels: List[str],
                   title: str = "Heatmap",
                   output_file: Optional[str] = None) -> go.Figure:
    """
    Create an interactive heatmap
    
    Example:
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        x_labels = ['A', 'B', 'C']
        y_labels = ['X', 'Y', 'Z']
        fig = create_heatmap(data, x_labels, y_labels, title="Correlation Matrix")
    """
    # TODO: Create heatmap trace
    # TODO: Add x and y labels
    # TODO: Add colorbar and customize appearance
    # TODO: Save and return figure
    pass


# ============================================================================
# TASK 3: Data Analysis Visualization
# ============================================================================

def plot_correlation_matrix(dataframe: pd.DataFrame,
                           output_file: Optional[str] = None) -> None:
    """
    Create and display a correlation heatmap from a DataFrame
    
    Example:
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        plot_correlation_matrix(df, output_file="correlation.html")
    """
    # TODO: Calculate correlation matrix from DataFrame
    # TODO: Create heatmap visualization
    # TODO: Save to file if provided
    pass


def plot_pie_chart(labels: List[str], values: List[float],
                  title: str = "Pie Chart",
                  output_file: Optional[str] = None) -> None:
    """
    Create a pie chart for composition analysis
    
    Example:
        labels = ["Category A", "Category B", "Category C"]
        values = [30, 25, 45]
        plot_pie_chart(labels, values, title="Sales Distribution")
    """
    # TODO: Create pie chart using matplotlib or plotly
    # TODO: Add labels and percentages
    # TODO: Customize colors and appearance
    # TODO: Save if needed
    pass


def plot_grouped_bar_chart(groups: List[str], 
                          categories: List[str],
                          data_dict: Dict[str, List[float]],
                          title: str = "Grouped Bar Chart",
                          output_file: Optional[str] = None) -> None:
    """
    Create a grouped bar chart for multi-category comparison
    
    Example:
        groups = ["Q1", "Q2", "Q3"]
        categories = ["Product A", "Product B"]
        data = {"Product A": [100, 150, 200], "Product B": [120, 140, 180]}
        plot_grouped_bar_chart(groups, categories, data)
    """
    # TODO: Create grouped bar chart
    # TODO: Organize bars by group and category
    # TODO: Add legend and labels
    # TODO: Save if needed
    pass


def plot_distribution_with_stats(data: List[float],
                                title: str = "Distribution",
                                output_file: Optional[str] = None) -> None:
    """
    Create histogram with statistical overlays (mean line, std dev shading)
    
    Example:
        data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
        plot_distribution_with_stats(data, title="Score Distribution")
    """
    # TODO: Create histogram
    # TODO: Add mean line
    # TODO: Add standard deviation shading
    # TODO: Add statistics annotations
    # TODO: Save if needed
    pass


def plot_trend_line(x_data: List[float], y_data: List[float],
                   title: str = "Trend Analysis",
                   output_file: Optional[str] = None) -> None:
    """
    Create scatter plot with trend line (linear regression)
    
    Example:
        x = [1, 2, 3, 4, 5]
        y = [2.1, 3.9, 6.2, 8.1, 10.2]
        plot_trend_line(x, y, title="Growth Trend")
    """
    # TODO: Create scatter plot
    # TODO: Calculate and plot trend line
    # TODO: Add equation and R-squared value
    # TODO: Save if needed
    pass


# ============================================================================
# TASK 4: Dashboard and Multi-Chart Layouts
# ============================================================================

def create_matplotlib_dashboard(datasets: Dict[str, Dict],
                               layout: Tuple[int, int] = (2, 2),
                               title: str = "Dashboard",
                               output_file: Optional[str] = None) -> None:
    """
    Create a comprehensive dashboard with multiple matplotlib plots
    
    Args:
        datasets: Dictionary with plot info: {'plot_name': {'type': 'line', 'data': {...}}}
        layout: Subplot grid layout (rows, cols)
        title: Dashboard title
        output_file: Optional file path to save
    
    Example:
        datasets = {
            'sales': {'type': 'line', 'x': [...], 'y': [...]},
            'regions': {'type': 'bar', 'categories': [...], 'values': [...]}
        }
        create_matplotlib_dashboard(datasets)
    """
    # TODO: Create figure with required subplots
    # TODO: Create each plot based on type and data
    # TODO: Apply consistent styling
    # TODO: Save if needed
    pass


def create_plotly_dashboard(datasets: Dict[str, Dict],
                           layout: Tuple[int, int] = (2, 2),
                           title: str = "Interactive Dashboard",
                           output_file: Optional[str] = None) -> go.Figure:
    """
    Create an interactive Plotly dashboard with multiple subplots
    
    Example:
        datasets = {
            'sales': {'type': 'line', 'x': [...], 'y': [...]},
            'distribution': {'type': 'histogram', 'data': [...]}
        }
        fig = create_plotly_dashboard(datasets, title="Dashboard")
    """
    # TODO: Create figure with subplots
    # TODO: Add traces based on dataset types
    # TODO: Configure layout and styling
    # TODO: Save and return figure
    pass


def create_summary_dashboard(dataframe: pd.DataFrame,
                            output_file: Optional[str] = None) -> None:
    """
    Create a summary dashboard from a DataFrame with key metrics and visualizations
    
    Should include:
    - Summary statistics table
    - Distribution histograms
    - Correlation heatmap
    - Time series if available
    
    Example:
        df = pd.read_csv("data.csv")
        create_summary_dashboard(df, output_file="summary.html")
    """
    # TODO: Extract key metrics and statistics
    # TODO: Create multiple visualizations
    # TODO: Arrange in dashboard layout
    # TODO: Save HTML file
    pass


if __name__ == "__main__":
    # Example usage and testing
    print("Data Visualization Assignment")
    print("==============================")
    
    # TODO: Add test code here to verify your implementations
    # Example:
    # x = [1, 2, 3, 4, 5]
    # y = [2, 4, 6, 8, 10]
    # plot_line_graph(x, y, title="Test Plot", output_file="test.png")
