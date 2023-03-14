import json

# Carrega o arquivo JSON
with open('data/dados.json') as json_file:
    data = json.load(json_file)

# Criação do formulário HTML
html = "<form>"
for atributo in data["atributos"]:
    html += f'<label>{atributo["nome"]}: </label>'
    html += f'<input type="{atributo["tipo"]}" name="{atributo["nome"]}" '
    if atributo["opcional"]:
        html += 'optional'
    html += '><br>'

html += '<input type="submit" value="Enviar"></form>'

# Criação do código SQL para criação da tabela
tabela_sql = f'CREATE TABLE entidade (\n'
for atributo in data["atributos"]:
    tabela_sql += f'{atributo["nome"]} {atributo["tipo"]}'
    if not atributo["opcional"]:
        tabela_sql += ' NOT NULL'
    tabela_sql += ',\n'
tabela_sql += ');'

# Salva o formulário HTML em um arquivo
with open('formulario.html', 'w') as file:
    file.write(html)

# Salva o código SQL em um arquivo
with open('tabela.sql', 'w') as file:
    file.write(tabela_sql)