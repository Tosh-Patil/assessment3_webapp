from website import create_app, db

if __name__=='__main__':
    app=create_app()
    app.run(debug=True)
    ctx=app.app_context()
    ctx.push()
    db.create_all()
    