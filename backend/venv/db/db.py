
from sqlalchemy import Table, Column, Integer, String, Text, ARRAY, create_engine, MetaData

topics = set(['any'])

# Login
def name_or_url(username: str, password: str, db: str='defaultdb'):
    """

    Args:
        username (str): User's username
        password (str): User's password
        db (str, optional): Initial database to connect. Defaults to 'defaultdb'.

    Returns:
        str: url string for engine to connect with
    """
    return f'cockroachdb://{username}:{password}@localhost:26257/{db}?sslcert=certs%5Cclient.root.crt&sslkey=certs%5Cclient.root.key&sslmode=require&sslrootcert=certs%5Cca.crt'

username = 'fennec2000'
password = 'pass'
engine = create_engine(name_or_url=name_or_url(username=username, password=password), echo=True)

# Creating single database and table
conn = engine.connect()
conn.execute("CREATE DATABASE IF NOT EXISTS notes_db")
conn.execute('SET database = notes_db')
conn.execute("commit")
conn.close()
engine.dispose()

# Restarting engine with newly created database
db = 'notes_db'
engine = create_engine(name_or_url=name_or_url(username=username, password=password, db=db), echo=True)

meta = MetaData()
notes = Table('notes', meta,
            Column(name='id', type_=Integer, primary_key=True, autoincrement=True),
            Column(name='title', type_=String, nullable=False, unique=True),
            Column(name='topics', type_=ARRAY(String), nullable=True, default=ARRAY(['any'])),
            Column(name='original', type_=Text, nullable=False),
            Column(name='summary', type_=Text, nullable=False))

notes.create(bind=engine, checkfirst=True)
