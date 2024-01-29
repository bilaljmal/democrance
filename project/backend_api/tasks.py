from project.main.celery import app



@app.task
def test_task():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

