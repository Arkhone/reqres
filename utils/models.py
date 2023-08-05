from faker import Faker

fake = Faker()


class CreateUser:
    @staticmethod
    def random_user_c():
        name = fake.name()
        job = fake.job()
        return {"name": name, "job": job}


class RegisterUser:
    @staticmethod
    def random_user_r():
        email = fake.email()
        password = fake.password()
        return {"email": email, "password": password}
