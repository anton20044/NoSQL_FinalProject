#! /bin/python3
from datetime import datetime
import datetime
import random
import time
from sys import argv
from clickhouse_driver import Client

def count_500k():
  result = []
  dt = datetime.datetime(2024, 8, 1)
  end = datetime.datetime(2024, 8, 31, 23, 59, 59)
  step = datetime.timedelta(seconds=5)

  while dt < end:
    result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
    dt += step
  return result

def count_170k():
  result = []
  dt = datetime.datetime(2024, 8, 1)
  end = datetime.datetime(2024, 8, 10, 23, 59, 59)
  step = datetime.timedelta(seconds=5)

  while dt < end:
    result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
    dt += step
  return result


def count_86k():
  result = []
  dt = datetime.datetime(2024, 8, 1)
  end = datetime.datetime(2024, 8, 5, 23, 59, 59)
  step = datetime.timedelta(seconds=5)

  while dt < end:
    result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
    dt += step
  return result


def count_17k():
  result = []
  dt = datetime.datetime(2024, 8, 1)
  end = datetime.datetime(2024, 8, 1, 23, 59, 59)
  step = datetime.timedelta(seconds=5)

  while dt < end:
    result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
    dt += step
  return result



arr_text=['Ошибка 1','Предупреждение 2','Внимание 1','Предупреждение 1','Ошибка 2','Ок','Возможна ошибка','Внимание 2','Ошибка 3','Внимание 3']
arr_event=['Событие 1','Событие 2','Событие 3','Событие 4','Событие 5','Событие 6','Событие 7','Событие 8','Событие 9','Событие 10']


if (argv[1] == '17'):
  arr = count_17k()
  client =  Client(host='192.168.50.113', port=9000, user='default', password='anton')
  start_time = time.time()

  for times in arr:
    client.execute("insert into log_table (*) values ('" + times + "','" + arr_event[random.randrange(0, 10)] + "','" + arr_text[random.randrange(0, 10)] + "')")

  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


if (argv[1] == '86'):
  arr = count_86k()
  client =  Client(host='192.168.50.113', port=9000, user='default', password='anton')
  start_time = time.time()
  for times in arr:
    client.execute("insert into log_table (*) values ('" + times + "','" + arr_event[random.randrange(0, 10)] + "','" + arr_text[random.randrange(0, 10)] + "')")
  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


if (argv[1] == '170'):
  arr = count_170k()
  client =  Client(host='192.168.50.113', port=9000, user='default', password='anton')
  start_time = time.time()
  for times in arr:
    client.execute("insert into log_table (*) values ('" + times + "','" + arr_event[random.randrange(0, 10)] + "','" + arr_text[random.randrange(0, 10)] + "')")
  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


if (argv[1] == '500'):
  arr = count_500k()
  client =  Client(host='192.168.50.113', port=9000, user='default', password='anton')
  start_time = time.time()
  for times in arr:
    client.execute("insert into log_table (*) values ('" + times + "','" + arr_event[random.randrange(0, 10)] + "','" + arr_text[random.randrange(0, 10)] + "')")
  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


if (argv[1] == '-500'):
  client =  Client(host='192.168.50.113', port=9000, user='default', password='anton')
  start_time = time.time()
  client.execute("select date, event from log_table where date >= '2024-08-01' " \
	" and date < '2024-08-08'")
  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


if (argv[1] == '-100'):
  client =  Client(host='192.168.50.113', port=9000, user='default', password='anton')
  start_time = time.time()
  client.execute("select date, event from log_table where date >= '2024-08-01' " \
        " and date < '2024-08-08' limit 1000")
  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


if (argv[1] == '-5001'):
  client =  Client(host='192.168.50.113', port=9000, user='default', password='anton')
  start_time = time.time()
  client.execute("select date, event from log_table where date >= '2024-08-01' " \
        " and date < '2024-08-08' and event = 'Событие 6'")
  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


if (argv[1] == '-1001'):
  client =  Client(host='192.168.50.113', port=9000, user='default', password='anton')
  start_time = time.time()
  client.execute("select date, event from log_table where date >= '2024-08-01' " \
        " and date < '2024-08-08' and event = 'Событие 6' limit 1000 ")
  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


