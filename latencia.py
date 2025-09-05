# agent_nlp.py - Demo para Slack/GitHub integration nueva latencia

class AgentNLP:
    def __init__(self, name):
        self.name = name

    def greet_user(self, user_name):
        # Función simple de prueba
        return f"Hola {user_name}, soy el agente {self.name}!"

    def process_request(self, request):
        # Simula procesamiento de IA
        if "ayuda" in request.lower():
            return "Claro, puedo ayudarte con eso!"
        else:
            return "Procesando tu solicitud..."
