import csv
import json
from collections import Counter, defaultdict
import datetime

import dataset
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient


def get_mongo_database(db_name, host='localhost', \
                       port=27017, username=None, password=None):
    # setting connection
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s%s' % \
                    (username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db_name]


def mongo_coll_to_dicts(dbname='test', collname='test', \
                        query={}, del_id=True, **kw):
    db = get_mongo_database(dbname, **kw)
    res = list(db[collname].find(query))

    if del_id:
        for r in res:
            r.pop('_id')

    return res


if __name__ == '__main__':
    nobel_winners = [
        {'category': 'Physics',
         'name': 'Albert Einstein',
         'nationality': 'Swiss',
         'sex': 'male',
         'year': 1921},
        {'category': 'Physics',
         'name': 'Paul Dirac',
         'nationality': 'British',
         'sex': 'male',
         'year': 1933},
        {'category': 'Chemistry',
         'name': 'Marie Curie',
         'nationality': 'Polish',
         'sex': 'female',
         'year': 1911}
    ]
    DB_NOBEL_PRIZE = 'nobel_prize'
    COLL_WINNERS = 'winners'
    db = get_mongo_database(DB_NOBEL_PRIZE)
    coll = db[COLL_WINNERS]
    # coll.insert_many(nobel_winners)
    # res = coll.find({'category': 'Chemistry'})
    # print(list(res))
    res = coll.find({'year': {'$gt': 1930}})
    print(list(res))

    res = coll.find({'$or': [{'year': {'$gt': 1930}}, \
                             {'sex': 'female'}]})
    print(list(res))

    print(list(mongo_coll_to_dicts(DB_NOBEL_PRIZE, COLL_WINNERS)))
    d = datetime.datetime.now()
    print(d.isoformat())

    # db = dataset.connect('sqlite:///data/nobel_prize.db')
    # winners = db['winners'].find()
    # datafreeze.freeze(winners, format='csv', \
    #                   filename='data/nobel_winners_ds.csv')
    # open('data/nobel_winners_ds.csv')
    # with db as tx:
    #     for w in nobel_winners:
    #         tx['winners'].insert(w)
    #     print(list(db['winners'].find()))
    # wtable = db['winners']
    # winners = wtable.find()
    # winners = list(winners)
    # print(winners)
    # wtable.drop()
    #
    # wtable = db['winners']
    # print(wtable.find())

    # create session
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # session.query(Winner).filter_by(name='Albert Einstein').delete()
    # print(list(session.query(Winner)))
    # winner_rows = session.query(Winner)
    # nobel_winners = [inst_to_dict(w) for w in winner_rows]
    # # print(nobel_wrint(session.dirty)
    # res = session.query(Winner).order_by('year')
    # print(list(res))
    # albert = Winner(**nobel_winners[0])
    # session.add(albert)
    # session.new
    # session.expunge(albert)
    # session.new
    # winner_rows = [Winner(**w) for w in nobel_winners]
    # session.add_all(winner_rows)
    # session.commit()
    # print(session.query(Winner).count())
    # result = session.query(Winner).filter( \
    #     Winner.category == 'Physics', \
    #     Winner.nationality != 'Swiss')
    # print(session.query(Winner).get(3))

# names = ['Alice', 'Bob', 'Carol']
# for i, n in enumerate(names):
#   print('%d: %s' % (i, n))
#
#
# def fibonacci(n):
#   x, y = 0, 1
#   for i in range(n):
#     print(x)
#     print(y)
#     x, y = y, x
# from functools import reduce

# closure
# def get_counter(inc):
#   count = 0
#   def add():
#     count += inc
#     print('Current count: ' + str(count))
#   return add

# datetime serialize
# class JSONDateTimeEncoder(json.JSONEncoder):
#       def default(self, obj):
#           if isinstance(obj, (datetime.date, datetime.datetime)):
#               return obj.isoformat()
#           else:
#               return json.JSONEncoder.default(self, obj)

# def dumps(obj):
#     return json.dumps(obj, cls=JSONDateTimeEncoder)


# f = open('data/nobel_winners.csv', 'w')
# cols = nobel_winners[0].keys()
# sorted(cols)
#
# with open('data/nobel_winners.csv', 'w') as f:
#   f.write(','.join(cols) + '\n')
#
#   for o in nobel_winners:
#     for col in cols:
#       row = [str(o[col]) for col in cols]
#     f.write(','.join(row) + '\n')
#
# with open('data/nobel_winners.csv') as f:
#   for line in f.readlines():
#     print(line),

# with open('data/nobel_winners.csv', 'w') as f:
#   fieldnames = nobel_winners[0].keys()
#   print(fieldnames)
#   sorted(fieldnames)
#   writer = csv.DictWriter(f, fieldnames=['category', 'name', 'nationality', 'sex', 'year'])
#   writer.writeheader()
#   for w in nobel_winners:
#     writer.writerow(w)

#   with open('/home/ec2-user/environment/sandpit/data/nobel_winners.csv') as f:
#       reader = csv.DictReader(f)
#       nobel_winners = list(reader)
#       print(nobel_winners)

#   with open('/home/ec2-user/environment/sandpit/data/nobel_winners.json', 'w') as f:
#       json.dump(nobel_winners, f)

#   with open('/home/ec2-user/environment/sandpit/data/nobel_winners.json') as f:
#       nobel_winners = json.load(f)
#       print(nobel_winners)
#   now_str = dumps({'time': datetime.datetime.now()})
#   print(now_str)


# lambda
# nums = range(10)
#
# odds = filter(lambda x: x % 2, nums)
# odds_dq = map(lambda x: x * x, odds)
# print(reduce(lambda x, y: x + y, odds_dq))
# odd_squares = [x * x for x in nums if x % 2]
#
# print(sum(odd_squares))
# fibonacci(2)
# winner = 'Albert', 'Physics', 1921, 'Swiss'直
# name, _, _, nationality = winner
# print(name, nationality)
# items = ['F', 'C', 'C', 'A', 'B', 'A', 'C', 'E', 'F']
#
# cntr = Counter(items)
# print(cntr)
# cntr['C'] -= 1
# print(cntr)
#
# d = defaultdict(int)
#
# for item in items:
#   d[item] += 1
#
# print(d)
