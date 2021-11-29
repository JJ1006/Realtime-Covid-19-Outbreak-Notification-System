import requests
from plyer import notification
import time
import pandas as pd

jsonData = requests.get('https://www.mohfw.gov.in/data/datanew.json').json()
df = pd.DataFrame(jsonData)
def notifyMe(message):
    notification.notify(
        # title = title,
        message = message,
        app_icon="D:\Visual Studio Code\python projects\Realtime-Covid-19-Outbreak-Notification-System\icon.ico",
        timeout=3.5
    )

# print(df)
# print(df.loc[df['state_name'] == 'Gujarat'])
states = ['Gujarat','Andhra Pradesh']
for i in states:
    state_name = df.loc[df['state_name'] == i].state_name.values[0]
    active = df.loc[df['state_name'] == i].active.values[0]
    positive = df.loc[df['state_name'] == i].positive.values[0]
    cured = df.loc[df['state_name'] == i].cured.values[0]
    death = df.loc[df['state_name'] == i].death.values[0]
    new_active = df.loc[df['state_name'] == i].new_active.values[0]
    new_positive = df.loc[df['state_name'] == i].new_positive.values[0]
    new_cured = df.loc[df['state_name'] == i].new_cured.values[0]
    new_death = df.loc[df['state_name'] == i].new_death.values[0]

    # nTitle = 'Cases of Covid-19'
    nText = f"State: {state_name}\nActive: {active}\nNew Cured: {new_cured}\nNew Death: {new_death}"
    # print(nText)
    notifyMe(nText)
    time.sleep(7)
