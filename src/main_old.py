# src/main.py

# Importa a função que contém a lógica do seu agente
from agente1 import meu_agente as agent

if __name__ == "__main__":
    import webbrowser
    from kaggle_environments import make

    OPPONENT = "random"  # Adversário de teste: "random", "pass" ou "starter"
    EPISODE_STEPS = 720  # Duração da simulação em turnos
    SAVE_HTML = True     # Gera replay visual no navegador

    print(f"Iniciando teste local contra '{OPPONENT}' ({EPISODE_STEPS} turnos)...")
    env = make("kaggriculture", configuration={"episodeSteps": EPISODE_STEPS}, debug=True)
    env.run([agent, OPPONENT])

    p0, p1 = env.steps[-1]
    print("-" * 45)
    print(f"Seu Agente (P0): ${p0.reward:,.2f} | Status: {p0.status}")
    print(f"Adversário (P1): ${p1.reward:,.2f} | Status: {p1.status}")
    print("-" * 45)

    if SAVE_HTML:
        with open("resultado.html", "w", encoding="utf-8") as f:
            f.write(env.render(mode="html", width=1000, height=750))
        webbrowser.open("resultado.html")

