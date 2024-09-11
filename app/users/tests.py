from django.test import TestCase
from django.contrib.auth import get_user_model

# TDD: Test Driven Development (테스트 주도 개발)
# => 채용공고 => 우대사항: TDD
class UserTestCase(TestCase):
    
    # 일반 유저 생성 테스트 함수
    def test_create_user(self):
        email = 'inseop@gmail.com'
        password = 'password123'
        
        user = get_user_model().objects.create_user(email=email, password=password)
        
        # 유저가 정상적으로 잘 만들어졌는지?
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)
        
        
    
    # 슈퍼 유저 생성 테스트 함수
    def test_create_superuser(self):
        email = 'inseop_super@gmail.com'
        password = 'password123'
        
        user = get_user_model().objects.create_superuser(
            email=email, password=password
            )
         
        # 슈퍼유저
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

# docker-compose run --rm app sh -c 'python manage.py makemigrations'
# docker-compose run --rm app sh -c 'python manage.py migrate'
# docker-compose run --rm app sh -c 'python manage.py test users'