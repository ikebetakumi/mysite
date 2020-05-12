import uuid

def get_submit_token(request):
    submit_token = str(uuid.uuid4())
    request.session['submit_token'] = submit_token
    return submit_token

def exists_submit_token(request):
    token_in_request = request.POST.get('submit_token')
    token_in_session = request.session.get('submit_token', '')
    print(token_in_request)
    print(token_in_session)
    if not token_in_request:
        return False
    if not token_in_session:
        return False

    return token_in_request == token_in_session