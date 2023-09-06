from app import app

print("LOGGING")
if __name__ == '__main__':
    app.run(debug=True, host="10.211.116.43", port=443)
