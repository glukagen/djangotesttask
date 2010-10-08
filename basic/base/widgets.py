from django import forms


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('/media/datepicker.css',)
        }
        js = (
            '/media/ui.datepicker.js',
            '/media/ui.datepicker.init.js'
        )

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(
            attrs={'class': 'vDateField', 'size': '10'})
