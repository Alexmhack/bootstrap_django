from django.shortcuts import render


def home_page(request):
	return render(request, 'home_page.html')


def features_page(request):
	return render(request, 'feature_page.html')


def pricing_page(request):
	return render(request, 'pricing_page.html')


def about_page(request):
	return render(request, 'about_page.html')