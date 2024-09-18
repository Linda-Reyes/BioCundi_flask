
# Importar la Flask
from flask import Flask, render_template

# Objeto Flask para controlar la aplicación
app_flask = Flask(__name__)

# Configurar las rutas del sitio web
# Congigurar la ruta raiz del sitio para el home
@app_flask.route('/')
def ir_a_principal():
    # return 'Bienvenido a la Página WEB Principal hecha en Flask con Python'
    return render_template('_index.html')

# Congigurar la ruta de los flora 
@app_flask.route('/flora')
def ir_a_flora():
    #return 'Página de Flora con Flask'
    lista_flora = ["Espeletia argentea", "Puya santosii", "Ceroxylon quindiuense", "Cyathea caracasana", "Lupinus bogotensis", "Aequatorium dodsonii", "Draba boyacensis", "Salvia muisca", "Epidendrum cundinamarcae", "Polylepis sericea"]
    return render_template('_flora.html', lista=lista_flora)

# Congigurar la ruta de los fauna
@app_flask.route('/fauna')
def ir_a_fauna():
    #return 'Página de fauna con Flask'
    lista_fauna = ["Nymphargus ruizi", "Anadia bogotensis", "Coeligena orina", "Hapalopsittaca fuertesi fuertesi", "Thomasomys bombycinus", "Leopardus tigrinus pardinoides", "Atelopus muisca", "Merganetta armata columbiana", "Marmosa robinsoni colombiana", "Phalcoboenus carunculatus"]
    return render_template('_fauna.html', lista=lista_fauna)

@app_flask.route('/parques')
def ir_a_parques():
    #return 'Página parques con Flask'    
    lista_parques = ["Parque Nacional Natural Chingaza", "Parque Nacional Natural Sumapaz", "Parque Nacional Natural Serranía de los Yariguíes", "Santuario de Fauna y Flora Iguaque", "Parque Nacional Natural El Cocuy", "Parque Nacional Natural Pisba", "Parque Natural Chicaque", "Parque Natural Los Tunos", "Parque Natural Siete Chorros", "Santuario de Flora y Fauna de Guanentá Alto Río Fonce"]
    return render_template('_parques.html', lista_parques=lista_parques)


# Levantar la Aplicación WEB para verla en el navegador
# debug=True Indica es que estamos en periodo de depuración
if __name__ == '__main__':
    app_flask.run(debug=True, port=5000)
