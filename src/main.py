#  Coloque aqui a importação do seu agente
from dummy import dummy as agent

# Este trecho abaixo é apenas para teste local, não é executado no kaggle
if __name__ == "__main__":
    import webbrowser
    from kaggle_environments import make

    OPPONENT = "random"  # Opções: "random", "pass", "starter"
    EPISODE_STEPS = 720  # Temporada completa (24 turnos x 30 dias)
    SAVE_HTML = True     # Se True, gera e abre o replay visual no navegador

    print(f"Iniciando simulação de teste local: Agente vs {OPPONENT} ({EPISODE_STEPS} turnos)...")
    env = make("kaggriculture", configuration={"episodeSteps": EPISODE_STEPS}, debug=True)
    env.run([agent, OPPONENT])

    p0, p1 = env.steps[-1]
    saldo_p0 = p0.reward if p0.reward is not None else 0.0
    saldo_p1 = p1.reward if p1.reward is not None else 0.0

    print("-" * 50)
    print("RESULTADO DO TESTE LOCAL")
    print("-" * 50)
    print(f"Player 0 (Seu Agente) : Saldo = ${saldo_p0:,.2f} | Status = {p0.status}")
    print(f"Player 1 ({OPPONENT:<11}) : Saldo = ${saldo_p1:,.2f} | Status = {p1.status}")

    if p0.status == "ERROR":
        print(f"\n[ERRO] Seu agente quebrou! Verifique logs/traceback acima.")
    elif saldo_p0 > saldo_p1:
        print("\nVitória do seu agente!")
    elif saldo_p0 < saldo_p1:
        print(f"\nDerrota contra {OPPONENT}.")
    else:
        print("\nEmpate!")
    print("-" * 50)

    if SAVE_HTML:
        output_html = "resultado.html"
        with open(output_html, "w", encoding="utf-8") as f:
            f.write(env.render(mode="html", width=1000, height=750))
        print(f"Replay salvo em '{output_html}'. Abrindo no navegador...")
        webbrowser.open(output_html)
