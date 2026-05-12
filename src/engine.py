import os
import streamlit as st
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
 
MODEL_ID="llama-3.3-70b-versatile"
# Carregamento de ambiente
base_path = Path(__file__).resolve().parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)

try:
  api_key = st.secrets("GROQ_API_KEY") 
except: 
  api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key,
)

def call_openrouter(messages):
    """
    Agora recebe uma lista de dicionários contendo o histórico:
    [{'role': 'system', 'content': '...'}, {'role': 'user', 'content': '...'}]
    """
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:3000",
                "X-Title": "Copilot-Fullstack-Dev",
            },
            # Mantendo o modelo que você validou como funcional
            model="llama-3.3-70b-versatile", 
            messages=messages,
            timeout=30.0,
            stream=True 
        )
        for chunk in completion:
          if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
            
        #return completion.choices[0].message.content
    except Exception as e:
        yield f"Detalhe do Erro: {str(e)}"
