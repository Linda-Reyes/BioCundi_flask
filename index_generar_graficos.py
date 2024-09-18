#importar las libreria necesarias
from flask import Flask, render_template
import io
import pandas
import matplotlib.pyplot as plt

# Objeto Flask para controlar la aplicación
app_flask = Flask(__name__)

# Rutas del sitio WEB
@app_flask.route('/')
def ir_a_datos():
    ejex = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ejey = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #df = pandas.read_csv('datos.csv')    
    #print(df)

    #plotting :: trazado
    plt.plot(ejex, ejey)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Gráfico de ")

    url1 = 'images/grafico1.png'
    plt.savefig('static/' + url1)
    #plt.savefig('static/images/grafico1.png')
    plt.close()

    df = pandas.DataFrame({
        'nombre':['José', 'Maria', 'Pedro', 'Jeff', 'Manuel', 'Lisa', 'Antonio'],
        'edad': [23,78,22,19,45,33,20],
        'genero':['M','F','M','M','M', 'F','M'],
        'provincia': ['Madrid', 'Barcelona', 'Málaga', 'Giron', 'París', 'Milan', 'Roma'],
        'num_hijos': [2,0,0,3,2,1,4],
        'num_mascotas':[5,1,0,5,2,2,3]
    })
    # figsize :: parametro de matplotlib en pulgadas (ancho)6,4 y (alto)4,8
    df.plot(figsize=(10,8), title='Gráfico de Barras no apiladas', kind='bar', stacked=False)
    url2 = 'images/grafico2.png'
    plt.savefig('static/' + url2, format='png')
    plt.close()
    
    return render_template('datos_graficos.html', elejex=ejex, elejey=ejey, nombre="Gráfico 1", url1=url1, nombre2='Gráfico 2', url2=url2 )

@app_flask.route('/flora')
def ir_a_flora():
    lista_flora = ["Espeletia argentea", "Puya santosii", "Ceroxylon quindiuense", "Cyathea caracasana", "Lupinus bogotensis", "Aequatorium dodsonii", "Draba boyacensis", "Salvia muisca", "Epidendrum cundinamarcae", "Polylepis sericea"]
    return render_template('_flora.html', lista_flora=lista_flora)

# Configurar la ruta del proyecto para la pagina de 
@app_flask.route('/fauna')
def ir_a_fauna():
    #return 'Bienvenido a la pagina WEB Principal hecha con Flask'    
    lista_fauna = ["Nymphargus ruizi", "Anadia bogotensis", "Coeligena orina", "Hapalopsittaca fuertesi fuertesi", "Thomasomys bombycinus", "Leopardus tigrinus pardinoides", "Atelopus muisca", "Merganetta armata columbiana", "Marmosa robinsoni colombiana", "Phalcoboenus carunculatus"]
    return render_template('_fauna.html', lista_fauna=lista_fauna)
# -----------------------------------------------------------------


if __name__ == '__main__':
    app_flask.run(debug=True, port=5000)
