from flask import Flask, render_template, redirect, request
from database import init_db, db
from models import Usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Noah1310@127.0.0.1/postgres'



# Rota da página inicial
@app.route('/', methods=['GET', 'POST'])
def index():
        
    return render_template('index.html')

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
           
    return render_template('cadastro_vacina_paciente.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
            
    return render_template('cadastro.html')

@app.route('/recuperar_senha', methods=['GET', 'POST'])
def recuperar_senha():
            
    return render_template('recuperar_senha.html')

# Rota para rodar o app
if __name__ == '__main__':
    app.run()
