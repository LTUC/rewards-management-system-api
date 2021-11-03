from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.user.id == None:
            
            return False
        else:
          
            return request.user.role == 'instructor' 
    def has_object_permission(self, request, view, obj):
       
        if request.user.id == None:
            
            return False
        else:
          
            return request.user.role == 'instructor' 
        

class RecordOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        print(obj.role)
       
        if request.user.id == None:
            
            return False
        elif (request.method == "PATCH" or request.method == "PUT") and request.data.get("role", False):
            if request.data["role"] != obj.role and request.user.role != "instructor" :

                return False
            
            else:
                return request.user.id == obj.id or request.user.role == 'instructor'

        else:
            return request.user.id == obj.id or request.user.role == 'instructor'