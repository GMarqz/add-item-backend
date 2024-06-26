from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/inicio')
def ola():
    legends = [
        {
            "first": "Add Item",
            "second": "Set the new item's stats",
            "critStat":"Crit value",
            "spdValue": "Speed Value",
            "third": "Item's description"
        }
    ]

    input_name_type = [
        {
            "type": "text",
            "id": "name",
            "name": "name",
            "placeholder": "Item's name"
        },
        {
            "type": "text",
            "id": "type",
            "name": "type",
            "placeholder": "Item's type"
        }
    ]

    second_input = [
        {
            "type": "number",
            "id": "atk",
            "name": "atk",
            "value": "0"   
        },
        {
            "type": "number",
            "id": "def",
            "name": "def",
            "value": "0"
        },
        {
            "type": "number",
            "id": "hp",
            "name": "hp",
            "value": "0"
        },
        {
            "type": "number",
            "id": "str",
            "name": "str",
            "value": "0"
        },
        {
            "type": "number",
            "id": "int",
            "name": "int",
            "value": "0"
        },
        {
            "type": "number",
            "id": "agi",
            "name": "agi",
            "value": "0"
        }
    ]

    crit_input = [
        {
            "type": "number",
            "id": "rate",
            "name": "rate",
            "value": "0" 
        },
        {
            "type": "number",
            "id": "dmg",
            "name": "dmg",
            "value": "0"
        }
    ]

    speed_input = [
        {
            "type": "number",
            "id": "atks",
            "name": "atk",
            "value": "0"
        },
        {
            "type": "number",
            "id": "mvt",
            "name": "mvt",
            "value": "0"
        }
    ]

    creator_price = [
        {
            "type": "text",
            "id": "creator",
            "name": "creator",
            "placeholder": "Creator"
        },
        {
            "type": "text",
            "id": "price",
            "name": "price",
            "placeholder": "Price"
        }
    ]

    return render_template('index.html', legends=legends, inputs=input_name_type, secondInput=second_input, critInput=crit_input, spdInput=speed_input, cpi=creator_price)

@app.route('/login',)
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'admin' == request.form['senha']:
        return redirect('/')
    else:
        return redirect('/login')

app.run()