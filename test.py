from main import sravnit

def test_sravnit():
    assert sravnit(1, 1) == True
    assert sravnit(-1, 4) == False
    assert sravnit(10, 10) == True
    print("Все правильно!")

test_sravnit()