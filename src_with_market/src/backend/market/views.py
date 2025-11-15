from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from .models import Product, Category

def health(request):
    return JsonResponse({"ok": True, "app": "market"})

def products(request):
    data = [
        {
            "id": p.id,
            "title": p.title,
            "slug": p.slug,
            "category": p.category.name,
            "created_at": p.created_at.isoformat(),
        }
        for p in Product.objects.select_related("category").order_by("-created_at")[:50]
    ]
    return JsonResponse({"results": data})

@require_http_methods(["GET"])
def categories(request):
    data = [model_to_dict(c, fields=["id", "name", "slug"]) for c in Category.objects.order_by("name")]
    return JsonResponse({"results": data})
