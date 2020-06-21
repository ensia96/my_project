import json
import bcrypt
import jwt

from my_settings import SECRET

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import User


class UserAuthView(View):
    def make_token(self, user):
        return jwt.encode(
            {"user": user.id}, SECRET["key"], algorithm=SECRET["algorithm"]
        )

    def create_account(self, data):
        account = User.objects.create(
            user=data["user"],
            password=bcrypt.hashpw(
                data["password"].encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8"),
        )
        return account

    def post(self, request):
        data = json.loads(request.body)

        account = User.objects.filter(user=data["user"])

        if not account:
            account = self.create_account(data)
            token = self.make_token(account).decode("utf-8")
            return JsonResponse({"Authorization": token}, status=201)

        if bcrypt.checkpw(
            data["password"].encode("utf-8"), account.first().password.encode("utf-8")
        ):
            token = self.make_token(account.first()).decode("utf-8")
            return JsonResponse({"Authorization": token}, status=200)

        return JsonResponse({"MESSAGE": "FAILED_TO_LOGIN"}, status=401)
