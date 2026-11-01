"""
Generate static QR Code asset for Joel Lal's Portfolio Hub
Pointing to: https://bluwarrior.github.io
Output: portfolio_qr.png (600x600 PNG)
"""
import urllib.request
import os

TARGET_URL = "https://bluwarrior.github.io"
API_ENDPOINT = f"https://api.qrserver.com/v1/create-qr-code/?size=600x600&format=png&data={TARGET_URL}"
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portfolio_qr.png")

def main():
    print(f"Generating QR code for {TARGET_URL}...")
    req = urllib.request.Request(
        API_ENDPOINT,
        headers={"User-Agent": "Mozilla/5.0 (compatible; PortfolioAssetGenerator/1.0)"}
    )
    with urllib.request.urlopen(req) as response, open(OUTPUT_PATH, "wb") as out_file:
        out_file.write(response.read())
    print(f"QR code successfully saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
