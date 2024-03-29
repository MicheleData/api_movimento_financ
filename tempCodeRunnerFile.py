import pandas as pd
from flask import Flask
from flask import jsonify


    

tabela = pd.read_excel("Base Financeiro.xlsx")
    

app = Flask(__name__) # Cria o site

@app.route('/')
def movimento():
  dic_movimento = tabela.to_dict()
  return jsonify(dic_movimento)

@app.route('/movimento/banco/<banco>') # Decorater -> Diz em qual link a função vai rodar
def movimento_banco(banco):
  tabela_banco = tabela[['Banco', 'Valor da Movimentação']].groupby('Banco').sum()
  if banco in tabela_banco.index:
    valor_banco = tabela_banco.loc[banco]
    dic_banco = valor_banco.to_dict()
  return jsonify({banco: dic_banco})

@app.route('/movimento/tipo/<tipo>') # Decorater -> Diz em qual link a função vai rodar
def movimento_tipo(tipo):
  tabela_tipo = tabela[['Tipo', 'Valor da Movimentação']].groupby('Tipo').sum()
  if tipo in tabela_tipo.index:
    valor_tipo = tabela_tipo.loc[tipo]
    dic_tipo = valor_tipo.to_dict()
  return jsonify({tipo: dic_tipo})


if __name__ == '__main__':
    app.run()