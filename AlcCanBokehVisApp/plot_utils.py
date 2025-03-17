from bokeh.models import Legend, LegendItem, HoverTool, ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure
from bokeh.palettes import Category10, Spectral11
import pandas as pd
from bokeh.embed import components
from bokeh.transform import cumsum
from math import pi
from bokeh.layouts import gridplot

def generate_sales_line_graph(name, data):
    x_years=data['Year']
    y_sales=data['Total Sales'] * 1000
    
    colorNumber1 = 0
    colorNumber2 = 0
    
    if name == "Alcohol":
        colorNumber1 = 6
        colorNumber2 = 7
    elif name == "Cannabis":
        colorNumber1 = 3
        colorNumber2 = 2

    p = figure(title=f'{name} Sales from 2019 - 2024', x_axis_label = 'Year', y_axis_label = 'Total Sales (in billions)', sizing_mode="stretch_both")
    p.line(x=x_years, y=y_sales, legend_label="Sales", line_width=5, color=Spectral11[colorNumber1], line_alpha=0.6)
    p.scatter(x=x_years, y=y_sales, size=10, color=Spectral11[colorNumber2], legend_label="Years")

    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.legend.location = "top_left"

    hover = HoverTool()
    hover.tooltips = [('Year', "@x"), ("Total Sales", "@y{$0.00a}")]
    p.add_tools(hover)

    p.yaxis.formatter = NumeralTickFormatter(format="$0a")
    
    script, div = components(p)

    script = script.strip()
    script = script.replace('<script type="text/javascript">', '').replace('</script>', '').strip()

    return {"script": script, "div": div}


def generate_sales_growth_line_graph(data1, data2):
    x_years=data1['Year']
    y_alcohol_growth = data1['Growth Percentage']
    y_cannabis_growth = data2['Growth Percentage']

    p = figure(title='Growth Variance for Alcohol and Cannabis 2019 - 2024', x_axis_label='Year', y_axis_label='Percentage Growth', y_range=[ -20, 125], sizing_mode="stretch_both")

    p.line(x=x_years, y=y_alcohol_growth, legend_label="Alcohol Growth", line_width=4, color=Spectral11[6], line_alpha=0.6)
    p.scatter(x=x_years, y=y_alcohol_growth, size=10, color=Spectral11[7])

    p.line(x=x_years, y=y_cannabis_growth, legend_label="Cannabis Growth", line_width=4, color=Spectral11[3], line_alpha=0.6)
    p.scatter(x=x_years, y=y_cannabis_growth, size=10, color=Spectral11[2])
    
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    hover = HoverTool()
    hover.tooltips = [('Year', "@x"), ("Total Growth", "@y{0.00}%")]
    p.add_tools(hover)

    script, div = components(p)

    script = script.strip()
    script = script.replace('<script type="text/javascript">', '').replace('</script>', '').strip()
    
    return {"script": script, "div": div}
    
    
def generate_sales_growth_bar_chart(data1, data2):
    x_years=data1['Year']
    y_alcohol_growth = data1['Growth Percentage']
    y_cannabis_growth = data2['Growth Percentage']
    
    p = figure(title='Growth Variance for Alcohol and Cannabis 2020 - 2024',
                       x_axis_label='Year', y_axis_label='Percentage Growth',
                        x_range=[2019.5, 2024.5], sizing_mode="stretch_both")

    x_years_numeric = pd.to_numeric(x_years)


    x_offset = 0.2
    x_alcohol_sales_with_offset = x_years_numeric + x_offset
    x_cannabis_sales_with_offset = x_years_numeric - x_offset

    p.vbar(x=x_alcohol_sales_with_offset, top=y_alcohol_growth, width=0.4, legend_label="Alcohol Growth",
                    color=Spectral11[6], bottom=0)


    p.vbar(x=x_cannabis_sales_with_offset, top=y_cannabis_growth, width=0.4, legend_label="Cannabis Growth",
                    color=Spectral11[3], bottom=0)

    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.legend.location = "top_right"
    p.legend.orientation = "vertical"
    p.legend.title = "Growth Type"

    hover = HoverTool()
    hover.tooltips = [("Year", "@x{0}"), ("Growth", "@top{0.00}%")]
    p.add_tools(hover)
    
    script, div = components(p)

    script = script.strip()
    script = script.replace('<script type="text/javascript">', '').replace('</script>', '').strip()
    
    return {"script": script, "div": div}


def market_share_pie_chart(name, data, year):
    data = data.reset_index()

    yearly_data = data[data['year'] == year].copy()
    yearly_data.columns = ['index', 'year', "Product_type", "Sales", "Colour"]
    yearly_data.loc[:, "Angle"] = yearly_data["Sales"] / yearly_data["Sales"].sum() * 2 * pi
    yearly_data.loc[:, 'Percentage'] = yearly_data['Sales'] / yearly_data['Sales'].sum() * 100

    p = figure(title=f"{year}", tools="hover", tooltips="@Product_type: @Percentage{0.0}% Market Share", x_range=(-0.5, 0.5), y_range=(0.5, 1.5), sizing_mode="stretch_both")
    p.wedge(x=0, y=1, radius=0.3,
            start_angle=cumsum("Angle", include_zero=True), end_angle=cumsum("Angle"),
            line_color="white", fill_color="Colour", source=yearly_data)
    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    return p


def generate_market_share_pies(name, data):
    buds_palette = {
        "Dried Cannabis": "#006400",
        "Edibles": "#8A2BE2",
        "Extracts": "#228B22",
        "Seeds": "#800080",
        "Topicals": "#32CD32"
    }
    bevy_palette = {
        "Beers": "#FFD700",
        "Wines": "#8B0000",
        "Spirits": "#A0522D",
        "Ciders & Coolers": "#9ACD32"
    }

    if name == 'Cannabis':
        product_types = data['Product_type'].unique()
        if len(buds_palette) < len(product_types):
            raise ValueError("Not enough colors in the buds_palette for all product types.")
        data["Colour"] = data["Product_type"].map(buds_palette)
    elif name == 'Alcohol':
        data["Colour"] = data["Product_type"].map(bevy_palette)
    else:
        raise ValueError("Type not included in colour palettes.")
        
    years = data.year.unique()
    
    pie_charts = []
    for year in years:
        p = market_share_pie_chart(name, data, year)
        pie_charts.append(p)
        

    legend_fig = figure(title="Legend", sizing_mode='stretch_both')
    legend_fig.xgrid.visible = False
    legend_fig.ygrid.visible = False
    legend_fig.xaxis.visible = False
    legend_fig.yaxis.visible = False

    product_types = data['Product_type'].unique()
    product_color_mapping = {product: color for product, color in zip(product_types, data['Colour'].unique())}
    legend_items = [
        LegendItem(
            label=product,
            renderers=[
                legend_fig.scatter(
                    marker='square', 
                    x=[0], 
                    y=[0], 
                    size=10, 
                    color=product_color_mapping[product], 
                    visible=False
                )
            ]
        )
        for product in product_types
    ]

    legend = Legend(items=legend_items, title="Product types", location='top_left', orientation='vertical',)
    legend_fig.title.align = 'center'
    legend_fig.add_layout(legend, 'center')

    num_cols = 3
    pie_grid_figs = [pie_charts[i:i+num_cols] for i in range(0, len(pie_charts), num_cols)]

    if len(pie_grid_figs[-1]) < num_cols:
        pie_grid_figs[-1].append(legend_fig)
    else:
        pie_grid_figs.append([legend_fig])

    grid = gridplot(children=pie_grid_figs, sizing_mode="stretch_both")

    script, div = components(grid)

    script = script.strip()
    script = script.replace('<script type="text/javascript">', '').replace('</script>', '').strip()

    return {"script": script, "div": div}


def generate_alcohol_cannabis_use_plot(data, title):
    years = list(data.keys())
    age_ranges = list(next(iter(data.values())).keys())

    df = pd.DataFrame(columns=[f"{age_range}_lifetime" for age_range in age_ranges] + [f"{age_range}_12mo" for age_range in age_ranges], index=years)

    for year in years:
        for age_range in age_ranges:
            past_lifetime = data[year].get(age_range, [None, None])[0]
            past_12mo = data[year].get(age_range, [None, None])[1]

            if past_lifetime:
                percentage_lifetime = float(past_lifetime.split(" [")[0])
                df.loc[year, f"{age_range}_lifetime"] = percentage_lifetime

            if past_12mo:
                percentage_12mo = float(past_12mo.split(" [")[0])
                df.loc[year, f"{age_range}_12mo"] = percentage_12mo

    source = ColumnDataSource(df)

    p = figure(title=title, x_axis_label="Year", y_axis_label="Percentage", x_range=years, sizing_mode="stretch_both")

    colors = Category10[len(age_ranges)]

    legend_items = []
    for i, age_range in enumerate(age_ranges):
        line_lifetime = p.line(x='index', y=f"{age_range}_lifetime", source=source, line_width=4, color=colors[i], line_alpha=0.6)
        line_12mo = p.line(x='index', y=f"{age_range}_12mo", source=source, line_width=4, color=colors[i], line_dash="dashed", line_alpha=0.6)
        
        point_lifetime = p.scatter(x='index', y=f"{age_range}_lifetime", source=source, size=8, color=colors[i], marker="square")
        point_12mo = p.scatter(x='index', y=f"{age_range}_12mo", source=source, size=8, color=colors[i])

        legend_items.append(LegendItem(label=f"{age_range} (lifetime)", renderers=[line_lifetime, point_lifetime]))
        legend_items.append(LegendItem(label=f"{age_range} (12mo)", renderers=[line_12mo, point_12mo]))

    hover = HoverTool()
    hover.tooltips = [("Year", "@index"), ("Percentage", "$y%")]
    p.add_tools(hover)

    custom_legend = Legend(items=legend_items, location='top_left', orientation='vertical')
    custom_legend.title = "Age Range and Time Period"
    custom_legend.click_policy = "hide"
    custom_legend.label_text_font_size = "8pt"
    custom_legend.title_text_font_size = "10pt"
    custom_legend.spacing = 5
    custom_legend.label_standoff = 5
    custom_legend.padding = 5
    custom_legend.margin = 5

    p.add_layout(custom_legend, 'right')

    script, div = components(p)

    script = script.strip()
    script = script.replace('<script type="text/javascript">', '').replace('</script>', '').strip()

    return {"script": script, "div": div}