import pandas as pd
from datetime import datetime
import dateutil.parser
from googletrans import Translator  # need pip install 4.0.0.rc1

# imports
checkins = pd.read_csv(r'C:\Users\lurie\Documents\ThinkingMachines\dailycheckins.csv')
checkins_new = open(r'C:\Users\lurie\Documents\ThinkingMachines\dailycheckins_updated.csv', 'w')
column_list = list(checkins.columns)
translator = Translator()

# declarations
user_before = 'admin' #Default
timestamp_before = datetime.min
default_hours = 24
default_project = 'admin'

#Header
checkins_new.write(",".join(column_list))
checkins_new.write('\n')

#loop through items
for i in checkins.itertuples(index=True, name='Pandas'):
    user_str = getattr(i, "user")
    timestamp_str = getattr(i, "timestamp")
    hours_str = getattr(i, "hours")
    project_str = getattr(i, "project")

    #set to default
    new_row = []
    new_row_format = ''

    #User
    user = user_str
    if user_str == '':
        user = user_before

    #Date
    #try parse string to date
    try:
        timestamp = dateutil.parser.parse(timestamp_str)
    #translate
    except:
        try:
            translated = translator.translate(timestamp_str).text
            timestamp = dateutil.parser.parse(translated)
        except:
            timestamp = timestamp_before

    #Hours - need to check default hour
    try:
        hours = int(hours_str)
        if hours > default_hours:
            hours = default_hours
    except:
        hours = 0

    #Project
    project = project_str
    if project_str == '':
        project = default_project
    if project_str[0:7] != 'project':
        project = project.replace('-', '')

    # store date before in temp variable, to use if translator cannot translate
    timestamp_before = timestamp
    user_before = user_str

    # update the column value/data
    checkins.loc[getattr(i, "Index"), "user"] = user.capitalize() if isinstance(user, str) else user
    checkins.loc[getattr(i, "Index"), "timestamp"] = timestamp.strftime("%Y-%m-%d")
    checkins.loc[getattr(i, "Index"), "hours"] = hours
    checkins.loc[getattr(i, "Index"), "project"] = project

    #Append rows into comma delimited format
    for col_i in column_list:
        new_row.append(str(checkins.loc[getattr(i, "Index"), col_i]))

    #Format comma delimited
    new_row_format = ",".join(new_row)
    checkins_new.write(new_row_format)
    checkins_new.write('\n')

    print(getattr(i, "Index"))