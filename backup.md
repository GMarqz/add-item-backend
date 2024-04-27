```py
{% extends "template.html" %}
{% block content %}
    <form action="#" method="post" class="form">
        <fieldset class="first__container">
            <div class="first__container__add__item">
                <legend class="first__container__add__item__legend">{{ legends[0]['first'] }}</legend>
            </div>
            <div class="first__container__add__item__input">
                {% for input in inputs %}
                <label for="{{ input.id }}">{{ input.placeholder }}</label>
                <input type="{{ input.type }}" id="{{ input.id }}" name="{{ input.name }}" placeholder="{{ input.placeholder }}" required />
                {% endfor %}
            </div>
        </fieldset>
        <fieldset class="second__container">
            <div class="second__container__set__stats">
                <legend class="second__container__set__stats__legend">{{ legends[0]['second'] }}</legend>
            </div>
            <div class="second__container__set__stats__input">
                {% for secondInput in secondInputs %}
                <p>{{ secondInput }}</p> <!-- Adicionando isso para depuração -->
                <label for="{{ secondInput.id }}">{{ secondInput.name.upper() }}</label>
                <input type="{{ secondInput.type }}" id="{{ secondInput.id }}" name="{{ secondInput.name }}" value="{{ secondInput.value }}" required />
                {% endfor %}
            </div>
            <div class="second__container__set__crit__value__input">
                <legend class="second__container__set__crit__value__legend">{{ legends[0]['critStat'] }}</legend>
                {% for input in critInput %}
                <label for="{{ critInput.id }}">{{ critInput.name.upper() }}</label>
                <input type="{{ critInput.type }}" id="{{ critInput.id }}" name="{{ critInput.name }}" value="{{ critInput.value }}" required />
                {% endfor %}
            </div>
        </fieldset>
    </form>
{% endblock %}
```