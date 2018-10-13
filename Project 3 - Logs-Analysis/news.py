#!/usr/bin/env python

import psycopg2
DBNAME = "news"


# CONNECT TO DATABASE
def connect():
    return psycopg2.connect(dbname=DBNAME)


# MOST POPULAR POSTS
def get_popular_articles():
    db = connect()
    c = db.cursor()
    c.execute('''
        select articles.title, count(*) as views
        from articles inner join log on log.path
        like concat('%', articles.slug, '%')
        where log.status like '%200%' group by
        articles.title, log.path order by views desc limit 3''')
    for row in c:
        print ("'" + row[0] + "'" + " - " + str(row[1]) + " views")
    db.close()


# MOST POPULAR AUTHORS
def get_popular_authors():
    db = connect()
    c = db.cursor()
    c.execute('''
        select authors.name, count(*) as views from articles inner
        join authors on articles.author = authors.id inner join log
        on log.path like concat('%', articles.slug, '%') where
        log.status like '%200%' group by authors.name
        order by views desc limit 4
        ''')
    for row in c:
        print ("'" + row[0] + "'" + " - " + str(row[1]) + " views")
    db.close()


# ON WHICH DAYS DID MORE THAN 1% OF REQUESTS LEAD TO ERRORS?
def get_errors_over_one_percent():
    db = connect()
    c = db.cursor()
    c.execute('''
        select day, perc from (select day, round(
        (sum(requests)/(select count(*) from log
        where time::date = day) * 100), 2)
        as perc from (select time::date as day,
        count(*) as requests from log where status
        like '%404%' group by day) as log_percentage
        group by day order by perc desc) as result
        where perc >= 1
    ''')
    for row in c:
        print(str(row[0]) + " - " + format(row[1]) + '% errors')
    db.close()


# Runs and prints results with magic
if __name__ == "__main__":
    print ("\nMOST POPULAR ARTICLES\n")
    get_popular_articles()

    print("\nMOST POPULAR AUTHORS\n")
    get_popular_authors()

    print("\nON WHICH DAYS DID MORE THAN 1% OF REQUESTS LEAD TO ERRORS?\n")
    get_errors_over_one_percent()

    # Add empty line at the end
    print("\n")
