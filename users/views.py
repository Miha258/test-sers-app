from django.shortcuts import render
from .models import Users
from django.views.decorators.csrf import csrf_exempt
from json import loads
from django.http import JsonResponse

def get_all_users(request):
    users = Users.objects.all()
    return render(request, 'list.html', {'users': users})

@csrf_exempt
def create_user(request):
    try:
        user = loads(request.body.decode('utf-8'))
        if not user['email'] or not user['username']:
            return JsonResponse({'error': 'Fll in all fields'}, status = 400)
        user = Users.objects.create(
            username = user['username'], 
            email = user['email'], 
            group_id = int(user['group_id']), 
            is_admin = user['is_admin']
        )
        user.save()
        return JsonResponse({'message': 'User created'}, status = 201)
    except ValueError:
        return JsonResponse({'error': 'Invalid group value.Try again'}, status = 400)

@csrf_exempt
def edit_user(request, id):
    try:
        updated = loads(request.body.decode('utf-8'))
        user = Users.objects.get(id = int(id))
        print(user.username)
        user.username = updated['username']
        user.group_id = int(updated['group_id'])
        user.is_admin = updated['is_admin']
        
        user.save()
        print(Users.objects.get(id = int(id)).username)
        return JsonResponse({'message': 'User updated successfully'}, status = 200)
    except ValueError:
        return JsonResponse({'error': 'Invalid group value. Try again'}, status = 400)

@csrf_exempt
def delete_user(request, id):
    try:
        user = Users.objects.get(id = int(id))
        user.delete()
        return JsonResponse({'message': 'User updated successfully'}, status = 200)
    except Exception as e:
        return JsonResponse({'error': repr(e)}, status = 400)
