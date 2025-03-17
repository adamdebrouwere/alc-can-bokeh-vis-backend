# Alcohol and Cannabis Data Analysis - Django Views

This project contains a set of Django views and data cleaners that generate various visualizations related to alcohol and cannabis consumption and market trends in Canada. To clean the data I use pandas, then create new csv files served to the views which, process data, generate responses, and return JSON responses with dynamic data visualizations. See the project fully deployed [here](https://alc-can-market-analysis.netlify.app/).

## Features

- **Alcohol Use by Age Range**: Visualizes alcohol consumption across different age groups from 2013 to 2023.
- **Cannabis Use by Age Range**: Displays cannabis consumption across age groups from 2013 to 2023.
- **Alcohol Product Market Share**: Shows the market share of alcohol products.
- **Cannabis Product Market Share**: Displays the market share of cannabis products.
- **Alcohol Yearly Sales**: Visualizes yearly sales data for alcohol.
- **Cannabis Yearly Sales**: Visualizes yearly sales data for cannabis.
- **Combined Sales Growth (Line Chart)**: Compares the sales growth of alcohol and cannabis.
- **Combined Sales Growth (Bar Chart)**: Shows the combined sales growth for alcohol and cannabis in a bar chart format.

## CSV Data Files

The following CSV files are used in the views for generating the respective visualizations:

- `yearly_alcohol_product_market_share.csv`: Contains alcohol product market share data.
- `yearly_cannabis_product_market_share.csv`: Contains cannabis product market share data.
- `yearly_alcohol_sales.csv`: Contains yearly sales data for alcohol.
- `yearly_cannabis_sales.csv`: Contains yearly sales data for cannabis.

- ## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/adamdebrouwere/alc-can-bokeh-vis-backend.git
    cd https://github.com/adamdebrouwere/alc-can-bokeh-vis-backend.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Conclusion

This Django-based backend provides interactive data visualizations for alcohol and cannabis consumption and sales trends in Canada. The views leverage dynamic chart generation and display data in various formats (line plots, bar charts, and pie charts), allowing for easy analysis of trends in these sectors.
