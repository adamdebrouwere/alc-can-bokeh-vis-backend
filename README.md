# Alcohol and Cannabis Data Analysis - Django Views

This project contains a set of Django views that generate various visualizations related to alcohol and cannabis consumption and market trends in Canada. The views process data, generate responses using the `generate_response` function, and return JSON responses with dynamic data visualizations.

## Features

- **Alcohol Use by Age Range**: Visualizes alcohol consumption across different age groups from 2013 to 2023.
- **Cannabis Use by Age Range**: Displays cannabis consumption across age groups from 2013 to 2023.
- **Alcohol Product Market Share**: Shows the market share of alcohol products.
- **Cannabis Product Market Share**: Displays the market share of cannabis products.
- **Alcohol Yearly Sales**: Visualizes yearly sales data for alcohol.
- **Cannabis Yearly Sales**: Visualizes yearly sales data for cannabis.
- **Combined Sales Growth (Line Chart)**: Compares the sales growth of alcohol and cannabis.
- **Combined Sales Growth (Bar Chart)**: Shows the combined sales growth for alcohol and cannabis in a bar chart format.

## Views

### `alcohol_use_view(request)`
This view generates a plot for **alcohol use by age range** from 2013 to 2023.

- **Data**: Alcohol consumption data categorized by age range (15-19, 20-24, 25+).
- **Plot**: Line plot showing alcohol use by age group.

### `cannabis_use_view(request)`
This view generates a plot for **cannabis use by age range** from 2013 to 2023.

- **Data**: Cannabis consumption data categorized by age range (15-19, 20-24, 25+).
- **Plot**: Line plot showing cannabis use by age group.

### `alcohol_product_market_share_view(request)`
This view generates a pie chart visualizing the **market share of alcohol products**.

- **Data**: CSV data containing market share of alcohol products.
- **Plot**: Pie chart of alcohol product market share.

### `cannabis_product_market_share_view(request)`
This view generates a pie chart visualizing the **market share of cannabis products**.

- **Data**: CSV data containing market share of cannabis products.
- **Plot**: Pie chart of cannabis product market share.

### `alcohol_yearly_sales_view(request)`
This view generates a line graph of **yearly alcohol sales** data.

- **Data**: CSV data containing yearly alcohol sales.
- **Plot**: Line graph of alcohol sales over the years.

### `cannabis_yearly_sales_view(request)`
This view generates a line graph of **yearly cannabis sales** data.

- **Data**: CSV data containing yearly cannabis sales.
- **Plot**: Line graph of cannabis sales over the years.

### `combined_sales_growth_line_plot_view(request)`
This view generates a **combined sales growth line graph** for alcohol and cannabis.

- **Data**: CSV data for both alcohol and cannabis sales.
- **Plot**: Line graph comparing the sales growth of alcohol and cannabis over time.

### `combined_sales_growth_bar_chart_view(request)`
This view generates a **combined sales growth bar chart** for alcohol and cannabis.

- **Data**: CSV data for both alcohol and cannabis sales.
- **Plot**: Bar chart comparing the sales growth of alcohol and cannabis over time.

## Utilities

### `generate_response`
This utility function is responsible for generating a response based on the provided plot generation function, data, and title. It is used across multiple views to ensure that the generated plot is returned in a JSON response.

### `load_csv`
This utility function loads CSV data from a given file path and returns it in a format suitable for analysis and visualization.

### `generate_alcohol_cannabis_use_plot`
This function generates a line plot to visualize the alcohol and cannabis use across different age groups.

### `generate_market_share_pies`
This function generates pie charts for the market share of alcohol or cannabis products.

### `generate_sales_line_graph`
This function generates line graphs for alcohol or cannabis sales data.

### `generate_sales_growth_line_graph`
This function generates a line graph comparing the sales growth of alcohol and cannabis.

### `generate_sales_growth_bar_chart`
This function generates a bar chart comparing the sales growth of alcohol and cannabis.

## Error Handling

Each view is decorated with the `@handle_error` decorator to ensure that any errors are caught and handled gracefully.

## CSV Data Files

The following CSV files are used in the views for generating the respective visualizations:

- `yearly_alcohol_product_market_share.csv`: Contains alcohol product market share data.
- `yearly_cannabis_product_market_share.csv`: Contains cannabis product market share data.
- `yearly_alcohol_sales.csv`: Contains yearly sales data for alcohol.
- `yearly_cannabis_sales.csv`: Contains yearly sales data for cannabis.

## Conclusion

This Django-based backend provides interactive data visualizations for alcohol and cannabis consumption and sales trends in Canada. The views leverage dynamic chart generation and display data in various formats (line plots, bar charts, and pie charts), allowing for easy analysis of trends in these sectors.
