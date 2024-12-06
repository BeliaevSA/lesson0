import requests
from PIL import Image



#Осуществляем Get запрос на сервер и получаем данные
r = requests.get('https://api.github.com/users')
users = r.json()
# print(r.json()[0])
data_users = []
for user in users:
    data_users.append({'login': user['login'], 'id': user['id']})
print(data_users)

#Осуществляем Post запрос, для отправки данных на сервер
payload = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.post('https://httpbin.org/post', data=payload)
print(r2.json()['form'])


# Работа с изображением
def apply_sepia(image):
    image = image.convert('RGB')
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.189 * b)

            pixels[x, y] = (min(tr, 255), min(tg, 255), min(tb, 255))
    return image

def process_image(input_path, output_path):
    image = Image.open(input_path)
    image.show()
    new_size = (image.width * 2, image.height * 2)
    image = image.resize(new_size)
    image = apply_sepia(image)
    image.save(output_path, 'PNG')
    image.show()


process_image('kak-delat-khoroshie-fotografii-03.jpg', 'kak-delat-khoroshie-fotografii-03.png')
