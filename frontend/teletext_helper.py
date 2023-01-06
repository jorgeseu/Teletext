from .models import ProgramItem
import requests
from datetime import date, timedelta

class Fetching_current_data():
    class Meta:
        model = ProgramItem
        fields = {"program_ID", "program_date", "program_data"}

    #def fetch_data(self, commit=True):
        #fetching all programs here at once
        #for i in range(14):
            #TVP1
            #c_item = ProgramItem(program_ID='TVP1', program_date= date.today())
            #n_day = date.today() + timedelta(i)
            #d3 = n_day.strftime("%m%d")
            #print("d3 =", d3)
            #response = requests.get(target_url)
            #data = response.text

