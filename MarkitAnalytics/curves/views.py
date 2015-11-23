from django.shortcuts import render
import datetime
import pdb
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from curves.forms import CurveConstructionForm
import numpy as np


def home(request):
    plot = figure(x_axis_type="datetime", tools="pan,box_zoom,reset,save")
    x = np.array(['2007-01-01', '2008-02-01', '2009-03-01'], dtype='datetime64')
    y = np.array([0.032, 0.0562, 0.0461])
    plot.line(x, y)

    # show the results
    script, div = components(plot)

    form = []
    if request.method == 'POST':
        form = CurveConstructionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

    else:
        form = CurveConstructionForm({
            'constructors_path': '',
            'processors_path': '',
            'market_data_path': '',
        })

    context = {
        'form': form,
        'plot_script': script,
        'plot_div': div,
    }

    return render(request, 'index.html', context)
