import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
gmt = time.gmtime()
ts = calendar.timegm(gmt)/(3600*24)
rnd = random.seed(ts)

secret_key = ''.join(rnd.choice(string.ascii_uppercase + string.digits) for x in range(32))

class Verifier:
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            # Valid Token, but expired
            return None
        except BadSignature:
            # Invalid Token
            return None
        user_id = data['id']
        return user_id

    @staticmethod
    def generate_auth_token(id, expiration=1800):
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'id': id})
