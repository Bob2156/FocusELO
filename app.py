"""
Focus ELO — Standalone Desktop Launcher
Serves the app on localhost and opens your default browser.
Close the terminal window to stop the server.
"""
import http.server
import threading
import webbrowser
import os
import sys
import signal

PORT = 47932  # Obscure port to avoid conflicts
HOST = "127.0.0.1"

def get_html_path():
    """Find index.html next to the exe/script."""
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller .exe
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "index.html")


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """Serve files from the app directory without noisy logs."""

    def __init__(self, *args, directory=None, **kwargs):
        if getattr(sys, 'frozen', False):
            directory = sys._MEIPASS
        else:
            directory = os.path.dirname(os.path.abspath(__file__))
        super().__init__(*args, directory=directory, **kwargs)

    def log_message(self, fmt, *args):
        pass  # Silence request logs

    def end_headers(self):
        # Prevent browser from caching — always serve fresh content
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        # Serve index.html for root path
        if self.path == "/" or self.path == "":
            self.path = "/index.html"
        return super().do_GET()


def main():
    # Verify HTML exists
    html_path = get_html_path()
    if not os.path.exists(html_path):
        print(f"ERROR: Could not find index.html at {html_path}")
        input("Press Enter to exit...")
        sys.exit(1)

    # Start server
    server = http.server.HTTPServer((HOST, PORT), QuietHandler)

    # Handle Ctrl+C gracefully
    def shutdown(sig, frame):
        print("\nShutting down...")
        server.shutdown()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)

    url = f"http://{HOST}:{PORT}"

    print("=" * 48)
    print("  ⚡ Focus ELO — Running!")
    print(f"  🌐 {url}")
    print("  ❌ Close this window to stop the app")
    print("=" * 48)

    # Open browser after a tiny delay
    def open_browser():
        webbrowser.open(url)

    threading.Timer(0.5, open_browser).start()

    # Serve forever
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("Server stopped.")


if __name__ == "__main__":
    main()
