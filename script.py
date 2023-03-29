import configparser
cfg = configparser.ConfigParser()
cfg.read('cfg.ini')

nomeBanco = cfg['DEFAULT']['NomeBanco']
codEntidade = cfg['DEFAULT']['CodEntidade']
nomeEntidade = cfg['DEFAULT']['NomeEntidade']
motorista = cfg['DEFAULT']['Motorista']

scripts = {

'Cor' : f"""  """,

'Marca' : f"""  """,

'Especie' : f""" """,

'Modelo' : f"""  """,

'Motorista' : f"""  """,

'MotoristaCategoriaCnh' : f"""  """,

'MotoristaSituacaoCnh' : f"""  """,

'Veiculo' : f"""  """,

'Abastecimento' : f"""  """,

'Acumulador' : f"""  """

}