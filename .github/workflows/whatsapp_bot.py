import os
import requests
import json
import time
from datetime import datetime

# Configuration - Récupère automatiquement depuis GitHub Secrets
PHONE_ID = os.getenv('PHONE_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
WEBHOOK_VERIFY_TOKEN = os.getenv('WEBHOOK_VERIFY_TOKEN')

class WhatsAppBot:
    def __init__(self):
        self.base_url = f"https://graph.facebook.com/v17.0/{PHONE_ID}"
        self.headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
    
    def send_message(self, phone_number, message):
        """Envoie un message WhatsApp automatiquement"""
        url = f"{self.base_url}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "text": {"body": message},
            "context": {
                "message_id": f"msg_{int(time.time())}"
            }
        }
        
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            print(f"✅ Message envoyé à {phone_number}: {response.status_code}")
            return response.json()
        except Exception as e:
            print(f"❌ Erreur: {e}")
            return None
    
    def process_pending_messages(self):
        """Traite les messages en attente - À ADAPTER avec votre base de données"""
        # EXEMPLE - À remplacer par votre propre logique
        pending_messages = [
            {
                "phone": "+237677536642",  # Votre numéro de test
                "message": "🔄 **SYSTÈME AUTOMATIQUE ACTIVÉ**\n\nBonjour ! Votre système d'envoi automatique WhatsApp est maintenant opérationnel. Vous recevrez automatiquement les messages pour chaque nouvel inscrit.\n\n✅ Configuration réussie\n🤖 Système 100% autonome\n📱 Numéro: +237 677536642\n\nFélicitations ! 🎉"
            }
        ]
        
        for msg in pending_messages:
            self.send_message(msg["phone"], msg["message"])
            time.sleep(2)  # Pause entre les messages

if __name__ == "__main__":
    print("🚀 Démarrage du Bot WhatsApp Auto-Sender...")
    bot = WhatsAppBot()
    bot.process_pending_messages()
    print("✅ Traitement terminé à", datetime.now())
