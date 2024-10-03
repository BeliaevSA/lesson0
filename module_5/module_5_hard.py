import time


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        current_user = None
        for user in self.users:
            if user.nickname == nickname or user.password == hash(password):
                current_user = user
                break
        if current_user:
            self.current_user = current_user
            # print("Вы успешно вошли!")
        else:
            print("Неверный логин или пароль")

    def register(self, nickname: str, password: str, age: int):
        auth = False
        for user in self.users:
            if user.nickname == nickname:
                auth = True
                break
        if auth:
            print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, password, age)
            self.users.append(user)

            self.log_in(nickname, password)
            # print(f"Пользователь {nickname} успешно зарегистрирован")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        new_videos = args
        for new_video in new_videos:
            if isinstance(new_video, Video):
                repeat_video = False
                for video in self.videos:
                    if video.title == new_video.title:
                        repeat_video = True
                        break
                if repeat_video:
                    print(f"Видео {new_video.title} уже существует")
                else:
                    self.videos.append(new_video)
                    # print(f"Видео {new_video.title} успешно добавлено")

    def get_videos(self, query):
        find_videos = []
        for video in self.videos:
            if query.lower() in video.title.lower():
                find_videos.append(video.title)
        return find_videos

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video_to_watch = None
        for video in self.videos:
            if video.title.lower() == title.lower():
                video_to_watch = video
        if video_to_watch:
            if self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            for sec in range(1, video_to_watch.duration + 1):
                time.sleep(1)
                print(sec)
            print("Конец видео")
        else:
            print(f"Видео {title} не найдено")


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')