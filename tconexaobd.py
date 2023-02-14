import sqlalchemy


engine = create_engine('mysql+pymsql://root:dulguiga16@lovalhost:3306/comissaom')
conn = engine.connect()

if conn.is_connected():
    print('conn')
