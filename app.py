import os


def run_app():
    llm_mapping = {
        'groq': {category: os.listdir(f'groq/{category}') for category in os.listdir('groq')},
        'ollama': {category: os.listdir(f'ollama/{category}') for category in os.listdir('ollama')},
    }

    llm = input("Pick an LLM (groq or ollama): ")
    categories = llm_mapping.get(llm)
    if categories is None:
        print(f"No LLM found with the name {llm}")
        return

    category = input("Pick a category (assistant, ai, task, workspace): ")
    subdirs = categories.get(category)
    if subdirs is None:
        print(f"No category found with the name {category}")
        return

    subdir = input(f"Pick a subdirectory ({', '.join(subdirs)}): ")
    if subdir not in subdirs:
        print(f"No subdirectory found with the name {subdir} under {category}")
        return

    app_path = f"{llm}/{category}/{subdir}/app.py"
    if not os.path.isfile(app_path):
        print(f"No app.py found in {app_path}")
        return
