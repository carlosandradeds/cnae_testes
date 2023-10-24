from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

conhecimentos = {
    "conhecimentos": {
        "CF12345": {
            "origem": "São Paulo, SP",
            "destino": "Rio de Janeiro, RJ",
            "data_emissao": "2023-10-24",
            "remetente": "Empresa A",
            "destinatario": "Empresa B",
            "produto": "Eletrônicos",
            "peso": "500 kg",
            "valor_carga": "$10,000.00",
            "status": "Em trânsito",
            "rota": ["São Paulo, SP -> Belo Horizonte, MG -> Rio de Janeiro, RJ"],
            "previsao_entrega": "2023-11-02",
            "notas_fiscais": [
                {
                    "numero_nota_fiscal": "NF001",
                    "cnpj_emitente": "07.047.183/0001-40",
                    "cnpj_destinatario": "98.765.432/0001-02",
                    "data_emissao": "2023-10-24",
                    "itens": [
                        {
                            "descricao_produto": "Smartphones",
                            "quantidade": 50,
                            "valor_unitario": "$100.00",
                            "valor_total": "$5,000.00",
                            "ncm": "85171300"
                        },
                        {
                            "descricao_produto": "Tablets",
                            "quantidade": 50,
                            "valor_unitario": "$100.00",
                            "valor_total": "$5,000.00",
                            "ncm": "85171300"
                        }
                    ],
                    "valor_total_nota": "$10,000.00"
                },
                {
                    "numero_nota_fiscal": "NF002",
                    "cnpj_emitente": "23.456.789/0001-03",
                    "cnpj_destinatario": "87.654.321/0001-04",
                    "data_emissao": "2023-10-24",
                    "itens": [
                        {
                            "descricao_produto": "Acessórios Eletrônicos",
                            "quantidade": 100,
                            "valor_unitario": "$30.00",
                            "valor_total": "$3,000.00"
                        }
                    ],
                    "valor_total_nota": "$3,000.00"
                }
            ]
        },
        "CF67890": {
            "origem": "Belo Horizonte, MG",
            "destino": "Curitiba, PR",
            "data_emissao": "2023-10-25",
            "remetente": "Empresa C",
            "destinatario": "Empresa D",
            "produto": "Produtos Químicos",
            "peso": "800 kg",
            "valor_carga": "$15,000.00",
            "status": "Aguardando coleta",
            "rota": ["Belo Horizonte, MG -> São Paulo, SP -> Curitiba, PR"],
            "previsao_entrega": "2023-11-05",
            "notas_fiscais": [
                {
                    "numero_nota_fiscal": "NF003",
                    "cnpj_emitente": "34.567.890/0001-05",
                    "cnpj_destinatario": "76.543.210/0001-06",
                    "data_emissao": "2023-10-25",
                    "itens": [
                        {
                            "descricao_produto": "Produtos Químicos",
                            "quantidade": 40,
                            "valor_unitario": "$375.00",
                            "valor_total": "$15,000.00"
                        }
                    ],
                    "valor_total_nota": "$15,000.00"
                }
            ]
        },
        "CF54321": {
            "origem": "Recife, PE",
            "destino": "Salvador, BA",
            "data_emissao": "2023-10-26",
            "remetente": "Empresa E",
            "destinatario": "Empresa F",
            "produto": "Alimentos Perecíveis",
            "peso": "300 kg",
            "valor_carga": "$7,500.00",
            "status": "Entregue",
            "rota": ["Recife, PE -> Maceió, AL -> Salvador, BA"],
            "data_entrega": "2023-11-01",
            "notas_fiscais": [
                {
                    "numero_nota_fiscal": "NF004",
                    "cnpj_emitente": "45.678.901/0001-07",
                    "cnpj_destinatario": "65.432.109/0001-08",
                    "data_emissao": "2023-10-26",
                    "itens": [
                        {
                            "descricao_produto": "Alimentos Perecíveis",
                            "quantidade": 50,
                            "valor_unitario": "$150.00",
                            "valor_total": "$7,500.00"
                        }
                    ],
                    "valor_total_nota": "$7,500.00"
                }
            ]
        }
    }
}

class NumeroFrete(BaseModel):
    numero_conhecimento: str

@app.get("/conhecimentos_de_frete/")
def get_conhecimento_de_frete(numero_conhecimento: NumeroFrete):
    if numero_conhecimento.numero_conhecimento in conhecimentos["conhecimentos"]:
        return conhecimentos["conhecimentos"][numero_conhecimento.numero_conhecimento]
    return {"message": "Conhecimento de frete não encontrado"}