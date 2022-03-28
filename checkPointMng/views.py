from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Search, TerminalThroughput
from .forms import SearchForm
import datetime


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
    labels=[]
    data=[]

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

            throughput_list = TerminalThroughput.objects.filter(date__gte = startDate, date__lte = endDate, terminal__name = terminal).order_by("date")
            labels = []
            data = []
            for throughput in throughput_list:
                labels.append(throughput.date.strftime("%m/%d/%Y %H:%M:%S"))
                data.append(throughput.throughput)

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
                      'labels': labels,
                      'data': data,
                  })

    # return render(request, 'checkPointMng/home.html')
