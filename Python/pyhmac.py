import hmac
import base64
from hashlib import sha256

key = "abcd1234"
message = "my lover is only you"
# hmac.new will new a hash object that encrypts message with a secret key and a hash mothed(digestmod)
# messqge and secret need to be byte type.
bkey = key.encode('utf-8') 
bmessage = message.encode('utf-8')
sha = hmac.new(bkey, bmessage, digestmod=sha256)
#digest() method will return the byte code of a hash object.
#hexdigest() method will return the hex code of a hash object.
print("\nSha-256 Binary Digest: %s"%sha.digest())
print("Sha-256 Hex Digest: %s\n"%sha.hexdigest())
#for delivery hash code via network, we need to transform it into a base64 string format. 
signature= base64.b64encode(sha.digest())
print("Secret Key = %s"%key)
print("Message = %s\n"%message)
print("SHA-256 Signature: %s\n\n"%signature)