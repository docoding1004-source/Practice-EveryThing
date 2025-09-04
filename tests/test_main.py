from app.main import greet

def test_greet():
    assert greet("Lee") == "Hello, Lee!"