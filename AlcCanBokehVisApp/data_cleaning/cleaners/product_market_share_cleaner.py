## Market Share
import json
import pandas as pd

# Alcohol Product Market Share
alcohol_sales_by_bevy = pd.read_csv(
    '../csv/alcohol_sales_by_beverages.csv',
    skiprows=9,
    on_bad_lines='skip',
    quotechar='"'
)

alcohol_sales_by_bevy = alcohol_sales_by_bevy[alcohol_sales_by_bevy['Unnamed: 0'].str.contains('Total', na=False)]
alcohol_sales_by_bevy.columns = ['Product_type', 'Product Type', '2020', '2021', '2022', '2023', '2024']
alcohol_sales_by_bevy = alcohol_sales_by_bevy.drop(columns=['Product Type'])
alcohol_sales_by_bevy.reset_index(drop=True, inplace=True)


alcohol_sales_by_bevy_long = alcohol_sales_by_bevy.melt(id_vars=["Product_type"], var_name="year", value_name="Sales")
alcohol_sales_by_bevy_long["Sales"] = alcohol_sales_by_bevy_long["Sales"].str.replace(",", "").astype(float)

alcohol_sales_by_bevy_long.set_index("year", inplace=True)
alcohol_sales_filtered = alcohol_sales_by_bevy_long[alcohol_sales_by_bevy_long["Product_type"] != "Total beverages"].copy()
alcohol_sales_filtered["Product_type"] = alcohol_sales_filtered["Product_type"].str.replace(
    "Total spirits", "Spirits"
)
alcohol_sales_filtered["Product_type"] = alcohol_sales_filtered["Product_type"].str.replace(
    "Total wines", "Wines"
)
alcohol_sales_filtered["Product_type"] = alcohol_sales_filtered["Product_type"].str.replace(
    "Total beers", "Beers"
)
alcohol_sales_filtered["Product_type"] = alcohol_sales_filtered["Product_type"].str.replace(
    "Total ciders, coolers, and other refreshment beverages", "Ciders & Coolers"
)

# print(alcohol_sales_filtered)
alcohol_sales_filtered.to_csv('../../data/csv/yearly_alcohol_product_market_share.csv', index=True)



# Cannabis Product Market Share
file_name = '../json/cannabis_sales_by_product.json'

with open(file_name, mode='r') as file:
    cannabis_sales_by_product = json.load(file)

def extract_data_to_df(data, category):
    category_data = cannabis_sales_by_product[category]
    df = pd.DataFrame({
        'Year-Month': category_data['Year-Month'],
        'Sales': category_data['Sales']
    })
    df['Product_type'] = category
    return df

categories = ['dried_cannabis', 'edibles', 'extracts', 'topicals', 'seeds']

dfs = [extract_data_to_df(cannabis_sales_by_product, category) for category in categories]

cannabis_sales_by_product_df = pd.concat(dfs, ignore_index=True)

cannabis_sales_by_product_df['Year-Month'] = pd.to_datetime(cannabis_sales_by_product_df['Year-Month'], errors='coerce')

cannabis_sales_by_product_df['year'] = cannabis_sales_by_product_df['Year-Month'].dt.year

yearly_cannabis_sales_totals = cannabis_sales_by_product_df.groupby(['year', 'Product_type'])['Sales'].sum().reset_index()

yearly_cannabis_sales_totals['Product_type'] = yearly_cannabis_sales_totals['Product_type'].str.replace(
    "dried_cannabis", "Dried Cannabis"
)
yearly_cannabis_sales_totals['Product_type'] = yearly_cannabis_sales_totals['Product_type'].str.replace(
    "edibles", "Edibles"
)
yearly_cannabis_sales_totals['Product_type'] = yearly_cannabis_sales_totals['Product_type'].str.replace(
    "extracts", "Extracts"
)
yearly_cannabis_sales_totals['Product_type'] = yearly_cannabis_sales_totals['Product_type'].str.replace(
    "topicals", "Topicals"
)
yearly_cannabis_sales_totals['Product_type'] = yearly_cannabis_sales_totals['Product_type'].str.replace(
    "seeds", "Seeds"
)
yearly_cannabis_sales_totals.set_index('year', inplace=True)

# print(yearly_cannabis_sales_totals)
yearly_cannabis_sales_totals.to_csv('../../data/csv/yearly_cannabis_product_market_share.csv', index=True)



