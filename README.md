<h1>pendulum-3.0.0</h1>
<h4>Why Pendulum?</h4>
<p>Native datetime instances are enough for basic cases but when you face more complex use-cases they often show limitations and are not so intuitive to work with. Pendulum provides a cleaner and more easy to use API while still relying on the standard library. So it’s still datetime but better.

Unlike other datetime libraries for Python, Pendulum is a drop-in replacement for the standard datetime class (it inherits from it), so, basically, you can replace all your datetime instances by DateTime instances in your code (exceptions exist for libraries that check the type of the objects by using the type function like sqlite3 or PyMySQL for instance).

It also removes the notion of naive datetimes: each Pendulum instance is timezone-aware and by default in UTC for ease of use.

Pendulum also improves the standard timedelta class by providing more intuitive methods and properties.</p>

<h1>Resources</h1>
<li><a href="https://pendulum.eustace.io/">Official Website</a></li>
<li><a href="https://pendulum.eustace.io/docs/">Documentation</a></li>
<li><a href="https://github.com/python-pendulum/pendulum/issues">Issue Tracker</a></li>

<h1>Limitations</h1>
<p>Even though the DateTime class is a subclass of datetime there are some rare cases where it can’t replace the native class directly. Here is a list (non-exhaustive) of the reported cases with a possible solution, if any:</p>
<li>sqlite3 will use the type() function to determine the type of the object by default. To work around it you can register a new adapter:</li>

```
from pendulum import DateTime
from sqlite3 import register_adapter

register_adapter(DateTime, lambda val: val.isoformat(' '))
```
