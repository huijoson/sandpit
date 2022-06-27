import csv
import json
from collections import Counter, defaultdict
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker

engine = create_engine( \
    'sqlite:///data/nobel_prize.db', echo=True)
Base = declarative_base()


class Winner(Base):
    __tablename__ = 'winners'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))

    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>" \
               % (self.name, self.category, self.year)


def inst_to_dict(inst, delete_id=True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    if delete_id:
        dat.pop('id')
    return dat


Base.metadata.create_all(engine)

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

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Winner).filter_by(name='Albert Einstein').delete()
    print(list(session.query(Winner)))
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
