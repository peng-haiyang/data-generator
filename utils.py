def random_date(start=dt.datetime(2019, 6, 1, 0, 0, 0)):
    current = start
    curr = current + dt.timedelta(days=randrange(30), hours=randrange(24), minutes=randrange(60), seconds=randrange(60))
    return curr
# example
#start_date = dt.datetime(2015, 7, 1, 0, 0, 0)
#for x in random_date(start_date, 3):
#    print(x)
#2016-06-15 09:38:43
#2016-08-03 05:23:12
#2016-04-10 19:50:39
# 20150701 20161231

# seq = {"A":30, "B":40, "C":30}
def w_choice(seq):
    total_prob = sum(seq[item] for item in seq)
    chosen = random.uniform(0, total_prob)
    cumulative = 0
    for item, probality in seq.items():
        cumulative += probality
        if cumulative > chosen:
            return item