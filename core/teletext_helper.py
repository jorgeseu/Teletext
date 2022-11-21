from .models import ProgramItem
import requests
from datetime import date, timedelta

class Fetching_current_data():
    class Meta:
        model = ProgramItem
        fields = {"program_ID", "program_date", "program_data"}

    def fetch_data(self, commit=True):
        #fetching all programs here at once
        for i in range(14):
            n_day = date.today() + timedelta(i)
            #wzór https://www.tvp.pl/prasa/programTVP1/p0101_T1D.txt
            #tu pakujemy wynik
            self.get_prog_data('TVP1', n_day, 'https://www.tvp.pl/prasa/programTVP1/p', '_T1D.txt')
            self.get_prog_data('TVP2', n_day, 'https://www.tvp.pl/prasa/ProgramTVP2/p', '_T2D.txt')
            self.get_prog_data('TVPINF', n_day, 'https://www.tvp.pl/prasa/TVPInfo/p', '_INF.txt')
            self.get_prog_data('TVPKSP', n_day, 'https://www.tvp.pl/prasa/TVPSport/p', '_KSP.txt')
            self.get_prog_data('TVPNK', n_day, 'https://www.tvp.pl/prasa/TVPNauka/p', '_NK.txt')
            self.get_prog_data('TVPKTR', n_day, 'https://www.tvp.pl/prasa/TVPRozrywka/p', '_TRO.txt')


            #TVP2
    def get_prog_data(self, prog_ID, prog_date, link_1, link_2, commit=True,):
        d3 = prog_date.strftime("%m%d")
        print("d3 =", d3)
        response = requests.get(link_1 + d3 + link_2)
        p_data = response.text
        c_item= ProgramItem(program_ID=prog_ID, program_date=prog_date, program_data=p_data)
        try:
            obj = ProgramItem.objects.get(program_ID=prog_ID, program_date=prog_date, program_data=p_data)
        except UserToUserRole.DoesNotExist:
            c_item.save()
        obj = null



