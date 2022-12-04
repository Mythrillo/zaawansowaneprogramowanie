import os
import secrets


PUBLIC_API_KEY = os.environ.get("PUBLIC_API_KEY", secrets.token_urlsafe(16))
