import pypyodbc


DATABASE_CONFIG ={
    'Driver': 'SQL Server',
    'Server': 'AVULAPRATHYUSHA',
    'Database': 'Todo'
    }

# Return the sql connection 
def getConnection():
     connection = pypyodbc.connect("Driver= {"+DATABASE_CONFIG["Driver"]+"} ;
     Server=" + DATABASE_CONFIG["Server"] + ";
     Database=" + DATABASE_CONFIG["Database"] + ")
    #  uid=" + DATABASE_CONFIG["UID"] + ";pwd=" + DATABASE_CONFIG["Password"])
     return connection 