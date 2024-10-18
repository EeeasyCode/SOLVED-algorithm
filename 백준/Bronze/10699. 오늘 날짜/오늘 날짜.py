import datetime 

print((datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime("%Y-%m-%d"))
