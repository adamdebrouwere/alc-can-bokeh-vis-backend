from django.http import JsonResponse
from .utils import load_csv, generate_response, handle_error
from .plot_utils import (
    generate_alcohol_cannabis_use_plot,
    generate_market_share_pies,
    generate_sales_line_graph,
    generate_sales_growth_line_graph,
    generate_sales_growth_bar_chart,
)

@handle_error
async def alcohol_use_view(request):
    data = {
        "2013": {
            "15-19": ["68.7 [66.0-71.3]", "60.3 [57.6-63.1]"],
            "20-24": ["90.4 [88.2-92.5]", "83.2 [80.4-85.9]"],
            "25+": ["92.1 [91.0-93.3]", "76.5 [74.9-78.1]"]
        },
        "2015": {
            "15-19": ["66.4 [63.2-69.6]", "59.1 [55.5-62.6]"],
            "20-24": ["88.5 [85.9-91.1]", "82.7 [79.7-85.6]"],
            "25+": ["93.2 [92.3-94.1]", "77.8 [76.3-79.4]"]
        },
        "2017": {
            "15-19": ["64.2 [61.7-66.7]", "56.8 [54.1-59.5]"],
            "20-24": ["88.3 [84.9-91.6]", "83.5 [80.1-86.8]"],
            "25+": ["92.5 [91.2-93.8]", "79.4 [77.4-81.3]"]
        },
        "2019": {
            "15-19": ["48.5 [40.3-56.8]", "46.3 [38.0-54.5]"],
            "20-24": ["89.7 [84.9-94.6]", "84.4 [78.7-90.1]"],
            "25+": ["89.8 [88.8-90.8]", "78.2 [76.9-79.5]"]
        },
        "2023": {
            "15-19": ["62.7 [60.0-65.2]", "42.6 [40.2-45.0]"],
            "20-24": ["81.0 [78.8-82.9]", "63.4 [61.4-65.4]"],
            "25+": ["80.4 [79.6-81.3]", "67.8 [67.168.5]"]
        }
    }
    
    response = await generate_response(generate_alcohol_cannabis_use_plot,
        data=data,
        title="Alcohol Use by Age Range Over the Years",
    )
    return JsonResponse(response)

@handle_error
async def cannabis_use_view(request):
    data = {
        "2013": {
            "15-19": ["31.1 [28.0-34.2]", "31.1 [28.0-34.2]"],
            "20-24": ["50.9 [47.4-54.4]", "26.2 [23.0-29.5]"],
            "25+": ["41.1 [39.2-43.0]", "8.0 [7.0-9.1]"]
        },
        "2015": {
            "15-19": ["28.9 [25.7-32.1]", "29.7 [26.4-33.0]"],
            "20-24": ["53.7 [50.0-57.3]", "29.7 [26.4-33.0]"],
            "25+": ["44.9 [43.2-46.7]", "9.9 [8.9-11.0]"]
        },
        "2017": {
            "15-19": ["26.9 [24.5-29.3]", "33.2 [30.3-36.2]"],
            "20-24": ["52.6 [49.4-55.9]", "33.2 [30.3-36.2]"],
            "25+": ["47.6 [44.9-50.2]", "12.7 [10.9-14.6]"]
        },
        "2019": {
            "15-19": ["22.8 [16.0-29.6]", "21.9 [15.2-28.7]"],
            "20-24": ["54.8 [47.0-62.6]", "44.6 [36.8-52.3]"],
            "25+": ["42.1 [40.8-43.5]", "18.5 [17.3-19.8]"]
        },
        "2023": {
            "15-19": ["42.3 [40.4-44.3]", "43.3 [41.4-45.3]"],
            "20-24": ["60.6 [58.6-62.5]", "52.4 [50.4-54.5]"],
            "25+": ["59.9 [59.1-60.6]", "38.5 [37.5-39.5]"]
        }
    }
    
    response = await generate_response(
        generate_alcohol_cannabis_use_plot,
        data=data,
        title="Cannabis Use by Age Range Over the Years",
    )
    
    return JsonResponse(response)

@handle_error
async def alcohol_product_market_share_view(request):
    data = load_csv('./AlcCanBokehVisApp/data/csv/yearly_alcohol_product_market_share.csv')
    
    response = await generate_response(
        generate_market_share_pies,
        "Alcohol",
        data)
    
    return JsonResponse(response)

@handle_error
async def cannabis_product_market_share_view(request):
    data = load_csv('./AlcCanBokehVisApp/data/csv/yearly_cannabis_product_market_share.csv')

    response = await generate_response(
        generate_market_share_pies,
        "Cannabis", 
        data)
    
    return JsonResponse(response)

@handle_error    
async def alcohol_yearly_sales_view(request):
    data = load_csv('./AlcCanBokehVisApp/data/csv/yearly_alcohol_sales.csv')
    
    response = await generate_response(
        generate_sales_line_graph, 
        "Alcohol", 
        data)
    
    return JsonResponse(response)

@handle_error
async def cannabis_yearly_sales_view(request):
    data = load_csv('./AlcCanBokehVisApp/data/csv/yearly_cannabis_sales.csv')
    
    response = await generate_response(
        generate_sales_line_graph, 
        "Cannabis", 
        data)
    
    return JsonResponse(response)

@handle_error
async def combined_sales_growth_line_plot_view(request):
    alcohol_data = load_csv('./AlcCanBokehVisApp/data/csv/yearly_alcohol_sales.csv')
    cannabis_data = load_csv('./AlcCanBokehVisApp/data/csv/yearly_cannabis_sales.csv')
    
    response = await generate_response(
        generate_sales_growth_line_graph, 
        alcohol_data, 
        cannabis_data)
    
    return JsonResponse(response)

@handle_error
async def combined_sales_growth_bar_chart_view(request):
    alcohol_data = load_csv('./AlcCanBokehVisApp/data/csv/yearly_alcohol_sales.csv')
    cannabis_data = load_csv('./AlcCanBokehVisApp/data/csv/yearly_cannabis_sales.csv')
    
    response = await generate_response(
        generate_sales_growth_bar_chart, 
        alcohol_data, 
        cannabis_data)
    
    return JsonResponse(response)