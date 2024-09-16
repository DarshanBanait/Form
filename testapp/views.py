from django.shortcuts import render, redirect
from .forms import PHQGADForm
from .models import PHQGADResponse

def phq_gad_test_view(request):
    if request.method == 'POST':
        form = PHQGADForm(request.POST, request.FILES)
        if form.is_valid():
            # Section 1: User Info
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            devices_used = ', '.join(form.cleaned_data['devices_used'])
            app_types = ', '.join(form.cleaned_data['app_types'])
            main_screen_time_contributor = ', '.join(form.cleaned_data['main_screen_time_contributor'])
            screen_time_screenshot = request.FILES['screen_time_screenshot']

            # Section 2: PHQ-9 (Depression)
            phq_scores = [int(form.cleaned_data[f'phq_question_{i}']) for i in range(1, 10)]
            phq_score = sum(phq_scores)

            # Section 3: GAD-7 (Anxiety)
            gad_scores = [int(form.cleaned_data[f'gad_question_{i}']) for i in range(1, 8)]
            gad_score = sum(gad_scores)
            
            # Save response to database
            PHQGADResponse.objects.create(
                name=name,
                email=email,
                gender=gender,
                age=age,
                devices_used=devices_used,
                app_types=app_types,
                main_screen_time_contributor=main_screen_time_contributor,
                screen_time_screenshot=screen_time_screenshot,
                phq_total_score=phq_score,
                gad_total_score=gad_score,
            )

            # Redirect to results page
            return render(request, 'testapp/result.html', {
                'phq_score': phq_score,
                'gad_score': gad_score
            })
    else:
        form = PHQGADForm()

    return render(request, 'testapp/phq_gad_test.html', {'form': form})
