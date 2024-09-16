from django.db import models

class PHQGADResponse(models.Model):
    # Section 1: User Information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    devices_used = models.CharField(max_length=255)  # For storing checkbox values
    app_types = models.CharField(max_length=255)     # For storing checkbox values
    main_screen_time_contributor = models.CharField(max_length=255)
    screen_time_screenshot = models.ImageField(upload_to='screenshots/')
    
    # Section 2: PHQ-9 (Depression)
    phq_question_1 = models.IntegerField()
    phq_question_2 = models.IntegerField()
    phq_question_3 = models.IntegerField()
    phq_question_4 = models.IntegerField()
    phq_question_5 = models.IntegerField()
    phq_question_6 = models.IntegerField()
    phq_question_7 = models.IntegerField()
    phq_question_8 = models.IntegerField()
    phq_question_9 = models.IntegerField()
    phq_total_score = models.IntegerField(editable=False)

    # Section 3: GAD-7 (Anxiety)
    gad_question_1 = models.IntegerField()
    gad_question_2 = models.IntegerField()
    gad_question_3 = models.IntegerField()
    gad_question_4 = models.IntegerField()
    gad_question_5 = models.IntegerField()
    gad_question_6 = models.IntegerField()
    gad_question_7 = models.IntegerField()
    gad_total_score = models.IntegerField(editable=False)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate PHQ-9 total score
        self.phq_total_score = sum([
            self.phq_question_1 or 0,
            self.phq_question_2 or 0,
            self.phq_question_3 or 0,
            self.phq_question_4 or 0,
            self.phq_question_5 or 0,
            self.phq_question_6 or 0,
            self.phq_question_7 or 0,
            self.phq_question_8 or 0,
            self.phq_question_9 or 0
        ])

        # Calculate GAD-7 total score, treating None as 0
        self.gad_total_score = sum([
            self.gad_question_1 or 0,
            self.gad_question_2 or 0,
            self.gad_question_3 or 0,
            self.gad_question_4 or 0,
            self.gad_question_5 or 0,
            self.gad_question_6 or 0,
            self.gad_question_7 or 0
        ])

        # Call the original save method
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - PHQ: {self.phq_total_score}, GAD: {self.gad_total_score}"
