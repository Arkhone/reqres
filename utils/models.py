from faker import Faker

fake = Faker()


class RegisterUser:
    @staticmethod
    def registration_user():
        email = "eve.holt@reqres.in"
        password = "pistol"
        return {"email": email, "password": password}

    @staticmethod
    def login_user():
        email = "eve.holt@reqres.in"
        password = "cityslicka"
        return {"email": email, "password": password}

    @staticmethod
    def random_user_c():
        name = fake.name()
        job = fake.job()
        return {"name": name, "job": job}

    @staticmethod
    def invalid_user():
        email = "sydney@fife"
        return {"email": email}


class UpdateUser:
    @staticmethod
    def user_up():
        name = 'morpheus'
        job = fake.job()
        return {"name": name, "job": job}