
# Importar la Flask
from flask import Flask, render_template, jsonify

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

# Congigurar la ruta del gráfico tipo chartjs
@app_flask.route('/graficoschartjs')
def ir_a_graficoschartjs():    
    return render_template('_graficos_chartjs.html')

# Congigurar la ruta de los datos del gráfico tipo chartjs
@app_flask.route('/data')
def ir_a_data():
    # https://cifras.biodiversidad.co/boyaca
    datos = {
        'titulo': 'Especies Endémicas observadas en Boyacá',
        'maximo': '',
        'especies': ['Ortalis columbiana', 'Synallaxis subpudica', 'Espeletia cleefii', 'Espeletia boyacensis', 'Crax alberti', 'Cistothorus apolinari', 'Bucquetia glutinosa', 'Pristimantis lynchi', 'Paepalanthus alpinus', 'Habia gutturalis'],
        'observaciones': [1767, 1734, 1154, 904, 899, 892, 748, 739, 631, 609] 
    }
    
    return jsonify(datos)


# Levantar la Aplicación WEB para verla en el navegador
# debug=True Indica es que estamos en periodo de depuración
if __name__ == '__main__':
    app_flask.run(debug=True, port=5000)
