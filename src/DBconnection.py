#!/usr/bin/python2.7
import MySQLdb
import os

import pandas as pd
import numpy as np

from datetime import datetime
from constant import * # self-defined Constant


def MySQLConnectionNoOutput(query, MySQL_config = MySQLConfig.copy()):
    """
    This function will do delete or update queries. There will be no return value
    """
    print "################## Connecting {host} ...".format(**MySQL_config)
    db = MySQLdb.connect(**MySQL_config)
    cur = db.cursor()
    print "################## Excuting Queries ..."
    cur.execute(query)
    db.commit()
    db.close()

def MySQLConnectionWithOutput(query, MySQL_config = MySQLConfig.copy()):
    """
    This function will return a dataFrame.
    """
    # host = np.random.choice(Hosts,1)[0]
    num = os.getpid() % 4 + 1
    MySQL_config['host'] = Hosts[num]

    print "################## Connecting {host} ...".format(**MySQL_config)

    db = MySQLdb.connect(**MySQL_config)
    cur = db.cursor()
    
    print "################## Excuting Queries ..."
    print query
    
    t0 = datetime.now()
    
    cur.execute(query)
    print "################## Retrieving Data ..."
    names = [i[0] for i in cur.description]
    queryResult = cur.fetchall()
    output = [x for x in queryResult]
    db.close()
    df = pd.DataFrame(output, columns = names)

    t1 = datetime.now()
    print "################## Closing Connection with {host} ...".format(**MySQL_config)
    print "# Runing time of Data retrieving" + str(t1 - t0)
    return df
