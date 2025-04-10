from flask import Flask, request, jsonify
import os
import hmac
import hashlib

app = Flask(__name__)

@app.route("/")
def home():
    return "AutoPayBot está rodando!"

@app.route("/api/interactions", methods=["POST"])
def interactions():
    return jsonify({"type": 1})  # Pong response

@app.route("/verify-user")
def verify_user():
    return "Verificação de usuário funcionando."

@app.route("/terms-of-service")
def terms_of_service():
    return "<h1>Termos de Serviço</h1><p>Termos genéricos para uso do bot.</p>"

@app.route("/privacy-policy")
def privacy_policy():
    return "<h1>Política de Privacidade</h1><p>Sua privacidade é importante.</p>"

if __name__ == "__main__":
    app.run(debug=True)
