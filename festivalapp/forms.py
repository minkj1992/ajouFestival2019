from django import forms
from .models import Pub

class PubForm(forms.ModelForm):
    class Meta:
        model = Pub
        fields = '__all__'  
        
    def __init__(self, *args, **kwargs):
        super(PubForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "부스 이름 "
        self.fields['description'].label = "간단한 부스 소개와 메뉴 "
        self.fields['section'].label = "구역"
        self.fields['location'].label = "위치 "
        self.fields['time'].label = "주간/야간 "
        self.fields['date'].label = "날짜 " #중복선택가능
        self.fields['image_booth'].label = "부스 포스터(사진) "

