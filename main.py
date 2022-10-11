from website import create_app, db

if __name__=='__main__':
    napp=create_app()
    napp.run(debug=True)
    db.create_all
    