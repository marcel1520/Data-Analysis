from analysis.app.create_app import make_app

app = make_app()

if __name__ == "__main__":
    app.run(debug=True)