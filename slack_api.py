# slack_api.py
import time

def send_message_to_slack(channel, message):
    """
    Simula el envío de un mensaje a Slack.
    """
    print(f"[{channel}] {message}")
    time.sleep(1)
    return "Mensaje enviado con éxito"

if __name__ == "__main__":
    result = send_message_to_slack("#legal-ai", "Hola equipo 👋, el agente legal está en pruebas.")
    print(result)
