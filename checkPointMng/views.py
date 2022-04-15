from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Search
from .forms import SearchForm
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO


# hello world test
def index(request):
    submitted = False
    terminal = ''
    start = ''
    startYear = ''
    startMonth = ''
    startDay = ''
    end = ''
    endYear = ''
    endMonth = ''
    endDay = ''
    data = None

    # if (3. form submitted from .html (POST))
    if request.method == 'POST':
        # set form from POST request
        form = SearchForm(request.POST, request.FILES)

        # if valid, save form and return with GET parameter
        if form.is_valid():
            terminal = request.POST.get('terminal')
            start = request.POST.get('start')
            end = request.POST.get('end')

            return HttpResponseRedirect('/?submitted=True&terminal=' + terminal + '&start=' + start + '&end=' + end)

    # else (GET) (1. display an empty form to be filled out for the first time),
    else:
        form = SearchForm()

        # if (4. submitted is passed as GET parameter, set submitted to true)
        if 'submitted' in request.GET:
            submitted = True
            terminal = request.GET.get('terminal')
            start = request.GET.get('start')
            end = request.GET.get('end')
            startDate = datetime.datetime.strptime(start, '%Y-%m-%d')
            endDate = datetime.datetime.strptime(end, '%Y-%m-%d')

            # to utilize ISO calendar - startDate.year/month/day

            startYear = startDate.strftime('%Y')
            startMonth = startDate.strftime('%m')
            startDay = startDate.strftime('%d')
            endYear = endDate.strftime('%Y')
            endMonth = endDate.strftime('%m')
            endDay = endDate.strftime('%d')

            # read csv and store as DataFrame
            df = pd.read_csv('checkPoint2/static/lax_predictions.csv', parse_dates=True)
            df = df.set_index('Datetime')

            # get slice of DataFrame according to search parameters
            df2 = df.loc[startMonth.lstrip('0') + '/' + startDay.lstrip('0') + '/' + startYear + ' 3:00':endMonth.lstrip('0') + '/' + endDay.lstrip('0') + '/' + endYear + ' 3:00']
            df2 = df2[:-1]

            # plot
            fig = plt.figure()
            plt.rcParams.update({'figure.figsize': (15, 10), 'figure.dpi': 120})
            plt.xticks(rotation=90)
            plt.plot(df2['Throughput'], color='red')
            plt.plot(df2['Prediction'], color='blue')

            # return as graphic
            imgdata = StringIO()
            fig.savefig(imgdata, format='svg')
            imgdata.seek(0)

            data = imgdata.getvalue()

    # (2., 5. render .html page)
    return render(request,
                  'checkPointMng/home.html',
                  {
                      'form': form,
                      'submitted': submitted,
                      'terminal': terminal,
                      'start': start,
                      'startYear': startYear,
                      'startMonth': startMonth,
                      'startDay': startDay,
                      'end': end,
                      'endYear': endYear,
                      'endMonth': endMonth,
                      'endDay': endDay,
                      'data': data,
                  })

    # return render(request, 'checkPointMng/home.html')
