from passlib.hash import argon2

stored = "$argon2id$v=19$m=65536,t=3,p=4$GC6ceYG8ZYENk+fDGZnq+g$A3TQBPeg2RcDIfNprn5BbRaAYZ2ztO1YmPxvwDiNntk"
print("✅ Match" if argon2.verify("admin123", stored) else "❌ No match")

