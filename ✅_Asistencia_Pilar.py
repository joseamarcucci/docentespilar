import streamlit as st
st.set_page_config(
page_title="USAL Alta transporte Alumnos",
page_icon="https://webinars.usal.edu.ar/sites/default/files/favicon.ico",
layout="wide"

)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
       .css-rncmk8 {
    text-align: center;
}
.css-12ttj6m {
    border: 1px solid rgba(49, 51, 63, 0.2);
    border-radius: 0.25rem;
    padding: calc(1em - 1px);
    font-family: oswald;
}
.css-uaf2yl {
 
    margin-top: -40px;
}
.css-1c2btq4 {
    
 
    margin-top: -20px;
}
footer {visibility: hidden;}
#header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
col1, col2,col3 = st.columns([1,2,1])
#vivod=df.iat[1,1]
#vivom=df.iat[0,1]
col2.image("https://logisticausal.com.ar/sitio/logiusal22.jpg")
st.markdown('<div style="text-align:center; border-bottom:1px solid #008357;border-top:1px solid #008357;font-family: Oswald">CAMPUS NUESTRA SEÑORA DEL PILAR</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-size:18px;border-bottom:1px solid #008357;font-family: Oswald"><b>REGISTRO DE ASISTENCIA</b></div><br>', unsafe_allow_html=True)
#st.markdown('<div style="text-align:center; font-size:14px;border-bottom:1px solid #008357;font-family: Oswald;color:#e65100"><b>Horario de atención de 7 a 19 hs, las reservas se deben realizar con al menos 48 hs hábiles de antelación y dichas reservas se realizan únicamente online</b></div><br>', unsafe_allow_html=True)
st.write('<style>div.row-widget.stRadio> div{flex-direction:row;}</style>', unsafe_allow_html=True)
col12, col22,col32 = st.columns([1,2,1])
arriba=st.empty()

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

# Security
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


def add_userdata(username,password):
	sql = "INSERT INTO userstable (username,password) VALUES (%s, %s)"
	val = (username, password)

	c.execute(sql, val)
	mydb.commit()

	st.write(c.rowcount, "details inserted")

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




def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""








	with datos:
		col120, col220, col320 = st.columns([1, 2, 1])

		col220.markdown('<div style="text-align:center; font-size:18px;font-family: Oswald;color:#1f1f1f">INGRESAR DNI PARA REGISTRAR ASISTENCIA</div><br>', unsafe_allow_html=True)

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
				facu = st.session_state.df.iloc[:, 5]
				#selected_reward_price = st.session_state.df.loc[st.session_state.df.DNI == password]["Facultad"].iloc[4]

				datos.empty()
				txt = "{}".format(nombre )
				txt2 = "{}".format(password)
				txt22 = "{}".format(correo)
				txt3="{}".format(celular)
				#txt4 = "{}".format(selected_reward_price)

				htmlstr1 = f"""<p style='background-color:rgba(9, 171, 59, 0.2);;font-family: Oswald; 
														  color:rgb(23, 108, 54);
														  border: 1px solid rgba(9, 171, 59, 0.2);
														  font-size:16px;
														  border-radius:3px;
														  line-height:30px;
														  text-align:center;
														  margin-top:-40px;
														  '>
														  {txt}<br>{txt2}<br>{txt22}<br>{txt3}<br><br><b>Se registró su asistencia.</b></style>
														  <br></p>"""
				col222.markdown(htmlstr1, unsafe_allow_html=True)



			else:
				col22.warning("Usuario/Clave incorrecta")
		else:
				col22.warning("Ingrese usuario y Clave")








if __name__ == '__main__':
	main()
