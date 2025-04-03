import ecdsa, os

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSign.clicked.connect(self.call_api_sign)  # Corrected attribute name
        self.ui.btnVerify.clicked.connect(self.call_api_verify)  # Corrected attribute name

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()  # Generate private key
        vk = sk.get_verifying_key()  # Get public key from private key

        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        # Sign data with private key
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        sk, vk = self.load_keys()
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False
