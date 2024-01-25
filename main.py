import socket

# Функция для чтения кодов из файла или их захардкоженного значения
def read_codes_from_file():
    # Здесь можно реализовать чтение кодов из файла или задать их явным образом
    # with open('codes.txt', 'r') as file:
    #     codes = file.read().splitlines()
    codes = ["PDPL9O2C", "JKP1TY3E", "VU42SBWF"]  # Пример захардкоженных кодов
    return codes

# Функция для формирования строки в указанном формате
def format_codes(codes):
    return "<p>" + "|".join(codes) + "</p>"

# Создание TCP сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))  # Привязка к localhost и порту 8888
server.listen(1)

print("Сервер запущен. Ожидание подключений...")

while True:
    client_socket, addr = server.accept()
    print(f"Подключение от {addr}")

    # Ожидание команды от клиента (нажатия Enter)
    input("Нажмите Enter для отправки кодов...")

    # Получение и формирование кодов
    codes = read_codes_from_file()
    formatted_codes = format_codes(codes)

    # Отправка сформированных кодов клиенту
    client_socket.send(formatted_codes.encode('utf-8'))

    # Закрытие соединения с клиентом
    client_socket.close()
