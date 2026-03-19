from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    nombre_proyecto = os.environ.get("AMB_PROYECTO", "No configurado")
    
    return f"✅ Entorno configurado correctamente - Proyecto: {nombre_proyecto}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
