from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/diagnostico", methods=["POST"])
def diagnostico():
    data = request.json
    respostas = []

    if data.get("fastfood") == 's':
        respostas.append("🍕 Solução: Tente consumir fastfood no máximo 1x na semana.")

    if data.get("verduraselegumes") == 'n':
        respostas.append("🥗 Solução: Tente consumir verduras e legumes no seu dia a dia.")

    if data.get("agua") == 'n':
        respostas.append("🥤 Solução: Tomar no mínimo 2L de água no seu dia.")

    if data.get("exercícios") == 'n':
        respostas.append("🏃‍➡ Solução: Pratique ao menos 3x na semana atividades físicas.")

    if data.get("nutri") == 'n':
        respostas.append("🍏 Solução: Faça acompanhamento nutricional para melhorar sua saúde.")

    if data.get("saude") == 'n':
        respostas.append("❤‍🩹 Solução: Procure um especialista para te ajudar na sua nova vida saudável.")

    if not respostas:
        respostas.append("✅👏 Parabéns! Sua vida está andando em uma linha completamente saudável. Continue assim!")

    resposta_final = "\n".join(respostas)

    return jsonify({"resposta": resposta_final})

if __name__ == "__main__":
    app.run(debug=True)