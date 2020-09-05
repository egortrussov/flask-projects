from app import app;
import jwt

def decode_token(token):
    try: 
        decoded = jwt.decode(token, app.config['SECRET_KEY'])
        return decoded 
    except jwt.ExpiredSignatureError:
        return {
            'is_err': True,
            'msg': 'Invalid token'
        }