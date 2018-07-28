from django.shortcuts import render
from django.template.loader import get_template
from django.core.email import EmailMessage


def home_page(request):
	return render(request, 'bootstrap/home_page.html')


def features_page(request):
	return render(request, 'bootstrap/feature_page.html')


def pricing_page(request):
	return render(request, 'bootstrap/pricing_page.html')


def about_page(request):
	return render(request, 'bootstrap/about_page.html')


def contact_page(request):
	if request.method == 'POST':
		user_name = request.POST.get('name')
		user_email = request.POST.get('email')
		user_subject = request.POST.get('subject')
		user_message = request.POST.get('message')

		template = get_template('contact_tempalate.txt')
		context = {
			'contact_name': user_name,
			'contact_email': user_email,
			'contact_subject': user_subject,
			'contact_message': user_message
		}

		content = template.render(context)
		email = EmailMessage(
			"New contact form submission",
			content,
			"Your website ",
			['78030psg@gmail.com'],
			headers={'Reply-To': user_email})

		email.send()
		return redirect('contact_form')

	return render(request, 'contact.html')