from django.test import TestCase
from django.utils.timezone import now
from promises.models import Promise, Category
from promises.queryset import PromiseSummary
from popit.models import Person as PopitPerson, ApiInstance
from popolo.models import Person
from django.core.urlresolvers import reverse
from django.test import Client
from taggit.models import Tag
from constance import config
from django.contrib.staticfiles import finders

nownow = now()

class TemplateSelectorTestCase(TestCase):
    def setUp(self):
    	pass

    def test_home_returns_base_according_to_config(self):
        '''Home returns base theme according to config'''
        config.CURRENT_THEME = 'base'
        url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        self.assertTemplateUsed(response, 'base.html')

    def atest_get_base_if_template_not_in_theme(self):
    	'''If a certain template cannot be found uses the one in base'''
    	config.CURRENT_THEME = 'test'
    	url = reverse('promises_home')
        c = Client()
        response = c.get(url)
        # template = response.resolve_template(response.template_name)
        # print template
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.rendered_content, "testest")

    def test_static_finder(self):
    	'''Gets correctly the static files'''
    	result = finders.find('images/favicon.ico')
    	self.assertIsNotNone(result)

