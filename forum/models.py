from django.db import models
from django.utils.text import slugify

class Question(models.Model):
    qid = models.AutoField(primary_key=True)    #question id.
    question_title = models.CharField(max_length=100)   
    question_text = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)   #date and time on which the question was posted.
    # date_modified = models.DateTimeField(auto_now=True)    #date and time on which the quetion was modified.
    posted_by = models.TextField(max_length=20)     #name of the questioner.
    # modified_by = models.TextField(max_length=20)   #name of the modifier of the question.
    # question_votes = models.IntegerField()     #votes, a question gets
    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question_title)
        super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
    aid = models.AutoField(primary_key=True)    #answer id.
    qid = models.ForeignKey(Question, on_delete=models.CASCADE)   #question id (associated with the answer).
    answer_text = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)   #date and time on which the answer was posted.
    # date_modified = models.DateTimeField(auto_now=True)     #date and time on which the answer was modified.
    posted_by = models.TextField(max_length=20)     #name of the answerer.
    # modified_by = models.TextField(max_length=20)   #name of the modifier of the answer.
    # answer_votes = models.IntegerField()     #votes, a answer gets