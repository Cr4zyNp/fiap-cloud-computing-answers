import json
from baseDAO import BaseDAO
from datetime import datetime

def gravarBancoHandler(event,context):
    
    dao = BaseDAO('eventos-pizzaria')
    
    print(json.dumps(event))
    
    dao.put_item(
        {'pedido': str(event['detail']['pedido']),
         'status': str(event['detail']['status']),
         'cliente': str(event['detail']['cliente']),
         'datetime':str(datetime.now())         
       })
     
    print("Gravou")

    return True