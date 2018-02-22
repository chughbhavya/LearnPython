'''
This program gets data from a wiki page using beautiful soup library in python and then puts it into mysql database. This program is tailored for the accessing wiki page only.
'''
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import pymysql

class DataToSQL:
    wiki = ''
    def get_data(self):
            http = urllib3.PoolManager()
            r = http.request('GET', wiki)
            soup = BeautifulSoup(r.data, 'html.parser')
            all_tables = soup.find('table', class_='wikitable sortable plainrowheaders')
            A = []
            b = []
            c = []
            for row in all_tables.findAll('tr'):
                    cells = row.findAll('td')
                    states = row.findAll('th')
                    if len(cells) == 6:
                        A.append(cells[0].find(text= True))
                        b.append(states[0].find(text=True))
                        c.append(cells[1].find(text= True))
            df = pd.DataFrame(A, columns=['Number'])
            df['State'] = b
            df['Capital'] = c
            return df

    def create_connection(self,df):
        self.df = df
        try:
            engine = create_engine("mysql+pymysql://root:bhavya26@localhost/states and capitals")
            conn = engine.connect()
            print("Connection success")
            df.to_sql(name='states_table', con=conn, if_exists='replace', index=False)
            conn.close()
        except Exception as e:
            print("The exception is {0} generated for {1}".format(str(e), wiki))

    def __init__(self,wiki):
        self.wiki = wiki

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
data = DataToSQL(wiki)
df = data.get_data()
print("Got data")
print (df)
data.create_connection(df)
