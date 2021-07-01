PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "6aba808729630748572148be53299109",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": True,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.cloudflare.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"

TO_CLT_BUFSIZE = 262144
TO_TG_BUFSIZE = 262144