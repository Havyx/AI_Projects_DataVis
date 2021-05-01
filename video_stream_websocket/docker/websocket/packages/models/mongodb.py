from pymongo import MongoClient, DESCENDING

class HandleDB:
    def __init__(self):
        print('Se conectando a base de dados...')
        self.client = MongoClient('mongodb://localhost:27017/')
        print(self.client.list_database_names())
        self.db = self.client.dbcv
        self.face = self.db['face']
        if self.face:
            print('Concectado com sucesso')
        else: print('Falha ao se conectar')

    def atualiza(self, dict_data):
        self.face.insert(dict_data)
    
    def filtro(self):
        return self.face.find({}).sort("$natural", DESCENDING).limit(60)
#########################################################################
