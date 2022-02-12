from django.db import models
from ckeditor.fields import RichTextField

def get_age_str(a,b):
    if b >= 11 and b <= 20:
        return '{age1}-{age2} лет'.format(age1=a,age2=b)
    elif (b%10 >= 5 and b%10) <=9 or b%10 == 0:
        return '{age1}-{age2} лет'.format(age1=a,age2=b)
    elif b%10 >=2 and b%10 <=4:
        return '{age1}-{age2} года'.format(age1=a,age2=b)
    elif b%10 == 1:
        return '{age1}-{age2} год'.format(age1=a,age2=b)

def get_count_str(a):
    if a >= 11 and a <= 20:
        return '{count} уроков'.format(count=a)
    elif (a%10 >= 5 and a%10 <=9) or a%10 == 0:
        return '{count} уроков'.format(count=a)
    elif a%10 >=2 and a%10 <=4:
        return '{count} урока'.format(count=a)
    elif a%10 == 1:
        return '{count} урок'.format(count=a)

class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    age = models.CharField(max_length=30, verbose_name='Возраст')
    lweek = models.IntegerField(verbose_name='Занятий в неделю')
    lall = models.IntegerField(verbose_name='Всего занятий')
    image = models.ImageField(upload_to='media', verbose_name='Картинка')
    description = RichTextField(verbose_name='Описание')
    youtube = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Ссылка на YouTube (если есть)')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name

    def get_age(self):
        try:
            if self.age[0] == 'y':
                if '-' in self.age:
                    return get_age_str(self.age[1::].split('-')[0],int(self.age[1::].split('-')[1]))
                else:
                    return '{age}+'.format(age=self.age[1::])
            elif self.age[0] == 'c':
                return self.age[1::]
            else:
                return 'Error'
        except:
            return 'Error'

    def get_count(self):
        try:
            return [get_count_str(int(self.lweek)), get_count_str(int(self.lall))]
        except:
            return 'Error'