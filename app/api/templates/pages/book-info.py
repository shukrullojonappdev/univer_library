{% extends "index.html" %}
{% load static %}
{% block styles %}
<link rel="stylesheet" type="text/css" href="{% static 'css/book-info.css' %}" />
{% endblock %}
{% block content %}
<div class="container">
  <div class="content">
    <div class="row">
      {% for book in books %}
      <div class="col mb-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ book.name }}</h5>
            <h6 class="card-text">Автор: {{ book.author }}</h6>
            <h6 class="card-text">Кол-стр: 100</h6>
            <h6 class="card-text">Статус: Читаю</h6>
            <a href="#" class="card-link">more...</a>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>
{% endblock %}