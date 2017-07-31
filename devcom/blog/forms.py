from django import forms

class DpForm(forms.Form):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  dp=models.ImageField(upload_to="media/dp")
