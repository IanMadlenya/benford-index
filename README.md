# benford-index

<a href="https://en.wikipedia.org/wiki/Benford%27s_law">Benford's law</a> is phenomenon whereby the leading digits of some types of stochastic data follow a particular distribution.
There have been several suggestions as to why this occurs however there is considerable debate as to the cause.

<img src="https://raw.githubusercontent.com/nowaycomputer/benford-index/master/benford.png" width="50%" height="50%" align="right">

The distribution has been widely used in forensic data analysis, for example in identifying where companies might be cooking the books. Other research has compared the benford distribution with data from <a href="http://link.springer.com/chapter/10.1007%2F978-88-470-1481-7_10">financial markets</a> and indicates that typical (low volatility) market days follow the Benford distribution while high volatility days do not. 

With this idea in mind, this project compares the Beford distribution with characteristics of several major market indices (S&P 500, FTSE 100 etc) in order to (initially) develop a measure of financial volatitity.

The code incorporates a mostly working beautiful soup/python scraper which fetches index prices at minute resolution Yahoo Finance, stores them in a MySQL database and then calculates how the distribution of the differences between stock prices from minute to minute compare with the Benford distribution.

By default the scraper doesn't run and the analysis is done only on test data, specified in app.py

The most interesting thing so far: indices (S&P 500, FTSE etc) follow Benfords laws a LOT more closely than individual stocks do - play around with the test data to see!

# Notes

- Currently test data is the only way of running the app as database fetching of data hasn't been implemented yet
- Test data is in CSV files, from whichever source you choose in the form of three columns: date, time, value - you could use a single datetime column but you'll have to update the column in line 32 of app.py
- The data scraper operates at times when the markets should be open on weekdays (holidays are not yet handled and will result in recording some static data on those days)
- The stock values are recorded in local time, so that later it will be easier to pull out 'days' of data - but then again, this might make it harder to consolidate
- Python lib requirements are minimal, the only non-standard (default) libraries are <a href="https://pypi.python.org/pypi/MySQL-python">MySQLdb</a> and <a href="http://www.crummy.com/software/BeautifulSoup/">Beautiful Soup</a>
- With the scraper enabled, the code will die horribly unless there's a mysql database called 'benfordindex' with the username 'benford' and the password 'index' (you can change these in database.py)
- The chi-squared test doesn't seem very useful right now, a better statistical test is required based on the type and size of the data
- This has all been written in short bursts, whenever I have had time, so there are likely some flaws and there is almost nothing in the way of error handling

