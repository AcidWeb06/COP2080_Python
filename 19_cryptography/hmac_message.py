import hmac #hash-based message authentification
import hashlib

def calc_hash(key: str, message: str):
    b_key = bytes(key, "utf-8")
    b_message = bytes(message, "utf-8")

    hash_value = hmac.new(b_key, b_message, hashlib.sha256)
    return hash_value.hexdigest()

secret_key = "very_secret_key"
message1 = calc_hash(secret_key, "Pay $100")
message2 = calc_hash(secret_key, "Pay $100")
message3 = calc_hash(secret_key, "Pay $1000")

print(message1 == message2)
print(message2 == message3)