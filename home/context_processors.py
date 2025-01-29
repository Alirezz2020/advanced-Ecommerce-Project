from datetime import datetime

def add_current_year(request):
    return {'current_year': datetime.now().year}
