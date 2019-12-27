import datetime

def roundedTimestamp(timestampString):
    date_time_obj = (datetime.datetime.strptime(timestampString, '%Y/%m/%d %H:%M:%S'))
    return int(date_time_obj.timestamp()/900)*900

def convert(dict):
    print(dict['sensors'])
    sensors = dict['sensors']
    readings = {sensor: measurement['centigrade'] for (sensor, measurement) in sensors.items() }
    time = min([roundedTimestamp(measurement['time']) for (sensor, measurement) in sensors.items() ])
    readings['timestamp'] = time
    print(readings)
    print(time)
    datestring = dict['sensors']['temp1']['time']
    date_time_obj = (datetime.datetime.strptime(datestring, '%Y/%m/%d %H:%M:%S'))
    # print('Date:', date_time_obj.date())
    # print('Time:', date_time_obj.time())
    # print('Date-time:', int(date_time_obj.timestamp()))
    # print('rounded', datetime.datetime.strftime(datetime.datetime.fromtimestamp(time), '%Y/%m/%d %H:%M:%S'))
    return readings



dict = {u'sensors': {u'temp1': {u'centigrade': u'16.812', u'time': u'2019/08/18 20:55:17'}}}
print(convert(dict))
