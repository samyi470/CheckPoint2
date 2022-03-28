from django.contrib import admin
from .models import MainMenu
from .models import Airport, Terminal, AirportThroughput, TerminalThroughput, Throughput

admin.site.register(MainMenu)
admin.site.register(Airport)
admin.site.register(Terminal)
admin.site.register(AirportThroughput)
admin.site.register(TerminalThroughput)
admin.site.register(Throughput)
