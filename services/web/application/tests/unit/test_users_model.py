from application.api.users.models import User

def test_passwords_are_random(test_app, test_database, add_user):
    user_one = add_user('jonny', 'jon@sessionsdev.com', 'password')
    user_two = add_user('kristen', 'kristen@sessionsdev.com', 'password')
    assert user_one.password != user_two.password

def test_encode_token(test_app, test_database, add_user):
    user = add_user('test', 'test@test.com', 'test')
    token = user.encode_token(user.id, 'access')
    assert isinstance(token, bytes)

def test_decode_token(test_app, test_database, add_user):
    user = add_user('test', 'test@test.com', 'test')
    token = user.encode_token(user.id, 'access')
    assert isinstance(token, bytes)
    assert User.decode_token(token) == user.id