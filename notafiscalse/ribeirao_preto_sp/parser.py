"""
  Módulo responsável pelo tratamento dos dados para XML
"""

class SetupXml:
  """
    Classe responsável pelo tratamento dos dados para XML
  """
  def cabecalho_envia_lote_rps(self):
    return '<ns2:cabecalho versao="3" xmlns:ns2="http://www.ginfes.com.br/cabecalho_v03.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><versaoDados>3</versaoDados></ns2:cabecalho>'
              
  def envelope_envia_lote_rps(self):
    return '{}'.format(self.cabecalho_envia_lote_rps())

  def __repl__(self):
    return 'setupxml: {}'.format(self.envelope_envia_lote_rps())