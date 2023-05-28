# Wikiviews
## A command line tool to fetch Wikipedia analytics from the Pageview API
See: https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews

Prompts user to select monthly pageviews for a specific article in a user-defined year, or the most viewed articles in a user-defined month and year. In the latter case, user can also limit the returned list to the top n articles. 

The program will return a table of the pageviews for each month, or a table of the most viewed articles in the given time period, depending on user selection. Uses the tablify package to convert JSON data into tables.

Done as final project for CS50 Python: https://cs50.harvard.edu/python/2022/project/
