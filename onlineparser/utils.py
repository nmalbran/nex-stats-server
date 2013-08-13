

def save_uploaded_file(filename, data):
    with open(filename, 'wb+') as destination:
        for chunk in data.chunks():
            destination.write(chunk)