from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     choice = question.choice_set.get(pk = request.POST['choice'])
    # except (Choice.DoesNotExist, KeyError):
    #     context = {
    #         "question": question, 
    #         "error_message": "please select a choice"
    #     }
    #     return render(request, "polls/detail.html", context)
    # else:
    #     choice.votes = F("votes") + 1
    #     choice.save()
    # return HttpResponseRedirect(reverse("polls:results", args=[question.pk]))
    return HttpResponse("hello")

# Create your views here.
