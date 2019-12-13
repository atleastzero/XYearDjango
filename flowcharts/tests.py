from django.test import TestCase
from django.urls import reverse

from .models import Flowchart

def create_flowchart(name):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Flowchart.objects.create(name=name)

class FlowchartListViewTests(TestCase):
    def test_no_flowcharts(self):
        response = self.client.get(reverse('flowcharts:flowchart-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No flowcharts to display.")

class FlowchartDetailViewTests(TestCase):
    def test_flowchart(self):
        flowchart = create_flowchart("Hello")
        url = reverse('flowcharts:flowchart-detail', args=(flowchart.slug,))
        response = self.client.get(url)
        self.assertContains(response, flowchart.name)

    def test_wrong_slug(self):
        url = reverse('flowcharts:flowchart-detail', args=(52,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)