# chatbot/apps.py
from django.apps import AppConfig

class ChatbotConfig(AppConfig):
    name = 'chatbot'

    def ready(self):
        import chatbot.views  # Import views to trigger the function
        chatbot.views.create_default_user()  # Ensure the default user is created
