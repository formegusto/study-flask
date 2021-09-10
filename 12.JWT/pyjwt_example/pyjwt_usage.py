import jwt

secret = "formegusto@jwt"
json = {
    "user-id": "10289384",
    "usernamne": "formegusto"
}
encoded = jwt.encode(json, secret, algorithm="HS256")
decoded = jwt.decode(encoded, secret, algorithms="HS256")

print(encoded)
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyLWlkIjoiMTAyODkzODQiLCJ1c2VybmFtbmUiOiJmb3JtZWd1c3RvIn0.b1yFI1IW7gC3feZ9BssovawJx_LYxk8nTLZlviM90OI
print(decoded)
# {'user-id': '10289384', 'usernamne': 'formegusto'}
