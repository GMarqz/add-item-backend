from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    legends = [
        {
            "first": "Add Item",
            "second": "Set the new item's stats",
            "critStat":"Crit value",
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
    ],

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

    return render_template('index.html', legends=legends, inputs=input_name_type, secondInput=second_input, critInput=crit_input)

app.run()