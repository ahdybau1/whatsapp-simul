from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# Token de vérification webhook
VERIFY_TOKEN = os.getenv('WEBHOOK_VERIFY_TOKEN')

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Vérification webhook WhatsApp
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            print("✅ Webhook vérifié avec succès!")
            return challenge
        else:
            return 'Verification failed', 403
    
    elif request.method == 'POST':
        # Réception des messages entrants
        data = request.json
        print("📨 Message reçu:", json.dumps(data, indent=2))
        
        # Ici vous pouvez traiter les réponses des utilisateurs
        return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
