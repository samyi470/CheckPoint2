from django.core.management.base import BaseCommand, CommandError
from checkPointMng.models import Terminal, TerminalThroughput, Airport

import pandas as pd


class Command(BaseCommand):
    help = 'populate database from csv files'

    def handle(self, *args, **options):
        lAXAirport = Airport(name='Los Angeles International Airport', code='LAX')
        lAXAirport.save()
        LAX_TERMINALS = (
            ("Suites", "Suites"),
            ("TBIT Main Checkpoint", "TBIT Main Checkpoint"),
            ("Terminal 1 - Passenger", "Terminal 1 - Passenger"),
            ("Terminal 2 - Passenger", "Terminal 2 - Passenger"),
            ("Terminal 3 - Passenger", "Terminal 3 - Passenger"),
            ("Terminal 4 - FIS", "Terminal 4 - FIS"),
            ("Terminal 4 - Passenger", "Terminal 4 - Passenger"),
            ("Terminal 4A - Passenger", "Terminal 4A - Passenger"),
            ("Terminal 5 - Passenger", "Terminal 5 - Passenger"),
            ("Terminal 5A - Passenger", "Terminal 5A - Passenger"),
            ("Terminal 6 - Passenger", "Terminal 6 - Passenger"),
            ("Terminal 7 - Passenger", "Terminal 7 - Passenger"),
        )
        for term in LAX_TERMINALS:
            newTerminal = Terminal(name=term[0], airport=lAXAirport)
            newTerminal.save()

            df = pd.read_csv('~/Documents/Github/CheckPoint2/checkPoint2/static/Merged_Data/LAX_' + term[0] + '.csv')
            for year in ['2015', '2016', '2017', '2018', '2019']:
                try:
                    df['Time_' + year] = pd.to_datetime(df['Date_' + year], format='%m/%d/%y').dt.strftime(
                        '%m/%d/%y').astype('str') + ' ' + df['Hour'].astype('str')
                    df['Time_' + year] = pd.to_datetime(df['Time_' + year], errors='coerce')
                    print(df)
                except Exception as e:
                    pass

            for index, row in df.iterrows():
                for year in ['2015', '2016', '2017', '2018', '2019']:
                    try:
                        newThroughput = TerminalThroughput(date=row['Time_' + year],
                                                           throughput=row[
                                                               'Throughput_' + year],
                                                           terminal=newTerminal,
                                                           airport=lAXAirport)
                        newThroughput.save()
                        print('currently at', index)
                    except:
                        pass
