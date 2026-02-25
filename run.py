from app.main import app

if __name__ == "__main__":
    print("StyleMind AI Backend starting...")
    print("Running at http://localhost:5000")
    app.run(
        debug=True,
        port=5000,
        host="0.0.0.0",
        use_reloader=False
    )