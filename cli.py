import typer
from rich import print

from src.analyzer.scanner import scan_project
from src.analyzer.detector import detect_language
from src.analyzer.extractor import extract_package_json


app = typer.Typer()


@app.command()
def analyze(
    path: str = typer.Argument(...)
):
    """
    Analyze a project repository.
    """

    print("[green]Analyzing project...[/green]")


    files = scan_project(path)


    print("\n[bold]Detected files:[/bold]")

    for file in files:
        print(file)


    languages = detect_language(files)


    print("\n[bold]Languages:[/bold]")
    print(languages)


    for file in files:

        if file.name == "package.json":

            info = extract_package_json(file)

            print("\n[bold]Package Information:[/bold]")
            print(info)



if __name__ == "__main__":
    app()