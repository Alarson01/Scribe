# Scribe

Scribe est un outil de prise de notes intelligent.

## Fonctionnement

1. Lecture d'un fichier audio
2. Transcription du contenu
3. Modération du texte
4. Génération d'un compte-rendu structuré
5. Sauvegarde au format Markdown

## Architecture

Audio
→ TranscriberAgent
→ ModeratorAgent
→ SummarizerAgent
→ Markdown

## Installation

pip install -r requirements.txt

## Utilisation

python main.py

## Structure du projet

Scribe/
│
├── agents/
│   ├── transcriber.py
│   ├── summarizer.py
│   └── moderator.py
│
├── prompts/
│   └── summary_prompt.txt
│
├── outputs/
│
├── sample_audio/
│
├── config.py
├── save_report.py
├── main.py
├── requirements.txt
└── README.md