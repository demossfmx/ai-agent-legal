# demo_api.py
# Ejemplo súper básico de un "API" para Slack

def send_message_to_slack(channel, message):
    print(f"[Slack] Enviando mensaje a {channel}: {message}")

if __name__ == "__main__":
    send_message_to_slack("#legal-demo", "Contrato recibido, iniciando análisis...")
