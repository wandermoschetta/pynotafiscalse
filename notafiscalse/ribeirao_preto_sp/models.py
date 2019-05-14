''' 
   Classes representando dados que compõe a Nota Fiscal de Serviços Eletrônico

'''
 

class Prestador:
    '''
      Classe Prestador representando a empresa que emite a nota fiscal.
    '''
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

class ComplementoPrestador:
	
    def __init__(self, natureza_operacao, incentivador_cultural, optante_simples_nacional, iss_retido, item_lista_servico, codigo_tributacao_municipio, caminho_certificado, senha_certificado):
        self.natureza_operacao = natureza_operacao 
        self.incentivador_cultural = incentivador_cultural
        self.optante_simples_nacional = optante_simples_nacional
        self.iss_retido = iss_retido
        self.item_lista_servico = item_lista_servico
        self.codigo_tributacao_municipio = codigo_tributacao_municipio
        self.caminho_certificado = caminho_certificado
        self.senha_certificado = senha_certificado


class Tomador:
    '''
      Classe Tomador representando o cliente que está consumindo o serviço(s).
      
    '''

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

class ReciboNotaFiscal:
    '''
    Recibo Provisório de Serviço(RPS)
    
    status_rps : Código de status do RPS(1 – Normal, 2 – Cancelado).
    quantidade_rps : Quantidade de RPS do Lote.
    numero_rps : Número do RPS.
    numero_lote : Número do Lote de RPS.
    numero_protocolo : Número do protocolo de recebimento do RPS.
    serie_rps :  Número de série do RPS.
    tipo_rps : Código de tipo de RPS(1 - RPS,2 – Nota Fiscal Conjugada (Mista),3 – Cupom).
    data_emissao_rps : Data Emissão do RPS(AAAA-MM-DD), campo obrigatório apenas para NFS-e geradas pela emissão de RPS.      
	situacao_lote_rps : Código de situação de lote de RPS(1 – Não Recebido,2 – Não Processado,3 – Processado com Erro,4 – Processado com Sucesso). 
    '''
    def __init__(self, status_rps, quantidade_rps, numero_rps, numero_lote, numero_protocolo, serie_rps, tipo_rps, data_emissao_rps, situacao_lote_rps):
        self.status_rps = status_rps
        self.quantidade_rps = quantidade_rps
        self.numero_rps = numero_rps
        self.numero_lote = numero_lote
        self.numero_protocolo = numero_protocolo
        self.serie_rps = serie_rps
        self.tipo_rps = tipo_rps
        self.data_emissao_rps = data_emissao_rps
        self.situacao_lote_rps = situacao_lote_rps 

class ItemNotaFiscal:
    '''
      Valores e tributos que compõe a nota fiscal de serviços eletrônica.
    '''
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

class NotaFiscal:
    '''
	Campos de dados que compõe parte principal da nota fiscal de serviços eletrônica.

    numero_nfse : Número da Nota Fiscal de Serviço Eletrônica,
                  formado pelo ano com 04 (quatro) dígitos e um
                  número seqüencial com 11 posições – Formato AAAANNNNNNNNNNN.
    data_emissao_nfse : Data de Emissão da Nota Fiscal.
    codigo_verificacao : Código de verificação do número da nota gerado enviado automático. 
    competencia : Mês e ano da prestação de serviço. (AAAAMM).
    discriminacao : Discriminação do conteúdo da NFS-e.
    outras_informacoes : Informações adicionais ao documento.
    recibo_nota_fiscal : Classe referenciando Recibo da Nota Fiscal. 
    prestador : Classe referenciando o Prestador de serviços/Empresa.
    tomador : Classe referenciando o Tomador de serviços/Cliente.    
    '''
    def __init__(self, numero_nfse, data_emissao_nfse, codigo_verificacao, competencia, discriminacao, outras_informacoes, recibo_nota_fiscal, prestador, tomador):
        self.numero_nfse = numero_nfse
        self.data_emissao_nfse = data_emissao_nfse
        self.codigo_verificacao = codigo_verificacao
        self.competencia = competencia
        self.discriminacao = discriminacao
        self.outras_informacoes = outras_informacoes
        self.recibo_nota_fiscal = recibo_nota_fiscal
        self.prestador = prestador
        self.tomador = tomador

class MensagemRps:
    '''
      Mensagem de retorno de erros/avisos gerado no envio do recibo provisório da nota fiscal

      codigo : codigo correspondendo erro ou mensagem de retorno
      descricao : descrição da resposta do envio do recibo provisório
    '''
    def __init__(self,codigo, descricao, recibo_nota_fiscal):
        self.codigo = codigo
        self.descricao = descricao
        self.recibo_nota_fiscal = recibo_nota_fiscal
