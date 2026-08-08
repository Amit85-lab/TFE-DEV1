import requests
import sys

# ============================================================
# Configuration
# ============================================================

TFE_URL = "https://app.terraform.io"

TFE_TOKEN = os.getenv("TFE_TOKEN")
GITHUB_TOKEN = os.getenv("TFE_TOKEN")

ORGANIZATION = "TFE-DEV1"

VCS_NAME = "GitHub"


# ============================================================
# API URL
# ============================================================

url = (
    f"{TFE_URL}/api/v2/organizations/"
    f"{ORGANIZATION}/oauth-clients"
)


# ============================================================
# Headers
# ============================================================

headers = {
    "Authorization": f"Bearer {TFE_TOKEN}",
    "Content-Type": "application/vnd.api+json",
    "Accept": "application/vnd.api+json"
}


# ============================================================
# Request payload
# ============================================================

payload = {
    "data": {
        "type": "oauth-clients",

        "attributes": {
            "service-provider": "github",
            "name": VCS_NAME,

            "http-url": "https://github.com",
            "api-url": "https://api.github.com",

            # GitHub Personal Access Token
            "oauth-token-string": GITHUB_TOKEN,

            # Make it available to the complete organization
            "organization-scoped": True
        }
    }
}


# ============================================================
# Create VCS Provider
# ============================================================

response = requests.post(
    url,
    headers=headers,
    json=payload
)


# ============================================================
# Handle response
# ============================================================

if response.status_code == 201:

    result = response.json()["data"]

    print("\nVCS Provider created successfully")
    print("----------------------------------------")

    print("OAuth Client ID :", result["id"])

    attributes = result["attributes"]

    print("Provider        :", attributes.get("service-provider"))
    print("Name            :", attributes.get("name"))
    print("HTTP URL        :", attributes.get("http-url"))
    print("API URL         :", attributes.get("api-url"))
    print("Callback URL    :", attributes.get("callback-url"))

    # OAuth token is returned through the relationship
    oauth_tokens = (
        result
        .get("relationships", {})
        .get("oauth-tokens", {})
        .get("data", [])
    )

    if oauth_tokens:
        print("OAuth Token ID  :", oauth_tokens[0]["id"])
    else:
        print("OAuth Token ID  : Not returned in response")

else:

    print("\nFailed to create VCS Provider")
    print("----------------------------------------")
    print("HTTP Status:", response.status_code)
    print("Response:")
    print(response.text)

    sys.exit(1)
