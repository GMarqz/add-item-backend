from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    legends = [
        {
            "first": "Add Item",
            "second": "Set the new item's stats",
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
            "type": "text",
            "id": "atk",
            "name": "atk",
            "placeholder": "ATK"   
        },
        {
            "type": "text",
            "id": "def",
            "name": "def",
            "placeholder": "DEF"
        },
        {
            "type": "text",
            "id": "hp",
            "name": "hp",
            "placeholder": "HP"
        },
        {
            "type": "text",
            "id": "str",
            "name": "str",
            "placeholder": "STR"
        },
        {
            "type": "text",
            "id": "int",
            "name": "int",
            "placeholder": "INT"
        },
        {
            "type": "text",
            "id": "agi",
            "name": "agi",
            "placeholder": "AGI"
        }
    ]

    return render_template('index.html', legends=legends, inputs=input_name_type, secondInput=second_input)

app.run()