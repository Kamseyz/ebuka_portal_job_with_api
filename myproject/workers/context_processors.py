#MAKES SURES ONLY WORKER ALONG CAN SEE THE DOWNLOAD CV, UPLOAD CV AND LOGOUT WITH APPLY BUTTON 

def is_worker_user(request):
    is_worker = (
        request.user.is_authenticated and 
        getattr(request.user, 'user_type', None) == 'worker' and 
        hasattr(request.user, 'workerdetails')
    )
    return {'is_worker': is_worker}