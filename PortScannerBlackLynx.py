import socket
import time

print ("""
   ___           _                                         _                  
  / _ \___  _ __| |_ ___  ___ __ _ _ __  _ __   ___ _ __  | |__  _   _        
 / /_)/ _ \| '__| __/ __|/ __/ _` | '_ \| '_ \ / _ \ '__| | '_ \| | | |       
/ ___/ (_) | |  | |_\__ \ (_| (_| | | | | | | |  __/ |    | |_) | |_| |       
\/    \___/|_|   \__|___/\___\__,_|_| |_|_| |_|\___|_|    |_.__/ \__, |       
                                                                 |___/        
   ___ _            _        __                    _____                      
  / __\ | __ _  ___| | __   / / _   _ _ __ __  __ /__   \___  __ _ _ __ ___   
 /__\// |/ _` |/ __| |/ /  / / | | | | '_ \\ \/ /   / /\/ _ \/ _` | '_ ` _ \  
/ \/  \ | (_| | (__|   <  / /__| |_| | | | |>  <   / / |  __/ (_| | | | | | | 
\_____/_|\__,_|\___|_|\_\ \____/\__, |_| |_/_/\_\  \/   \___|\__,_|_| |_| |_| 
                                |___/                                         
""")

ports =[21,22,80,443,445,3306,25] 
site = input ("Target = ")
for port in ports:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(1)
    
     code = client.connect_ex (((site), port))
     print (code)
     if code==0:
       print(port ,"Open Door")
     else:
       print(port , "Closed door"); 
time.sleep(1)     
print("Scan finished")
time.sleep(10)

