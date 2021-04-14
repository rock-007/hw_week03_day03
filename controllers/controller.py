from app import app
from flask import render_template
from flask import request
from model.simple_calculator import calculator_01


# Solution_01
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculator/', methods=['GET'])
    
def calc():
    
    if request.method == 'GET':
        arg_1 = int(request.args.get('number_1'))
        arg_2 = int(request.args.get('number_2'))
        arg_3 = request.args.get('Enter-Operator')
        result=0
    
    # query_string= "?arg1={0}&arg2={1}&arg3={2}".format(arg1, arg2, arg3)
    if arg_3 == "+" :
        result= calculator_01.add_two_numbers(arg_1,arg_2)
    elif arg_3 == "-" :
        result= calculator_01.subtract_two_numbers(arg_1,arg_2)
    elif arg_3 == "*" :
        result= calculator_01.multiply_two_numbers(arg_1,arg_2)
    elif arg_3 == "/" :
        result= calculator_01.divide_two_numbers(arg_1,arg_2)

    return render_template("result.html",arg_1= arg_1, arg_2= arg_2, arg_3=arg_3, result = result)

# Solution_02

@app.route('/add/<number_01>/<number_02>')
def addCalc(number_01,number_02):
    result1= calculator_01.add_two_numbers(int(number_01),int(number_02))


    return render_template("result.html",number_01= number_01, number_02= number_02, operator="add", result1 = result1)

@app.route('/subtract/<number_01>/<number_02>')
def subCalc(number_01,number_02):
    result1= calculator_01.subtract_two_numbers(int(number_01),int(number_02))


    return render_template("result.html",number_01= number_01, number_02= number_02, operator="add", result1 = result1)

@app.route('/multiply/<number_01>/<number_02>')
def mulCalc(number_01,number_02):
    result1= calculator_01.multiply_two_numbers(int(number_01),int(number_02))


    return render_template("result.html",number_01= number_01, number_02= number_02, operator="add", result1 = result1)  

@app.route('/divide/<number_01>/<number_02>')
def divCalc(number_01,number_02):
    result1= calculator_01.divide_two_numbers(int(number_01),int(number_02))


    return render_template("result.html",number_01= number_01, number_02= number_02, operator="add", result1 = result1)  

