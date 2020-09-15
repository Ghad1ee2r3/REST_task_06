from rest_framework.permissions import BasePermission
from django.utils import timezone

class IsOwner(BasePermission):
    message = "You must be the owner of this booking."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.user :
            return True
        else:
            return False
class ThreeDaysAway(BasePermission):
    message = "You must  have three days "

    def has_object_permission(self, request, view, obj):
        return (obj.date - timezone.now().date()).days > 3
