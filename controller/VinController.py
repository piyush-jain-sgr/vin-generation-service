from flask import Flask, render_template, request
from service.VinService import VinService

app = Flask(__name__,template_folder="C:/Users/31817/PycharmProjects/Handson1/templates")
vinService = VinService()

@app.route('/')
@app.route('/home')
def home():
    return render_template("homepage.html")

@app.route('/getVIN', methods=['POST', 'GET'])
def getVIN():
    requestParameters=request.form.to_dict()
    inputNumber=int((requestParameters['inputNumber']))
    vinNumbers=vinService.generateVin(inputNumber)
    return render_template('vin.html', vinNumbers=vinNumbers)

@app.route('/validateVIN', methods=['POST', 'GET'])
def validateVIN():
    requestParameters = request.form.to_dict()
    inputVIN = (requestParameters['vinNumber'])
    isvalidvin = vinService.validateVIN(inputVIN)
    return render_template('validate.html', isvalidvin=isvalidvin)

if __name__ == "__main__":
    app.run(debug=True)