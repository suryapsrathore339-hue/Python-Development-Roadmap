from utils.security import hash_password, verify_password


password = "surya123"

hashed = hash_password(password)

print("Password:", password)
print("Hash:", hashed)

print(
    "Correct password:",
    verify_password(password, hashed)
)

print(
    "Wrong password:",
    verify_password("wrongpassword", hashed)
)