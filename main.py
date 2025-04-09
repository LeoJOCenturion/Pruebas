from flask oimport Flask. jsonnify 
app = Flash(__name__)

Dni = [
    {dni:71865107,nombre:'Leonardo'}
    {dni:00451289,nombre:'Ana'} 
    ]

@app.route('/')
def homre()
return "API EN PYHTON LISTA"

@app.route('/Dni')
methods=['GET']
def get_dnis():
    return jsonnify(Dni)
if __name__=='__main__':
    app.run(debug=true)