# coding: utf-8

import time
import socket
import serial

bluetoothSerial = serial.Serial("/dev/rfcomm0",baudrate=9600) 	# Permets de communiquer via le com 0 du bluetooth à 9600 bauds

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# initialisation de la partie sockets
socket.bind(('',54000))						# communication sur le port 54000
socket.listen(1) 						# Maximum fil d'attente des appareils qui veulent se connecter 
client, address = socket.accept()
print ("{} connected".format( address ))			# regarde si nous sommes bien connectés 

gauche=0
droite=0

while (1==1):

    try:
         
        msg = client.recv(4) 					# on stoker ce qui est reçu 
        reponse=int(msg)
        
        if(reponse > 300): 					# si la valeur est au-dessus de 300 alors moteur droit 
                droite=reponse-300 
        if(reponse > 255): 					# si la valeur est en dessous de 300 alors moteur gauche 
                gauche=reponse

        trame = [15,int(gauche),int(droite)]			# on envoi reconstitue la trame pour le drone comme celle de l'application 
        print(trame)				                # on écrit les valeurs reçu dans le terminal (vérification)
        bluetoothSerial.write(trame)                            # on envoi la trame au bluetooth                         

    except OSError as e:  					# pour les erreurs  
        print(e)
        client.close()
        #socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #socket.bind(('', 54000))
        socket.listen(5)
        client, address = socket.accept()
        print ("{} connected".format( address ))

client.close()
stock.close()