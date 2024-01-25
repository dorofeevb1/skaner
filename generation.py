import random
import string

# Функция для генерации случайных кодов
def generate_random_codes(num_codes, code_length):
    codes = []
    for _ in range(num_codes):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=code_length))
        codes.append(code)
    return codes

# Генерация 10 случайных кодов длиной 8 символов
random_codes = generate_random_codes(10, 8)

# Запись сгенерированных кодов в файл codes.txt
file_name = "codes.txt"
with open(file_name, 'w') as file:
    for code in random_codes:
        file.write(code + '\n')

print(f"Сгенерированные коды записаны в файл '{file_name}'.")