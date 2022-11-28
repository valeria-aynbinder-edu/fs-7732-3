# s = {'orange', 'red', 'green'}
# s = set()
# l = []
# l = list()
# d = {}
# d = dict()
# t = ()
# t = tuple()

# s = {'orange', 'red', 'green'}

# s[0]
# s.add('orange')
# print(s)

lecture_days = {'mon', 'thur'}
project_days = {'sun', 'mon', 'wed'}
lec_and_proj = lecture_days.intersection(project_days)
print(lec_and_proj)
busy_days = lecture_days.union(project_days)
print(busy_days)
week_days = {'sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat'}
free_days = week_days.difference(busy_days)
print(free_days)

