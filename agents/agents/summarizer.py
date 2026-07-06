class SummarizerAgent:

    def __init__(self):
        print("Agent Summarizer initialisé")

    def summarize(self, transcript):

        report = f"""
# Compte rendu

## Résumé

{transcript}

## Points clés

- Point clé 1
- Point clé 2

## Actions

- Action 1
"""

        return report
