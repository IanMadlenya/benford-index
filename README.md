# benford-index

<a href="https://en.wikipedia.org/wiki/Benford%27s_law">Benford's law</a> is phenomenon whereby the leading digits of some types of stochastic data follow a particular distribution.
There have been several suggestions as to why this occurs however there is considerable debate as to the cause.

<img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Rozklad_benforda.svg" width="50%" height="50%" align="right">

The distribution has been widely used in forensic data analysis, for example in identifying where companies might be cooking the books. Other research has compared the benford distribution with data from <a href="http://link.springer.com/chapter/10.1007%2F978-88-470-1481-7_10">financial markets</a>. Research indicates that typical (low volatility) market days follow the Benford distribution while high volatility days do not. 

With this idea in mind, this project compares the Beford distribution with characteristics of several major market indices (S&P 500, FTSE 100 etc) in order to (initially) develop a measure of financial volatitity.

The code incorporates a beautiful soup/python scraper which fetches index prices at minute resolution Yahoo Finance, stores them in a MySQL database and then calculates how the distribution of the differences between stock prices from minute to minute compare with the Benford distribution

# Notes

- Currently only the index price scraper works, no analysis is performed and there is no interface to speak of
- The data is scraped at times when the markets should be open on weekdays (holidays are not yet handled and will result in recording some static data on those days)
- The stock values are recorded in local time, so that later it will be easier to pull out 'days' of data
- Python lib requirements are minimal, the only non-standard (default) libraries I can think of is <a href="https://pypi.python.org/pypi/MySQL-python">MySQLdb</a> and <a href="http://www.crummy.com/software/BeautifulSoup/">Beautiful Soup</a>
- The code will die horribly unless there's a mysql database called 'benfordindex' with the username 'benford' and the password 'index' (you can change these in database.py
