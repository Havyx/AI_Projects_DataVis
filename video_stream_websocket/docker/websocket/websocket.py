import sys
import cv2
import time
import base64
import asyncio
import websockets
import json #codecs
from packages.face import reconhecimentoFacial
from packages.models.mongodb import HandleDB

####################################################################################################################################################################
async def QSocket(websocket, path):
    flag = 0
    countFrames = 0
    while True:
        new_message = await websocket.recv()
        if new_message:
            message = new_message
            await asyncio.sleep(0.2)
            try:
                frame, countFrames, flag = reconhecimentoFacial(message, countFrames, flag)
            except: print('Aproxime-se da camera')
        try:
            btframe = base64.b64encode(frame) #new_img = Image.fromarray(frame)
            await websocket.send(btframe) #await websocket.send(json.dumps(frame))
        except: print('Erro ao enviar bytes')
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            cv2.destroyAllWindows()
            sys.exit()

####################################################################################################################################################################
async def MongoSocket(websocket, path):
    QE = HandleDB()
    while True:
        dados = []
        message = await websocket.recv()
        print(message)
        try:
            cursor = QE.filtro()
            for doc in cursor:
                dados.insert(0, {'frame': doc['frame'], 'flag': doc['flag'], 'IMAR_value': doc['IMAR'], 'faceHorizontal_value': doc['faceHorizontal'], 'faceVertical_value': doc['faceVertical'], 'leftEAR_value': doc['leftEAR'], 'rightEAR_value': doc['rightEAR']})
            await asyncio.sleep(2)
            dados_de_envio = dados
            print('Dados Enviados a cada 2 segundos')
            await websocket.send(json.dumps(dados_de_envio))
        except: print("Algo deu errado!!!")


####################################################################################################################################################################
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(websockets.serve(QSocket, "0.0.0.0", 3333))
    #loop.run_until_complete(websockets.serve(MongoSocket, "127.0.0.1", 3332))
    loop.run_forever()

    #StartServer1 = websockets.serve(QSocket, "127.0.0.1", 3333)
    #print('Inicializando Server 127.0.0.1:3333...')
    #StartServer2 = websockets.serve(MongoSocket, "127.0.0.1", 3330)
    #print('Inicializando Server 127.0.0.1:3330...')
    #asyncio.get_event_loop().run_until_complete(StartServer1)
    #asyncio.get_event_loop().run_until_complete(StartServer2)
    #print('Servidores inicializados com sucesso!')
    #asyncio.get_event_loop().run_forever()