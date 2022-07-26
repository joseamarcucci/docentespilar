import streamlit as st
from ftplib import FTP 
import os
import fileinput

import cv2  
import qrcode
import datetime
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image
import urllib.request
import urllib.request as url
from oauth2client.service_account import ServiceAccountCredentials
urllib.request.urlretrieve('https://entendiste.ar/mail/service_account.json',"service_account.json")
from gspread import authorize
from datetime import date, timedelta, datetime
import time
def path_to_image_html(path):
    return '<img src="'+ path + '" width="120" >'
def load_image(image_file):
	img = Image.open(image_file)
	return img
from oauth2client.service_account import ServiceAccountCredentials

scopes = ["https://spreadsheets.google.com/feeds",
                  "https://www.googleapis.com/auth/spreadsheets",
                  "https://www.googleapis.com/auth/drive",
                  "https://www.googleapis.com/auth/drive"]
cred = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scopes)
gclient = authorize(cred)
dni=st.text_input('dni')
sheet2 = gclient.open('Alumnos').worksheet('2022')



qr = qrcode.QRCode()
previews2=[]
previews21=[]
previews22=[]
ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('ftp.appys.ar', 21) 
ftp.login("files_22@appys.ar", "subirfiles2022")

ftp.cwd('/')
if (dni):
  cell = sheet2.find(dni) 
  row_number = cell.row

  nombre=sheet2.acell('C'+str(row_number)).value
  dni=sheet2.acell('D'+str(row_number)).value
  parada=sheet2.acell('J'+str(row_number)).value 
  tipo= sheet2.acell('L'+str(row_number)).value 
  todos=sheet2.acell('S'+str(row_number)).value 
  dia1=sheet2.acell('n'+str(row_number)).value 
  dia12=sheet2.acell('o'+str(row_number)).value 
  dia13=sheet2.acell('p'+str(row_number)).value 
  dia14=sheet2.acell('q'+str(row_number)).value 
  dia15=sheet2.acell('r'+str(row_number)).value 
  diar1=sheet2.acell('t'+str(row_number)).value 
  diar12=sheet2.acell('u'+str(row_number)).value 
  diar13=sheet2.acell('v'+str(row_number)).value 
  diar14=sheet2.acell('w'+str(row_number)).value 
  diar15=sheet2.acell('x'+str(row_number)).value 
  diat=sheet2.acell('s'+str(row_number)).value 
  diar1r=sheet2.acell('t1').value 
  diar12r=sheet2.acell('u1').value 
  diar13r=sheet2.acell('v1').value 
  diar14r=sheet2.acell('w1').value 
  diar15r=sheet2.acell('x1').value
  import datetime as DT
  today = DT.date.today()
  week_ago = today + DT.timedelta(days=31)
  firstDay = st.date_input('Desde :')
  firstDay.strftime('%d-%m-%y')
  lastDay = st.date_input('Hasta :',week_ago)
  lastDay.strftime('%d-%m-%y')
  #st.write('Período: '+firstDay+' a '+lastDay)

  if dia1=='Lunes' or diat=='Lunes a viernes':

      weekDay = 'Monday'


      dates = [firstDay + timedelta(days=x) for x in range((lastDay-firstDay).days + 1) if (firstDay + timedelta(days=x)).weekday() == time.strptime(weekDay, '%A').tm_wday]
      dff=[dia.strftime('%d-%m-%y') for dia in dates] 
      dff=pd.DataFrame(dff)
       
      


      lista = dff.values.tolist()


      for  dia in lista:
        #st.write(dia)
        qr =qrcode.QRCode(version=1,box_size=8)
        qr.add_data(tipo)    
        qr.add_data('\n')      
        qr.add_data(nombre)
        qr.add_data('\n')     
        qr.add_data(dni)
        qr.add_data('\n')        
        qr.add_data('IDA')      
        qr.add_data('\n')      
        qr.add_data('Lunes')   
        qr.add_data('\n')
        qr.add_data(dia)          
        qr.add_data('\n')      
        qr.add_data(parada)
        qr.add_data('\n')
        
        qr.add_data('REGRESO')
            
        qr.add_data('\n')
        qr.add_data('Lunes')
        qr.add_data('\n')              
        qr.add_data(diar1)      
            

        qr.make(fit=True)
        url= qr.make_image()
        url.save(f"{dni}_{dia}.png", "PNG")
        barcode=str(dni)
        img = cv2.imread(dni+"_"+str(dia)+".png")
        #print(type(img))
        cv2.imwrite(dni+"_"+str(dia)+".png",img)
        im = Image.open(dni+"_"+str(dia)+".png")
        im.show()

        file = open(dni+"_"+str(dia)+".png",'rb')   
      
        ftp.storbinary("STOR "+dni+"_"+str(dia)+".png", file) 

        diaa = ', '.join(dia)
        entrada_preview2 = { 
      
          
          'Día':'Lunes',
          'Fecha':diaa,
          
          'Qr':"https://appys.ar/subir/"+dni+"_"+str(dia)+".png"

          }
        previews2.append(entrada_preview2)
        previews21=pd.DataFrame(previews2)
        file.close()
        

        st.write('Lunes',diaa)
        st.image("https://appys.ar/subir/"+dni+"_"+str(dia)+".png") 

    
      
  if dia12=='Martes' or diat=='Lunes a viernes':

      weekDay = 'Tuesday'


      dates = [firstDay + timedelta(days=x) for x in range((lastDay-firstDay).days + 1) if (firstDay + timedelta(days=x)).weekday() == time.strptime(weekDay, '%A').tm_wday]
      dff=[dia.strftime('%d-%m-%y') for dia in dates] 
      dff=pd.DataFrame(dff)
      



      lista = dff.values.tolist()


      for  dia in lista:
        qr =qrcode.QRCode(version=1,box_size=8)
        qr.add_data(tipo)    
        qr.add_data('\n')      
        qr.add_data(nombre)
        qr.add_data('\n')     
        qr.add_data(dni)
        qr.add_data('\n')        
        qr.add_data('IDA')      
        qr.add_data('\n')      
        qr.add_data('Martes')   
        qr.add_data('\n')
        qr.add_data(dia)          
        qr.add_data('\n')      
        qr.add_data(parada)
        qr.add_data('\n')
        
        qr.add_data('REGRESO')
            
        qr.add_data('\n')
        qr.add_data(diar12r)
        qr.add_data('\n')        
        qr.add_data(diar12)  

        qr.make(fit=True)
        url= qr.make_image()
        url.save(f"{dni}_{dia}.png", "PNG")
        barcode=str(dni)
        img = cv2.imread(dni+"_"+str(dia)+".png")
        #print(type(img))
        cv2.imwrite(dni+"_"+str(dia)+".png",img)
        im = Image.open(dni+"_"+str(dia)+".png")
        im.show()

        file = open(dni+"_"+str(dia)+".png",'rb')   
        
        ftp.storbinary("STOR "+dni+"_"+str(dia)+".png", file) 

        diaa = ', '.join(dia)
        entrada_preview2 = { 
                 
          'Día':'Martes',
          'Fecha':diaa,
          'Qr':"https://appys.ar/subir/"+dni+"_"+str(dia)+".png"

          }
        previews2.append(entrada_preview2)
        previews21=pd.DataFrame(previews2)
        file.close()

        st.write('Martes',diaa)
        st.image("https://appys.ar/subir/"+dni+"_"+str(dia)+".png") 

    
  if dia13=='Miércoles' or diat=='Lunes a viernes':

      weekDay = 'Wednesday'

      dates = [firstDay + timedelta(days=x) for x in range((lastDay-firstDay).days + 1) if (firstDay + timedelta(days=x)).weekday() == time.strptime(weekDay, '%A').tm_wday]
      dff=[dia.strftime('%d-%m-%y') for dia in dates] 
      dff=pd.DataFrame(dff)
      



      lista = dff.values.tolist()


      for  dia in lista:
        qr =qrcode.QRCode(version=1,box_size=8)
        qr.add_data(tipo)    
        qr.add_data('\n')      
        qr.add_data(nombre)
        qr.add_data('\n')     
        qr.add_data(dni)
        qr.add_data('\n')        
        qr.add_data('IDA')      
        qr.add_data('\n')      
        qr.add_data('Miércoles')   
        qr.add_data('\n')
        qr.add_data(dia)          
        qr.add_data('\n')      
        qr.add_data(parada)
        qr.add_data('\n')
        
        qr.add_data('REGRESO')
            
        qr.add_data('\n')
        qr.add_data('Miércoles')
        qr.add_data('\n')        
        qr.add_data(diar13)  

        qr.make(fit=True)
        url= qr.make_image()
        url.save(f"{dni}_{dia}.png", "PNG")
        barcode=str(dni)
        img = cv2.imread(dni+"_"+str(dia)+".png")
        #print(type(img))
        cv2.imwrite(dni+"_"+str(dia)+".png",img)
        im = Image.open(dni+"_"+str(dia)+".png")
        im.show()

        file = open(dni+"_"+str(dia)+".png",'rb')   
        
        ftp.storbinary("STOR "+dni+"_"+str(dia)+".png", file) 

        diaa = ', '.join(dia)
        entrada_preview2 = { 
                 
          'Día':'Miércoles',
          'Fecha':diaa,
          'Qr':"https://appys.ar/subir/"+dni+"_"+str(dia)+".png"

          }
        previews2.append(entrada_preview2)
        previews21=pd.DataFrame(previews2)
        file.close()

        st.write('Miércoles',diaa)
        st.image("https://appys.ar/subir/"+dni+"_"+str(dia)+".png") 


  if dia14=='Jueves' or diat=='Lunes a viernes':

      weekDay = 'Thursday'


      dates = [firstDay + timedelta(days=x) for x in range((lastDay-firstDay).days + 1) if (firstDay + timedelta(days=x)).weekday() == time.strptime(weekDay, '%A').tm_wday]
      dff=[dia.strftime('%d-%m-%y') for dia in dates] 
      dff=pd.DataFrame(dff)
      



      lista = dff.values.tolist()


      for  dia in lista:

        qr =qrcode.QRCode(version=1,box_size=8)
        qr.add_data(tipo)    
        qr.add_data('\n')      
        qr.add_data(nombre)
        qr.add_data('\n')     
        qr.add_data(dni)
        qr.add_data('\n')        
        qr.add_data('IDA')      
        qr.add_data('\n')      
        qr.add_data('Jueves')   
        qr.add_data('\n')
        qr.add_data(dia)          
        qr.add_data('\n')      
        qr.add_data(parada)
        qr.add_data('\n')
        
        qr.add_data('REGRESO')
            
        qr.add_data('\n')
        qr.add_data('Jueves')
        qr.add_data('\n')        
        qr.add_data(diar14)  

        qr.make(fit=True)
        url= qr.make_image()
        url.save(f"{dni}_{dia}.png", "PNG")
        barcode=str(dni)
        img = cv2.imread(dni+"_"+str(dia)+".png")
        #print(type(img))
        cv2.imwrite(dni+"_"+str(dia)+".png",img)
        im = Image.open(dni+"_"+str(dia)+".png")
        im.show()

        file = open(dni+"_"+str(dia)+".png",'rb')   
        
        ftp.storbinary("STOR "+dni+"_"+str(dia)+".png", file) 
        diaa = ', '.join(dia)

        entrada_preview2 = { 
                  
          'Día':'Jueves',
          'Fecha':diaa,
          'Qr':"https://appys.ar/subir/"+dni+"_"+str(dia)+".png"

          }
        previews2.append(entrada_preview2)
        previews21=pd.DataFrame(previews2)
        file.close()
        
        st.write('Jueves',diaa)
        st.image("https://appys.ar/subir/"+dni+"_"+str(dia)+".png") 

    
  if dia15=='Viernes' or diat=='Lunes a viernes':

      weekDay = 'Friday'


      dates = [firstDay + timedelta(days=x) for x in range((lastDay-firstDay).days + 1) if (firstDay + timedelta(days=x)).weekday() == time.strptime(weekDay, '%A').tm_wday]
      dff=[dia.strftime('%d-%m-%y') for dia in dates] 
      dff=pd.DataFrame(dff)
      



      lista = dff.values.tolist()


      for  dia in lista:
        qr =qrcode.QRCode(version=1,box_size=8)
        qr.add_data(tipo)    
        qr.add_data('\n')      
        qr.add_data(nombre)
        qr.add_data('\n')     
        qr.add_data(dni)
        qr.add_data('\n')        
        qr.add_data('IDA')      
        qr.add_data('\n')      
        qr.add_data('Viernes')   
        qr.add_data('\n')
        qr.add_data(dia)          
        qr.add_data('\n')      
        qr.add_data(parada)
        qr.add_data('\n')
        
        qr.add_data('REGRESO')
            
        qr.add_data('\n')
        qr.add_data('Viernes')
        qr.add_data('\n')        
        qr.add_data(diar15)  

        qr.make(fit=True)
        url= qr.make_image()
        url.save(f"{dni}_{dia}.png", "PNG")
        barcode=str(dni)
        img = cv2.imread(dni+"_"+str(dia)+".png")
        #print(type(img))
        cv2.imwrite(dni+"_"+str(dia)+".png",img)
        im = Image.open(dni+"_"+str(dia)+".png")
        im.show()

        file = open(dni+"_"+str(dia)+".png",'rb')   
        
        ftp.storbinary("STOR "+dni+"_"+str(dia)+".png", file) 

        diaa = ', '.join(dia)
        entrada_preview2 = { 
          
          'Día':'Viernes',
          'Fecha':diaa,
          'Qr':"https://appys.ar/subir/"+dni+"_"+str(dia)+".png"

          }
        previews2.append(entrada_preview2)
        previews21=pd.DataFrame(previews2)
        file.close()

        st.write('Viernes',diaa)
        st.image("https://appys.ar/subir/"+dni+"_"+str(dia)+".png") 
       
#st.write(previews21.to_html(escape=False, formatters=dict(Qr=path_to_image_html)))
#HTML(previews21.to_html(escape=False,formatters=dict(Qr=path_to_image_html)))
components.html(previews21.to_html(escape=False,formatters=dict(Qr=path_to_image_html)), width=900, height=1300)
