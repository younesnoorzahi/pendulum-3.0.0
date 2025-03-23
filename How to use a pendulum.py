import pendulum

now_in_paris = pendulum.now('Europe/Paris')
>>> now_in_paris
'2016-07-04T00:49:58.502116+02:00'

# Seamless timezone switching
now_in_paris.in_timezone('UTC')
'2016-07-03T22:49:58.502116+00:00'

tomorrow = pendulum.now().add(days=1)
last_week = pendulum.now().subtract(weeks=1)

past = pendulum.now().subtract(minutes=2)
past.diff_for_humans()
'2 minutes ago'

delta = past - last_week
delta.hours
23
delta.in_words(locale='en')
'6 days 23 hours 58 minutes'

# Proper handling of datetime normalization
pendulum.datetime(2013, 3, 31, 2, 30, tz='Europe/Paris')
'2013-03-31T03:30:00+02:00' # 2:30 does not exist (Skipped time)

# Proper handling of dst transitions
just_before = pendulum.datetime(2013, 3, 31, 1, 59, 59, 999999, tz='Europe/Paris')
'2013-03-31T01:59:59.999999+01:00'
just_before.add(microseconds=1)
'2013-03-31T03:00:00+02:00'
