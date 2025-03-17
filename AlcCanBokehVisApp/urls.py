from django.urls import path
from .views import alcohol_use_view, cannabis_use_view, alcohol_product_market_share_view, cannabis_product_market_share_view, alcohol_yearly_sales_view, cannabis_yearly_sales_view, combined_sales_growth_line_plot_view, combined_sales_growth_bar_chart_view

urlpatterns = [
    path("alcohol-use-view/", alcohol_use_view, name='alcohol_use_view'),
    path("cannabis-use-view/", cannabis_use_view, name='cannabis_use_view'),
    path("alcohol-product-market-share-view/", alcohol_product_market_share_view, name='alcohol_product_market_share_view'),
    path("cannabis-product-market-share-view/", cannabis_product_market_share_view, name='cannabis_product_market_share_view'),
    path("alcohol-yearly-sales-view/", alcohol_yearly_sales_view, name = 'alcohol_yearly_sales_view'),
    path("cannabis-yearly-sales-view/", cannabis_yearly_sales_view, name = 'cannabis_yearly_sales_view'),
    path("combined-sales-growth-line-plot-view/", combined_sales_growth_line_plot_view, name = 'combined_sales_growth_line_plot_view'),
    path("combined-sales-growth-bar-chart-view/", combined_sales_growth_bar_chart_view, name = 'combined_sales_growth_bar_chart_view'),
]
