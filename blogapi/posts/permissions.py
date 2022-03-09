from rest_framework import permissions

class IsAuthurOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        # read-only permissions are alowed for any permissions
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permission are only alowed for author of post
        return object.author == request.user
