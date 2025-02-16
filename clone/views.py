from django.shortcuts import render, redirect

def home(request):
    selected_theme = request.session.get('theme', 'default.css')  # Default theme
    return render(request, 'clone/home.html', {'selected_theme': selected_theme})

def set_theme(request, theme_name):
    request.session["theme"] = theme_name
    return redirect('/')



