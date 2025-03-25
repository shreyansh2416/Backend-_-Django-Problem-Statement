from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.core.paginator import Paginator


@login_required
def create_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.customer = request.user
            new_request.save()
            return redirect("my-requests")
    else:
        form = ServiceRequestForm()
    return render(
        request, "create_requests.html", {"form": form}
    )  # Updated template name


@login_required
def my_requests(request):
    status_filter = request.GET.get("status", None)
    requests = ServiceRequest.objects.filter(customer=request.user)
    if status_filter:
        requests = requests.filter(status=status_filter)
    paginator = Paginator(requests, 5)  # Show 5 requests per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "my_requests.html",
        {"page_obj": page_obj, "status_filter": status_filter},
    )
