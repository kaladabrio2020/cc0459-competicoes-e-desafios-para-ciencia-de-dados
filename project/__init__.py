import webbrowser
from kaggle_environments import make

def run_random(show:bool=True)-> None:
    env = make("kaggriculture", debug=False)
    env.run(['random', 'random'])
    if show:
        html_content = env.render(mode="html", width=800, height=600)
        output_path = "resultado.html"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"Visualização salva em {output_path}. Abrindo no navegador...")
        webbrowser.open(output_path)

def main() -> None:
    print("Hello from fazendinha!")
    run_random()

if __name__ == "__main__":
    main()
    