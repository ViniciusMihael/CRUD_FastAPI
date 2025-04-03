from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from schemas import UserPublic, UserSchema,UserDB

app = FastAPI()


#Banco de dados 
database = []



#Rota para criar usuarios
@app.post('/users/create_user', status_code=HTTPStatus.CREATED, response_model= UserPublic)
def create_user(user:UserSchema):
        
        # Variavel que recebe user em forma de JSON e adciciona id e soma ele
        user_with_id = UserDB(**user.model_dump(), id= len(database) + 1)
        
        # Adiciona a variavel user_with_id no banco de dados database
        database.append(user_with_id)
        
        # Retorna o usuario criado
        return user_with_id


# Retorna os usuarios no banco de dados
@app.get('/users/{user_id}',status_code=HTTPStatus.OK)
async def read_users(user_id: int):
        '''Recebe o Id do usuario e retorna a informações que estão no banco'''
        usuario = database[user_id - 1]
        return {'users': usuario}


# Recebe o id do usuario para fazer as um put(atualização) dos dados
@app.put('/users/{user_id}', response_model=UserPublic,  status_code=HTTPStatus.OK)
async def update_user(user_id: int, user: UserSchema):
        if user_id > len(database) or user_id < 1:
                raise HTTPException(
                        status_code=HTTPStatus.NOT_FOUND, detail='User not found'
                )
        user_with_id = UserDB(**user.model_dump(), id=user_id)
        database[user_id - 1] = user_with_id
        
        return user_with_id

@app.delete('/users/{user_id}', status_code=HTTPStatus.OK)
async def delete_user(user_id: int):
        if user_id > len(database) or user_id < 1:
                raise HTTPException(
                        status_code= HTTPStatus.NOT_FOUND, detail='User not found'
                )
                
        del database[user_id - 1]
           
        return {'message': 'User deleted'}     