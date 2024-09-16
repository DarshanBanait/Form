from django import forms

class PHQGADForm(forms.Form):
    # Section 1: User Information
    name = forms.CharField(label='Your Name', max_length=100, required=True)
    email = forms.EmailField(label='Email Address', required=True)
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        label='Gender',
        required=True
    )
    age = forms.IntegerField(label='Age', required=True)
    devices_used = forms.MultipleChoiceField(
        choices=[('SmartPhone', 'SmartPhone'), ('Laptop', 'Laptop'), ('Tablet', 'Tablet'), ('Desktop PC', 'Desktop PC')],
        widget=forms.CheckboxSelectMultiple,
        label='Which devices do you use daily?',
        required=True
    )
    app_types = forms.MultipleChoiceField(
        choices=[('Social Media', 'Social Media (e.g., Instagram, Snapchat)'), ('Gaming', 'Gaming (e.g., Call of Duty, Candy Crush)'), ('Online Chatting', 'Online Chatting (e.g., WhatsApp, Telegram)'), ('Entertainment', 'Entertainment (e.g., Netflix, YouTube)'), ('Browsing', 'Browsing (e.g., Chrome, Edge)')],
        widget=forms.CheckboxSelectMultiple,
        label='What types of apps do you use?',
        required=True
    )
    main_screen_time_contributor = forms.MultipleChoiceField(
        choices=[('Social Media', 'Social Media (e.g., Instagram, Snapchat)'), ('Gaming', 'Gaming (e.g., Call of Duty, Candy Crush)'), ('Online Chatting', 'Online Chatting (e.g., WhatsApp, Telegram)'), ('Entertainment', 'Entertainment (e.g., Netflix, YouTube)'), ('Browsing', 'Browsing (e.g., Chrome, Edge)')],
        widget=forms.CheckboxSelectMultiple,
        label='Which app contributes most to your screen time?',
        required=True
    )
    screen_time_screenshot = forms.ImageField(label='Upload a screenshot of your screen time (Weekly Report)', required=True)

    # Section 2: PHQ-9 (Depression)
    phq_scale_description = forms.CharField(
        widget=forms.Textarea(attrs={'readonly': 'readonly', 'rows': 3}),
        initial="Scale: 0 = Not at all; 1 = Several days; 2 = More than half the days; 3 = Nearly every day",
        label='PHQ-9 Scale Description',
        required=False
    )
    phq_question_1 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Little interest or pleasure in doing things',
        required=True
    )
    phq_question_2 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Feeling down, depressed, or hopeless',
        required=True
    )
    phq_question_3 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Trouble falling asleep, staying asleep or sleeping too much',
        required=True
    )
    phq_question_4 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Feeling tired or having little energy',
        required=True
    )
    phq_question_5 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Poor appetite or overeating',
        required=True
    )
    phq_question_6 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Feeling bad about yourself or like a failure',
        required=True
    )
    phq_question_7 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Trouble concentrating on things',
        required=True
    )
    phq_question_8 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Moving or speaking slowly or being fidgety',
        required=True
    )
    phq_question_9 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Thoughts of being better off dead or hurting yourself',
        required=True
    )

    # Section 3: GAD-7 (Anxiety)
    gad_scale_description = forms.CharField(
        widget=forms.Textarea(attrs={'readonly': 'readonly', 'rows': 3}),
        initial="Scale: 0 = Not at all; 1 = Several days; 2 = More than half the days; 3 = Nearly every day",
        label='GAD-7 Scale Description',
        required=False
    )
    gad_question_1 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Feeling nervous, anxious, or on edge',
        required=True
    )
    gad_question_2 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Not being able to stop or control worrying',
        required=True
    )
    gad_question_3 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Worrying too much about different things',
        required=True
    )
    gad_question_4 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Trouble relaxing',
        required=True
    )
    gad_question_5 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Being so restless that it is hard to sit still',
        required=True
    )
    gad_question_6 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Becoming easily annoyed or irritable',
        required=True
    )
    gad_question_7 = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        label='Feeling afraid as if something awful might happen',
        required=True
    )
