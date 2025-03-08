from flask import Flask
from flask_socketio import SocketIO

# Crear la instancia de SocketIO que será compartida en toda la aplicación
socketio = SocketIO()

def create_app():
    app = Flask(__name__, 
                template_folder='../templates', 
                static_folder='../static')
    
    app.config['SECRET_KEY'] = 'clave-secreta-segura'
    
    # Inicializar SocketIO con la aplicación
    socketio.init_app(app, cors_allowed_origins="*")
    
    # Registrar rutas
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app