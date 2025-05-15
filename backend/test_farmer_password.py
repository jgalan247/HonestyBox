from passlib.hash import argon2

stored_hash = "$argon2id$v=19$m=65536,t=3,p=4$CkqU2zSICnGSy/5mM0GEdw$k5b7Q3l8j/NlVRmEAhSwhKApBaRR7f1AZDnpX0joiBQ"
print("✅ Password matches" if argon2.verify("test123", stored_hash) else "❌ No match")

