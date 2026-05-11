import typer
from rich import print
from engine import call_openrouter

app = typer.Typer(help="Copiloto AI Full Stack - Terminal Edition")

@app.command()
def ask(pergunta: str):
    """Modo ASK: Dúvidas rápidas de código."""
    typer.echo(f"🤖 Consultando...")
    messages = [
        {"role": "system", "content": "Você é um desenvolvedor Sênior. Responda de forma técnica e concisa."},
        {"role": "user", "content": pergunta}
    ]
    res = call_openrouter(messages)
    print(f"\n[bold blue]🤖 Copiloto:[/bold blue]\n{res}")

@app.command()
def plan(planejamento: str):
    """Modo PLAN: Planejamento de arquitetura e tarefas."""
    typer.echo(f"🤖 Elaborando Planejamento...")
    messages = [
        {"role": "system", "content": "Você é um desenvolvedor Sênior. Responda de forma técnica e concisa."},
        {"role": "user", "content": pergunta}
    ]
    res = call_openrouter(messages)
    print(f"\n[bold green]📝 Plano Sugerido:[/bold green]\n{res}")

@app.command()
def agent(executar: str):
    """Modo AGENT: Execução de tarefas de codificação e automação."""
    typer.echo(f"🤖 Aguarde...")
    messages = [
        {"role": "system", "content": "Você é um desenvolvedor Sênior. Responda de forma técnica e concisa."},
        {"role": "user", "content": pergunta}
    ]
    res = call_openrouter(meassages)
    print(f"\n[bold green]📝 Resultado do Agente:[/bold green]\n{res}")

@app.command()
def study(pesquisa: str):
    """Modo STUDY: Pesquisa aprofundada e explicação de conceitos."""
    typer.echo(f"🤖 Pesquisando, aguarde...")
    messages = [
        {"role": "system", "content": "Você é um desenvolvedor Sênior. Responda de forma técnica e concisa."},
        {"role": "user", "content": pergunta}
    ]
    res = call_openrouter(messages)
    print(f"\n[bold green]📝 Material de Estudo:[/bold green]\n{res}")

# Adicione os stubs para agent e study de forma similar...

if __name__ == "__main__":
    app()
