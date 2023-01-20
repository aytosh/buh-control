from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail

from rest_framework import serializers

User = get_user_model()


# student_class RegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     name = serializers.CharField(required=False)
#     password = serializers.CharField(required=True, min_length=6)
#     password_confirmation = serializers.CharField(required=True, min_length=6)
#
#     def validate_email(self, email):
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError('Адрес почты уже занят')
#         return email
#
#     def validate(self, attrs):
#         password = attrs.get('password')
#         password_confirmation = attrs.pop('password_confirmation')
#         if password != password_confirmation:
#             raise serializers.ValidationError('Пароли не совподают')
#         return attrs
#
#     def create(self):
#         attrs = self.validated_data
#         user = User.objects.create_user(**attrs)
#         code = user.generate_activation_code()
#         user.send_activation_mail(user.email, code)
#         return user


# student_class ActivationSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     code = serializers.CharField(min_length=8, max_length=8)
#
#     def validate_email(self, email):
#         if not User.objects.filter(email=email).exists():
#             raise serializers.ValidationError('Пользователь не зарегистрирован')
#         return email
#
#     def validate_code(self, code):
#         if not User.objects.filter(activation_code=code).exists():
#             raise serializers.ValidationError('Пользователь не зарегистрирован')
#         return code
#
#
#     def validate(self, attrs):
#         email = attrs.get('email')
#         code = attrs.get('code')
#         if not User.objects.filter(email=email, activation_code=code).exists():
#             raise serializers.ValidationError('Пользователь не найден')
#         return attrs
#
#     def activate(self):
#         email = self.validated_data.get('email')
#         user = User.objects.get(email=email)
#         user.is_active = True
#         user.activation_code = ''
#         user.save()

class LoginSerializer(serializers.Serializer):
    # email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True)

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError('User have not signed up')
        return username

    def validate(self, attrs):
        request = self.context.get('request')
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = authenticate(username=username, password=password, request=request)
            if not user:
                raise serializers.ValidationError('Invalid username or password')
        else:
            raise serializers.ValidationError('Username and password required')
        attrs['user'] = user
        return attrs

# student_class ChangePasswordSerializer(serializers.Serializer):
#     old_pass = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, min_length=6)
#     password_confirm = serializers.CharField(required=True, min_length=6)
#
#     def validate_old_pass(self, old_pass):
#         user = self.context.get('request').user
#         if not user.check_password(old_pass):
#             raise serializers.ValidationError('Неверный пароль')
#         return old_pass
#
#     def validate(self, attrs):
#         pass1 = attrs.get('password')
#         pass2 = attrs.get('password_confirm')
#         if pass1 != pass2:
#             raise serializers.ValidationError('Пароли не совподают')
#         return attrs
#
#     def set_new_pass(self):
#         user = self.context.get('request').user
#         password = self.validated_data.get('password')
#         user.set_password(password)
#         user.save()


# student_class ForgotPasswordSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#
#     def validate_email(self, email):
#         if not User.objects.filter(email=email).exists():
#             raise serializers.ValidationError('Пользователь не зарегистрирован')
#         return email
#
#     def send_code(self):
#         email = self.validated_data.get('email')
#         user = User.objects.get(email=email)
#         user.generate_activation_code()
#         send_mail(
#             'Восстановление пароля',
#             f'Ваш код потверждения: {user.generate_activation_code()}',
#             'abai@gmail.com',
#             [email]
#         )

# student_class ForgetPasswordCompleteSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     # code = serializers.CharField(min_length=8, max_length=8, required=True)
#     password = serializers.CharField(required=True)
#     password_confirm = serializers.CharField(required=True)
#
#     def validate_email(self, email):
#         if not User.objects.filter(email=email).exists():
#             raise serializers.ValidationError('Пользователь не зарегистрирован')
#         return email
#
#     def validate_code(self, code):
#         if not User.objects.filter(activation_code=code).exists():
#             raise serializers.ValidationError('Пользователь не зарегистрирован')
#         return code
#
#     def validate(self, attrs):
#         pass1 = attrs.get('password')
#         pass2 = attrs.get('password_confirm')
#         if pass1 != pass2:
#             raise serializers.ValidationError('Пароли не совподают')
#         return attrs
#
#     def set_new_pass(self):
#         email = self.validated_data.get('email')
#         password = self.validated_data.get('password')
#         user = User.objects.get(email=email)
#         user.set_password(password)
#         user.activation_code = ''
#         user.save()