from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'seguridad/index.html')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'seguridad/user_list.html', {'users': users})

@login_required
def edit_user_groups(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        groups = request.POST.getlist('groups')
        user.groups.set(groups)
        return redirect('user_list')
    all_groups = Group.objects.all()
    return render(request, 'seguridad/edit_user_groups.html', {'user': user, 'all_groups': all_groups})

@login_required
def delete_user(request, user_id):
    user_to_delete = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        if request.user.groups.filter(name='Administradores').exists():
            user_to_delete.delete()
            messages.success(request, 'User deleted successfully.')
        else:
            messages.error(request, 'You do not have permission to delete this user.')
        return redirect('user_list')
    return render(request, 'seguridad/confirm_delete.html', {'user': user_to_delete})
