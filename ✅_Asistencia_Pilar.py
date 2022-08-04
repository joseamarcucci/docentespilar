import streamlit as st
st.set_page_config(
page_title="USAL QR para Registro Docentes",
page_icon="https://webinars.usal.edu.ar/sites/default/files/favicon.ico",
layout="wide"

)
import pytz
import os
argentina = pytz.timezone('America/Argentina/Buenos_Aires')
import geocoder
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styledocentes.css")
col1, col2,col3 = st.columns([1,2,1])
#vivod=df.iat[1,1]
#vivom=df.iat[0,1]

col12, col22,col32 = st.columns([1,2,1])
arriba=st.empty()
from datetime import timezone, datetime, timedelta
dia=datetime.now(argentina).strftime('%A %d-%m-%Y %H:%M')
dia=dia.replace('Monday','Lunes')
dia=dia.replace('Tuesday','Martes')
dia=dia.replace('Wednesday','Miércoles')
dia=dia.replace('Thursday','Jueves')
dia=dia.replace('Friday','Vierneses')
dia=dia.replace('Saturday','Sábado')
col2.image("https://logisticausal.com.ar/sitio/logiusal22.jpg")
st.markdown('<div style="text-align:center; border-bottom:1px solid #008357;border-top:1px solid #008357;font-family: Oswald">CAMPUS NUESTRA SEÑORA DEL PILAR</div>', unsafe_allow_html=True)
#st.markdown('<div style="text-align:center; font-size:18px;border-bottom:1px solid #008357;font-family: Oswald"><b>REGISTRO DE ASISTENCIA</b></div><br>', unsafe_allow_html=True)
#st.markdown('<div style="text-align:center; font-size:14px;border-bottom:1px solid #008357;font-family: Oswald;color:#e65100"><b>Horario de atención de 7 a 19 hs, las reservas se deben realizar con al menos 48 hs hábiles de antelación y dichas reservas se realizan únicamente online</b></div><br>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-size:24px;border-bottom:1px solid #008357;font-family: Oswald"><b>CONTROL DE ACCESO DOCENTES</b></div><br>', unsafe_allow_html=True)
col122, col222,col322 = st.columns([1,1,1])
import pandas as pd
from decouple import Config, RepositoryEnv
DOTENV_FILE = 'jamis.env'
env_config = Config(RepositoryEnv(DOTENV_FILE))
host = env_config.get('host')
userID = env_config.get('userID')
passwordh = env_config.get('password')
base = env_config.get('base')
api = env_config.get('api')
secret = env_config.get('secret')
from streamlit_folium import folium_static
import folium
import streamlit.components.v1 as components

make_map_responsive = """
  <style>
  [title~="st.iframe"] { width: 100%}
  border: 1px solid rgba(9, 171, 59, 0.2);
  </style>
"""
st.markdown(make_map_responsive, unsafe_allow_html=True)
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import mysql.connector
datos=st.empty()

# Creating connection object
mydb = mysql.connector.connect(
    host=host,
    user=userID,
    password=passwordh,
    database=base
)
c = mydb.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password, ip, coor):
	sql = "INSERT INTO accesos (Dia,DNI, Ip, Lugar) VALUES (%s, %s,%s, %s)"
	val = (username, password,ip, coor)

	c.execute(sql, val)
	mydb.commit()

	#st.write(c.rowcount, "details inserted")

	# disconnecting from server
	mydb.close()

def login_user(password):
	sql="SELECT * FROM datos WHERE nro_doc = %s"

	#c.execute('SELECT * FROM userstable WHERE password = ',(username,password))
	val = (password,)

	c.execute(sql, val)

	data = c.fetchall()
	df = pd.DataFrame(data, columns=['Nombre', 'DNI', 'Numero','Correo','Celular','Facultad'])
	#df = pd.DataFrame(data)
	#df.rename(columns=df.iloc[0]).drop(df.index[0])
	st.session_state.df = df

	#st.write(nombre)
	#st.table(df)
	return data
import requests
g = geocoder.ipinfo('me')
ip = geocoder.ip('me')
location = ip.latlng


map = folium.Map(location=location, zoom_start=10)
folium.CircleMarker(location=location, radius=50, color="red").add_to(map)
folium.Marker(location).add_to(map)

coor=(pd.DataFrame(location))
#st.table(coor)
from geopy.geocoders import Nominatim

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")


# Latitude & Longitude input
Latitude = str(coor.iloc[0, 0])

Longitude = str(coor.iloc[1, 0])

location = geolocator.reverse(Latitude + "," + Longitude)

#st.write(location.address)



sql2 = "SELECT * FROM codigosua"
c.execute(sql2)
data = c.fetchall()
df2 = pd.DataFrame(data, columns=['codigo', 'ua'])
c.execute('SELECT * FROM userstable')
data1 = c.fetchall()
df3 = pd.DataFrame(data1, columns=['Nombre', 'DNI'])
c.execute('SELECT * FROM datos')
data4 = c.fetchall()
df0 = pd.DataFrame(data4, columns=['Nombre', 'DNI', 'Numero', 'Correo', 'Celular', 'Facultad'])

#f0p = pd.merge(df2, st.session_state.df, left_on='codigo', right_on='Facultad')
def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	df = pd.DataFrame(data)
	st.table(df)
	return data



def main():
	"""Simple Login App"""

	col13, col23, col33 = st.columns([1, 2, 1])
	with datos:
		col120, col220, col320 = st.columns([1, 2, 1])

		col220.markdown('<div style="text-align:center; font-size:18px;font-family: Oswald;color:#1f1f1f">INGRESAR DNI PARA REGISTRAR ASISTENCIA</div><br>', unsafe_allow_html=True)
		col220.markdown(
			'<div style="text-align:center; font-size:16px;font-family: Oswald;color:#e65100"><b>' + dia + '</b></div><br>',
			unsafe_allow_html=True)

		form = col220.form(key='my-form')
		#username = form.text_input("Usuario")
		password = form.text_input("Ingresar DNI",type='password')
		submit = form.form_submit_button(label='Validar')










	if submit:

		if password:


			result = login_user(password)
			if result:

				nombre = st.session_state.df.iloc[:, 0]
				nombre = ', '.join(nombre)
				celular = st.session_state.df.iloc[:, 4]
				celular = ', '.join(celular)
				correo= st.session_state.df.iloc[:, 3]
				correo = ', '.join(correo)

				f0p = pd.merge(df2, st.session_state.df, left_on='codigo', right_on='Facultad')
				facu= f0p.iloc[:, 1]
				facu = ', '.join(facu)

				#selected_reward_price = st.session_state.df.loc[st.session_state.df.DNI == password]["Facultad"].iloc[4]

				datos.empty()
				txt = "{}".format(nombre )
				txt2 = "{}".format(password)
				txt22 = "{}".format(correo)
				txt3="{}".format(celular)
				#txt4 = "{}".format(selected_reward_price)
				add_userdata(dia,password,g.ip,location.address)

				htmlstr1 = f"""<p style='background-color:rgba(9, 171, 59, 0.2);;font-family: Oswald; 
														  color:rgb(23, 108, 54);
														  border: 1px solid rgba(9, 171, 59, 0.2);
														  font-size:16px;
														  border-radius:3px;
														  line-height:30px;
														  text-align:center;
														  margin-top:-10px;
														  '>
														  {txt}<br>{txt2}<br>{txt22}<br>{facu}<br><br><b>El día {dia}<br>se registró su asistencia.</b></style>
														  <br></p>"""
				col222.markdown(htmlstr1, unsafe_allow_html=True)
				


			else:
				col23.warning("DNI incorrecto")
		else:
				col23.warning("Ingrese DNI")





	components.html("""<script type="text/javascript">var sc_project=12780404; var sc_invisible=1; var sc_security="b99889ba"; </script><script type="text/javascript" src="https://www.statcounter.com/counter/counter.js" async></script><noscript><div class="statcounter"><a title="Web Analytics" href="https://statcounter.com/" target="_blank"><img class="statcounter" src="https://c.statcounter.com/12780404/0/b99889ba/1/" alt="Web Analytics" referrerPolicy="no-referrer-when-downgrade"></a></div></noscript>""")

	components.html("""<script async src="https://www.googletagmanager.com/gtag/js?id=G-HP3NVL9W85"></script><script>window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'G-HP3NVL9W85');</script>""")

	def inject_ga():
		"""Add this in your streamlit app.py
        see https://github.com/streamlit/streamlit/issues/969
        """
		# new tag method
		GA_ID = "google_analytics"
		# NOTE: you should add id="google_analytics" value in the GA script
		# https://developers.google.com/analytics/devguides/collection/analyticsjs
		GA_JS = """
	<!-- Global site tag (gtag.js) - Google Analytics -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=G-HP3NVL9W85"> id="google_analytics" </script>
	<script>
	  window.dataLayer = window.dataLayer || [];
	  function gtag(){dataLayer.push(arguments);}
	  gtag('js', new Date());

	  gtag('config', 'G-HP3NVL9W85');
	</script>
	"""
		# Insert the script in the head tag of the static template inside your virtual
		index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
		logging.info(f'editing {index_path}')
		soup = BeautifulSoup(index_path.read_text(), features="lxml")
		if not soup.find(id=GA_ID):  # if cannot find tag
			bck_index = index_path.with_suffix('.bck')
			if bck_index.exists():
				shutil.copy(bck_index, index_path)  # recover from backup
			else:
				shutil.copy(index_path, bck_index)  # keep a backup
			html = str(soup)
			new_html = html.replace('<head>', '<head>\n' + GA_JS)
			index_path.write_text(new_html)
if __name__ == '__main__':
	main()
	inject_ga()
