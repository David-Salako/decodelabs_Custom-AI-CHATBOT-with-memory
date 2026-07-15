"""
Custom AI Chatbot with Memory -- terminal entry point.

Run:
    python main.py

Commands inside the chat:
    /history   show the current in-memory conversation array
    /clear     wipe the session and start fresh
    /exit      quit
"""

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from history_manager import ChatHistory
from gemini_client import send_message

console = Console()


def print_banner() -> None:
    console.print(
        Panel.fit(
            "[bold cyan]Custom AI Chatbot with Memory[/bold cyan]\n"
            "[dim]DecodeLabs GenAI Industrial Training -- Project 1[/dim]\n\n"
            "Type your message and press Enter.\n"
            "Commands: [yellow]/history[/yellow]  [yellow]/clear[/yellow]  [yellow]/exit[/yellow]",
            border_style="cyan",
        )
    )


def print_history(history: ChatHistory) -> None:
    if history.turn_count() == 0:
        console.print("[dim]No messages yet.[/dim]")
        return
    for turn in history.get_turns():
        style = "green" if turn.role == "user" else "magenta"
        label = "You" if turn.role == "user" else "Gemini"
        console.print(f"[{style}]{label}:[/{style}] {turn.text}")


def main() -> None:
    print_banner()
    history = ChatHistory(max_turns=20)

    while True:
        try:
            raw = console.input("\n[bold green]You:[/bold green] ")
        except (KeyboardInterrupt, EOFError):
            console.print("\n[dim]Session ended.[/dim]")
            break

        if raw.strip().lower() == "/exit":
            console.print("[dim]Goodbye![/dim]")
            break

        if raw.strip().lower() == "/clear":
            history.clear()
            console.print("[yellow]History cleared.[/yellow]")
            continue

        if raw.strip().lower() == "/history":
            print_history(history)
            continue

        # Structural Validation Gate -- block empty/whitespace input
        cleaned = ChatHistory.validate_input(raw)
        if cleaned is None:
            console.print("[red]Message can't be empty. Try again.[/red]")
            continue

        try:
            with console.status("[cyan]Thinking...[/cyan]"):
                reply = send_message(history, cleaned)
        except Exception as exc:
            console.print(f"[red]Error: {exc}[/red]")
            continue

        console.print("[bold magenta]Gemini:[/bold magenta]")
        console.print(Markdown(reply))
        console.print(f"[dim]({history.turn_count()} turns in memory)[/dim]")


if __name__ == "__main__":
    main()