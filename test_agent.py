from kaggle_environments import make
from submission import agent

# Cria o ambiente
print("Iniciando ambiente Kaggriculture...")
env = make("kaggriculture", debug=True)
print(f"Environment: {env.name} v{env.version}")
print(f"Players: {env.specification.agents}")
print(f"Max steps: {env.configuration.episodeSteps}")

# Roda um jogo de teste (seu agente contra um agente aleatório)
print("\nRodando simulação...")
env.run([agent, "random"])

# Mostra o resultado final
final = env.steps[-1]
print("\n--- Resultados ---")
for i, s in enumerate(final):
    print(f"Player {i}: reward={s.reward}, status={s.status}")

# Mostra a observação do final
print("\nFim do jogo!")
