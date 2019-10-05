from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to only update their own Profiles"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit thier own profile
            Every time a request is made this function is called.
            eg, when we update a profile
        """
        if request.method in permissions.SAFE_METHODS:
            """Safe methods include those requests that donot update/del/write to a model object
               eg: GET request --->allow all to see anyones profile but not edit the same.
            """
            return True
        else:
            """If methods are not SAFE then check if user is trying to edit his/hers own prof"""
            return obj.id == request.user.id
