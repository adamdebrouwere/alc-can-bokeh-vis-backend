import pandas as pd

def remove_commas_letters(x):
    if isinstance(x, str):
        x = x.replace(',','')
        if x[-1].isalpha():
            x = x[:-1]
    return x

## Yearly Cannabis Sales in Canada
cannabis_sales = pd.read_csv('../csv/cannabis_sales_2019-2024.csv', delimiter=',', skiprows=11, skipfooter=22, engine='python')

canada_cannabis_sales =cannabis_sales[cannabis_sales['Geography'] == 'Canada']

columns_to_clean = canada_cannabis_sales.columns[1:]
for col in columns_to_clean:
    canada_cannabis_sales.loc[:, col] = canada_cannabis_sales[col].apply(remove_commas_letters).astype(float)

monthly_cannabis_sales = canada_cannabis_sales.iloc[:, 1:]

yearly_cannabis_sales = monthly_cannabis_sales.T.groupby(lambda x: x.split()[1]).sum().T

yearly_cannabis_sales = yearly_cannabis_sales.sum(axis=0)

yearly_cannabis_sales_df = pd.DataFrame(yearly_cannabis_sales, columns=['Total Sales'])

yearly_cannabis_sales_df['Total Sales'] = pd.to_numeric(yearly_cannabis_sales_df['Total Sales'], errors='coerce')

yearly_cannabis_sales_df['Growth Percentage'] = yearly_cannabis_sales_df['Total Sales'].pct_change() * 100

yearly_cannabis_sales_df['Growth Percentage'] = yearly_cannabis_sales_df['Growth Percentage'].fillna(0)

yearly_cannabis_sales_df = yearly_cannabis_sales_df.reset_index()

yearly_cannabis_sales_df.rename(columns={'index': 'Year'}, inplace=True)

# print(yearly_cannabis_sales_df)
yearly_cannabis_sales_df.to_csv('../../data/csv/yearly_cannabis_sales.csv', index=True)



## Yearly Alcohol Sales in Canada
alcohol_sales = pd.read_csv('../csv/alcohol_sales_2019-2024.csv', delimiter=',', skiprows=11, skipfooter=22, engine='python')

canada_alcohol_sales = alcohol_sales[alcohol_sales['Geography'] == 'Canada']

columns_to_clean = canada_alcohol_sales.columns[1:]
for col in columns_to_clean:
    canada_alcohol_sales.loc[:, col] = canada_alcohol_sales[col].apply(remove_commas_letters).astype(float)

monthly_alcohol_sales = canada_alcohol_sales.iloc[:, 1:]

yearly_alcohol_sales = monthly_alcohol_sales.T.groupby(lambda x: x.split()[1]).sum().T

yearly_alcohol_sales = yearly_alcohol_sales.sum(axis=0)

yearly_alcohol_sales_df = pd.DataFrame(yearly_alcohol_sales, columns=['Total Sales'])

yearly_alcohol_sales_df['Total Sales'] = pd.to_numeric(yearly_alcohol_sales_df['Total Sales'], errors='coerce')

yearly_alcohol_sales_df['Growth Percentage'] = yearly_alcohol_sales_df['Total Sales'].pct_change() * 100

yearly_alcohol_sales_df['Growth Percentage'] = yearly_alcohol_sales_df['Growth Percentage'].fillna(0)

yearly_alcohol_sales_df = yearly_alcohol_sales_df.reset_index()

yearly_alcohol_sales_df.rename(columns={'index': 'Year'}, inplace=True)

# print(yearly_alcohol_sales_df)
yearly_alcohol_sales_df.to_csv('../../data/csv/yearly_alcohol_sales.csv', index=True)
