from agents.transcriber import TranscriberAgent
from agents.summarizer import SummarizerAgent
from agents.moderator import ModeratorAgent
from save_report import save_report


def main():

    audio_file = "sample_audio/test.mp3"

    # Transcription
    transcriber = TranscriberAgent()
    transcript = transcriber.transcribe(audio_file)

    # Modération
    moderator = ModeratorAgent()

    if not moderator.check(transcript):
        print("Contenu bloqué par le modérateur.")
        return

    # Résumé
    summarizer = SummarizerAgent()
    report = summarizer.summarize(transcript)

    # Affichage
    print(report)

    # Sauvegarde Markdown
    save_report(report)


if __name__ == "__main__":
    main()
