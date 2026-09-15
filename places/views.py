from django.shortcuts import render, redirect
import random

def get_places(request):
    if 'places' not in request.session:
        request.session['places'] = []
    return request.session['places']

def home(request):
    places = get_places(request)
    random_place = None
    
    if request.GET.get('random') and places:
        weights = [int(p['rating']) for p in places]
        random_place = random.choices(places, weights=weights, k=1)[0]
        
    return render(request, 'places/home.html', {'random_place': random_place, 'has_places': bool(places)})

def place_list(request):
    places = get_places(request)
    return render(request, 'places/list.html', {'places': places})

def add_place(request):
    if request.method == 'POST':
        places = get_places(request)
        
        new_place = {
            'id': len(places) + 1,
            'name': request.POST.get('name'),
            'desc': request.POST.get('desc'),
            'type': request.POST.get('type'),
            'location': request.POST.get('location', ''),
            'rating': int(request.POST.get('rating')),
            'date': 'Сьогодні' 
        }
        
        places.append(new_place)
        request.session.modified = True 
        
        return redirect('place_list')
        
    return render(request, 'places/add.html')