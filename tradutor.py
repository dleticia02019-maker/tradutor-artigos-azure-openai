import os
from openai import AzureOpenAI

# 🔐 Variáveis de ambiente
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_ENDPOINT
)

def traduzir_artigo(texto, idioma_destino="Português"):
    
    prompt = f"""
    Você é um tradutor técnico especializado.
    Traduza o texto abaixo para {idioma_destino}.
    Preserve termos técnicos importantes.
    Mantenha clareza e coesão.
    """

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "Você é um especialista em tradução técnica."},
            {"role": "user", "content": texto}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    texto_exemplo = """
    Artificial Intelligence is transforming cloud computing 
    by enabling scalable machine learning solutions.
    """

    traducao = traduzir_artigo(texto_exemplo)
    print(traducao)
