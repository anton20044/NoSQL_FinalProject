#! /bin/python3
from datetime import datetime
import datetime
import random
import time
from sys import argv
from pymongo import MongoClient


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
  client = MongoClient('mongodb://192.168.50.118:27017,192.168.50.119:27017,192.168.50.120:27017/?replicaSet=cluster')

  start_time = time.time()
  db = client['my_base']
  collection = db.log_table

  for times in arr:
    post = {'date': "'" + times + "'", 'event': "'" + arr_event[random.randrange(0, 10)] + "'", 'text': "'" + arr_text[random.randrange(0, 10)] + "'" }
    collection.insert_one(post)

  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)



if (argv[1] == '86'):

  arr = count_86k()
  client = MongoClient('mongodb://192.168.50.118:27017,192.168.50.119:27017,192.168.50.120:27017/?replicaSet=cluster')

  start_time = time.time()
  db = client['my_base']
  collection = db.log_table

  for times in arr:
    post = {'date': "'" + times + "'", 'event': "'" + arr_event[random.randrange(0, 10)] + "'", 'text': "'" + arr_text[random.randrange(0, 10)] + "'" }
    collection.insert_one(post)

  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


if (argv[1] == '170'):

  arr = count_170k()
  client = MongoClient('mongodb://192.168.50.118:27017,192.168.50.119:27017,192.168.50.120:27017/?replicaSet=cluster')

  start_time = time.time()
  db = client['my_base']
  collection = db.log_table

  for times in arr:
    post = {'date': "'" + times + "'", 'event': "'" + arr_event[random.randrange(0, 10)] + "'", 'text': "'" + arr_text[random.randrange(0, 10)] + "'" }
    collection.insert_one(post)

  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)


if (argv[1] == '500'):

  arr = count_500k()
  client = MongoClient('mongodb://192.168.50.118:27017,192.168.50.119:27017,192.168.50.120:27017/?replicaSet=cluster')

  start_time = time.time()
  db = client['my_base']
  collection = db.log_table

  for times in arr:
    post = {'date': "'" + times + "'", 'event': "'" + arr_event[random.randrange(0, 10)] + "'", 'text': "'" + arr_text[random.randrange(0, 10)] + "'" }
    collection.insert_one(post)

  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)



if (argv[1] == '-500'):

  client = MongoClient('mongodb://192.168.50.118:27017,192.168.50.119:27017,192.168.50.120:27017/?replicaSet=cluster')

  start_time = time.time()
  db = client['my_base']
  collection = db.log_table

  post = {'date': {'$gt' : "'2024-08-01 00:00:00'", '$lt' : "'2024-08-30 00:00:00'"}}
  collection.find(post).limit(500000)

  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)



if (argv[1] == '-100'):

  client = MongoClient('mongodb://192.168.50.118:27017,192.168.50.119:27017,192.168.50.120:27017/?replicaSet=cluster')

  start_time = time.time()
  db = client['my_base']
  collection = db.log_table

  post = {'date': {'$gt' : "'2024-08-01 00:00:00'", '$lt' : "'2024-08-30 00:00:00'"}}
  collection.find(post).limit(1000)

  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)



if (argv[1] == '-5001'):

  client = MongoClient('mongodb://192.168.50.118:27017,192.168.50.119:27017,192.168.50.120:27017/?replicaSet=cluster')

  start_time = time.time()
  db = client['my_base']
  collection = db.log_table

  post = {'date': {'$gt' : "'2024-08-01 00:00:00'", '$lt' : "'2024-08-30 00:00:00'"}, 'event' : 'Событие 6'}
  collection.find(post).limit(500000)

  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)



if (argv[1] == '-1001'):

  client = MongoClient('mongodb://192.168.50.118:27017,192.168.50.119:27017,192.168.50.120:27017/?replicaSet=cluster')

  start_time = time.time()
  db = client['my_base']
  collection = db.log_table

  post = {'date': {'$gt' : "'2024-08-01 00:00:00'", '$lt' : "'2024-08-30 00:00:00'"}, 'event' : 'Событие 6'}
  collection.find(post).limit(500000)

  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Elapsed time: ', elapsed_time)
