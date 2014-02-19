# Start testing on the scraping script.
import urllib2
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen("http://www.timeanddate.+\
                                     com/worldclock/astron+\
                                     omy.html?n=78").read())

for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
    rowdt = row('td')
    print rowdt[0].string, rowdt[1].string


def main():
    print "Welcome to python mode presentation"

if __name__ == "__main__":
    main()
