class ModeratorAgent:

    def __init__(self):
        print("Agent Moderator initialisé")

    def check(self, transcript):

        forbidden_words = [
            "piratage",
            "hack",
            "virus"
        ]

        for word in forbidden_words:

            if word.lower() in transcript.lower():
                return False

        return True
