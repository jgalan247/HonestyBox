from passlib.hash import bcrypt

hashed = "$2b$12$KIXQ0cESpC6RGJ2FpQmP7uDJVkdDw/Ohmt1NvwB0X/hq0H8XZK8GC"
plain = "admin123"

if bcrypt.verify(plain, hashed):
    print("✅ Password matches")
else:
    print("❌ Password does NOT match")

