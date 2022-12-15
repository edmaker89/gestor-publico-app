from sqlalchemy import create_engine
import json
import psycopg2


#conexão banco de dados ponto eletronico 8.5 postgre_sql
#sistema herdado do TJ-GO

class Database:

    def get_connection_spe(db_name):

        if db_name == 'spe':
            with open("connections/spe.json") as spe:
                data_spe = json.load(spe)

            sgdb = data_spe['sgdb']
            hostname = data_spe['hostname']
            port = data_spe['port']
            database = data_spe['database']
            username = data_spe['username']
            pwd = data_spe['pwd']


            try:
                engine = create_engine(fr'{sgdb}://{username}:{pwd}@{hostname}:{port}/{database}')
                print('conectado...')
                return engine
            except Exception as e:
                print(f'não conseguiu conectar, {e}')
                return engine
        else:
            message = {'message': 'banco de dados não encontrado ou não existe'}
            print(message['message'])
            return {'result': message}, 500
