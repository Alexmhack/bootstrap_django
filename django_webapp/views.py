from django.shortcuts import render


def home_page(request):
	return render(request, 'bootstrap/home_page.html')


def features_page(request):
	return render(request, 'bootstrap/feature_page.html')


def pricing_page(request):
	return render(request, 'bootstrap/pricing_page.html')


def about_page(request):
	return render(request, 'bootstrap/about_page.html')