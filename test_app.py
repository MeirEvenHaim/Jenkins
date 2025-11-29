from app import add

def test_add():
    worth = add(2,2)
    assert worth == 4
    print(worth)
    
test_add()