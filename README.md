# benford-index

<a href="https://en.wikipedia.org/wiki/Benford%27s_law">Benford's law</a> is phenomenon whereby the leading digits of some types of stochastic data follow a particular distribution.
There have been several suggestions as to why this occurs however there is considerable debate as to the cause.

<img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Rozklad_benforda.svg" width="50%" height="50%" align="right">

The distribution has been widely used in forensic data analysis, for example in identifying where companies might be cooking the books. Other research has compared the benford distribution with data from <a href="http://link.springer.com/chapter/10.1007%2F978-88-470-1481-7_10">financial markets</a>. Research indicates that typical (low volatility) market days follow the Benford distribution while high volatility days do not. 

With this idea in mind, this project compares the Beford distribution with characteristics of several major market indices (S&P 500, FTSE 100 etc) in order to (initially) develop a measure of financial volatitity.

The code incorporates a beautiful soup/python scraper which fetches index prices at minute resolution Yahoo Finance, stores them in a MySQL database and then calculates how the distribution of the differences between stock prices from minute to minute compare with the Benford distribution
