from django import forms
from .models import User







class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].disabled = True   #دیگر نمیتوان نام کاربری را تغییر داد
        self.fields['username'].help_text = "سلامممم"   #تعیین کردن هلپ تکست راهنما دلخواه
        #self.fields['username'].help_text = None   حذف کردن هلپ تکست راهنما 
        self.fields['email'].disabled = True
        self.fields['email'].help_text = "لطفا از ایمیل معتبر استفاده کنید"
        self.fields['special_user'].disabled = True
        self.fields['is_author'].disabled = True 
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','special_user','is_author']


