from login import *

def test_login():
    db = show_login_result("bibhusha5", "sapkota6")
    assert db == "Pass"
def test_login1():
    db = show_login_result("bisesh", "sapkota")
    assert db == "Pass"
def test_login2():
    db=show_login_result("niraj2","niraj")
    assert db=="Pass"
    