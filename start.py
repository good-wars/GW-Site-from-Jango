import os
import time
import asyncio
import htmlc as hc
import app

def main():
    app.app.run(debug=True)

if __name__ == "__main__":
    main()
    asyncio.run(hc.start())