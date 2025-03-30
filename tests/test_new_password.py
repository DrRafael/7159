import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, проверяющий длину пароля."""
    lengths = [5, 20, 32, 42, 21]
    for length in lengths:
        assert len(generate_password(length)) == length

def test_password_uniq():
    """Тест, проверяющий уникальность паролей."""
    assert generate_password(100) != generate_password(100) 
        
