from .stat_models import Action
from datetime import date
def store_user_action(user, action):
    if(user == "" or user is None):
        user = 'Unlogged'
    c_date = date.today()
    action = Action(user=user, date=c_date, action=action)
    action.save()