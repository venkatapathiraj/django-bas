from django.shortcuts import render,get_object_or_404,redirect,render_to_response,HttpResponse,redirect
from basket.models import Item,Cart,OrderedItem
from django.views.generic import ListView
from django.conf import settings
from django.contrib import messages
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL
from bokeh.embed import components
from django.db import connection
import pandas as pd

# Create your views here.

class Veg(ListView):
    
    model = Item

    template_name = 'veg1.html'

    

class Rice(ListView):
    model = Item

    template_name = 'rice.html'



class Bands(ListView):
    model = Item

    template_name = 'biscuitsandsnacks.html'

class Bever(ListView):
    model = Item

    template_name = 'beverges.html'            

    #items = VegItem.objects.all()
    #return render(request, "pro.html", {'items':items})

# def purchases(request):
    # 
    # cur=connection.cursor()
    # cur.execute('select * from bigbasket.basket_item')
    # td = cur.fetchall()
# 
    # x=[]
# 
    # y=[]
# 
    # for i in td:
        # x.append(i[0][1])
        # y.append(i[0][4])
# 
    # title = 'Vegitables Purchases'
    # plot = figure(title=title,
    # x_axis_label='Item_Name',
    # y_axis_label='Date',
    # plot_width = 500,
    # plot_height=400)
    # plot.line(x,y,line_width=4)
    # script, div = components(plot)
    # return render_to_response('grap.html',{'script':script,'div':div})
       
def purchases(request):

    df = pd.DataFrame(AAPL)
    df['date'] = pd.to_datetime(df['date'])
    
    output_file("purchase.html")
    
    p = figure(plot_width=800, plot_height=400, x_axis_type="datetime")
    
    p.circle(df['date'], df['close'], color='navy', alpha=0.5)
    
    show(p)
    
    return redirect("basket:veg")
