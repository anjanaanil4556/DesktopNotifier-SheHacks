import COVID19Py

covid19=COVID19Py.COVID19(data_source="jhu")
latest = covid19.getLatest()

from plyer import notification
notification.notify(
    title="Covid 19 UPDATES",
    message=str(latest),
    app_icon="C:/Users/Anjana Anil/OneDrive/Desktop/Project/covid.ico",
    timeout=30
 )

