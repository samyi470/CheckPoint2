from django.core.management.base import BaseCommand, CommandError
from checkPointMng.models import Terminal, TerminalThroughput, TerminalPrediction, Airport

import pandas as pd


class Command(BaseCommand):
    help = 'populate database from csv files'

    def handle(self, *args, **options):
        lAXAirport = Airport(name='Los Angeles International Airport', code='LAX')
        lAXAirport.save()
        LAX_TERMINALS = (
            ("Terminal 1 - Passenger", "terminal1"),
        )
        for term in LAX_TERMINALS:
            newTerminal = Terminal(name=term[0], airport=lAXAirport)
            newTerminal.save()

            df = pd.read_csv('~/Documents/Github/CheckPoint2/checkPoint2/static/Data/lax_' + term[1] + '_predictions.csv', parse_dates=["Datetime"])
            for index, row in df.iterrows():
                newThroughput = TerminalThroughput(date=row['Datetime'],
                                                   throughput=row['Throughput'],
                                                   terminal=newTerminal,
                                                   airport=lAXAirport)
                newPrediction = TerminalPrediction(date=row['Datetime'],
                                                   prediction=row['Prediction'],
                                                   terminal=newTerminal,
                                                   airport=lAXAirport)
                newPrediction.save()
                newThroughput.save()
                print('currently at', index)

        print('Database populated!')