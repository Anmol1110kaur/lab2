# 📘 Assignment: Python Data Visualization

## 🎯 Objective

Learn to create effective data visualizations using matplotlib and plotly. Master different chart types, customize visual elements, and present data insights through interactive and static graphics.

## 📝 Tasks

### 🛠️ Static Visualizations with Matplotlib

#### Description
Create static charts and graphs using matplotlib to visualize different data types and relationships. Customize plots with labels, legends, colors, and styling.

#### Requirements
Completed program should:

- Create line plots for time series data with proper labels and legends
- Generate bar charts for categorical data comparisons
- Build histograms to visualize distributions
- Create scatter plots with color coding and size variations
- Plot multiple subplots in a single figure
- Customize plot appearance: titles, axis labels, grid, colors, fonts
- Save plots to files (PNG, PDF formats)
- Create plots with different figure sizes and resolutions
- Use different plot styles (line styles, markers, colors)
- Example usage:
  ```python
  plot_line_graph(x_data, y_data, title="Sales Over Time", 
                  xlabel="Month", ylabel="Revenue")
  ```

### 🛠️ Interactive Visualizations with Plotly

#### Description
Create interactive, web-based visualizations using plotly that allow users to hover, zoom, and explore data dynamically.

#### Requirements
Completed program should:

- Create interactive line, bar, and scatter plots
- Add hover tooltips with relevant data information
- Implement zoom and pan functionality
- Create dropdown menus to filter/switch between datasets
- Build interactive histograms and box plots
- Generate heatmaps and correlation matrices
- Export interactive plots as HTML files
- Combine multiple traces in a single interactive plot
- Customize layout, fonts, and colors for consistency
- Example usage:
  ```python
  interactive_sales_chart(sales_data, regions=["East", "West", "North"])
  ```

### 🛠️ Data Analysis Visualization

#### Description
Visualize statistical analyses and data insights to communicate findings effectively through charts and graphs.

#### Requirements
Completed program should:

- Create distribution plots (histograms, KDE plots, box plots)
- Generate correlation heatmaps from datasets
- Build pie charts for composition analysis
- Create grouped and stacked bar charts for comparisons
- Visualize multiple variables with appropriate chart types
- Add statistical elements: mean lines, trend lines, confidence intervals
- Create comparative visualizations (before/after, multiple categories)
- Handle missing data appropriately in visualizations
- Create publication-ready plots with proper formatting
- Example usage:
  ```python
  visualize_correlations(dataframe, output_file="correlation.html")
  ```

### 🛠️ Dashboard and Multi-Chart Layouts

#### Description
Combine multiple visualizations into cohesive dashboards and layouts for comprehensive data presentation.

#### Requirements
Completed program should:

- Create multi-chart dashboards with matplotlib subplots
- Build interactive dashboards with plotly that update based on user input
- Organize charts in meaningful layouts (grids, columns, rows)
- Apply consistent styling across all visualizations
- Create summary visualizations with key metrics
- Add annotations and insights to charts
- Design responsive layouts that work across different screen sizes
- Export complete dashboards as HTML or image files
- Include legends, color schemes, and titles for clarity
