from django.shortcuts import render
from .models import Groups
from django.views.decorators.csrf import csrf_exempt
from json import loads
from django.http import JsonResponse

def get_all_groups(request):
    groups = Groups.objects.all()
    return render(request, 'list.html', {'groups': groups})

@csrf_exempt
def create_group(request):
    try:
        group = loads(request.body.decode('utf-8'))
        group['id'] = int(group['id'])
        group = Groups.objects.create(
            **group
        )
        group.save()
        return JsonResponse({'message': 'Group created'}, status = 201)
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
def delete_(request, id):
    try:
        user = Users.objects.get(id = int(id))
        user.delete()
        return JsonResponse({'message': 'User updated successfully'}, status = 200)
    except Exception as e:
        return JsonResponse({'error': repr(e)}, status = 400)

