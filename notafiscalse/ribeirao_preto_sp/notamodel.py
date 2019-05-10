''' 
   Classes representando dados que compõe a Nota Fiscal de Serviços Eletrônico
   
'''
 

class Prestador():
    
    def __init__(self, cnpj, inscricao_municipal, razao_social, nome_fantasia, logradouro, numero_logradouro, complemento, bairro, cidade, estado, codigo_cidade_ibge, cep, email, telefone, complemento_prestador):
        self.cnpj = cnpj
        self.inscricao_municipal
        self.razaosocial = razaosocial
        self.nome_fantasia = nome_fantasia
        self.logradouro = logradouro
        self.numero_logradouro = numero_logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.codigo_cidade_ibge = codigo_cidade_ibge
        self.cep = cep
        self.email = email
        self.telefone = telefone
        self.complemento_prestador = complemento_prestador

class ComplementoPrestador():
	
    def __init__(self, natureza_operacao, incentivador_cultural, optante_simples_nacional, iss_retido, item_lista_servico, codigo_tributacao_municipio, caminho_certificado, senha_certificado):
        self.natureza_operacao = natureza_operacao 
        self.incentivador_cultural = incentivador_cultural
        self.optante_simples_nacional = optante_simples_nacional
        self.iss_retido = iss_retido
        self.item_lista_servico = item_lista_servico
        self.codigo_tributacao_municipio = codigo_tributacao_municipio
        self.caminho_certificado = caminho_certificado
        self.senha_certificado = senha_certificado


class Tomador():

    def __init__(self, cpf_cnpj, nome, logradouro, numero_logradouro, complemento, bairro, cidade, estado, cep, codigo_cidade_ibge, email, telefone):
       self.cpf_cnpj = cpf_cnpj
       self.nome = nome
       self.logradouro = logradouro
       self.numero_logradouro = numero_logradouro
       self.complemento = complemento
       self.bairro = bairro 
       self.cidade = cidade
       self.estado = estado
       self.cep = cep
       self.codigo_cidade_ibge = codigo_cidade_ibge,
       self.email = email
       self.telefone = self.telefone

class ReciboNotaFiscal():
    def __init__(self, status_rps, quantidade_rps, numero_rps, serie_rps, tipo_rps, data_emissao_rps, situacao_lote_rps):
        self.status_rps = status_rps
        self.quantidade_rps = quantidade_rps
        self.numero_rps = numero_rps
        self.serie_rps = serie_rps
        self.tipo_rps = tipo_rps
        self.data_emissao_rps = data_emissao_rps
        self.situacao_lote_rps = situacao_lote_rps 

class ItemNotaFiscal():
    def __init__(self, valor_servico, valor_iss_retido, aliquota, valor_deducoes, valor_pis, valor_cofins, valor_inss, valor_ir, valor_csll, outras_retencoes, base_calculo, valor_liquido, desconto_incondicionado, desconto_condicionado,	valor_iss):
        self.valor_servico = valor_servico
        self.valor_iss_retido = valor_iss_retido
        self.aliquota = aliquota 
        self.valor_deducoes = valor_deducoes
        self.valor_pis = valor_pis
        self.valor_cofins = valor_cofins
        self.valor_inss = valor_inss
        self.valor_ir = valor_ir
        self.valor_csll = valor_csll
        self.outras_retencoes = outras_retencoes
        self.base_calculo = base_calculo
        self.valor_liquido = valor_liquido
        self.desconto_incondicionado = desconto_incondicionado
        self.desconto_condicionado = desconto_condicionado
        self.valor_iss = valor_inss

class NotaFiscal():
    def __init__(self, numero_nfse, data_emissao_nfse, codigo_verificacao, numero_lote, numero_protocolo,competencia, discriminacao, outras_informacoes, recibo_nota_fiscal, prestador, tomador):
        self.numero_nfse = numero_nfse
        self.data_emissao_nfse = data_emissao_nfse
        self.codigo_verificacao = codigo_verificacao
        self.numero_lote = numero_lote
        self.numero_protocolo = numero_protocolo
        self.competencia = competencia
        self.discriminacao = discriminacao
        self.outras_informacoes = outras_informacoes
        self.recibo_nota_fiscal = recibo_nota_fiscal
        self.prestador = prestador
        self.tomador = tomador


