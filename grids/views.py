from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Grid
from .forms import GridForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def index(request):
    grids = Grid.objects.all()
    form = GridForm()
    return render(request, 'grids/index.html', {'grids': grids, 'form': form})

def save_grid(request):
    if request.method == 'POST':
        form = GridForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']

            if x < 0 or y < 0 or x + width > 800 or y + height > 600:
                return render(request, 'grids/index.html', {
                    'grids': Grid.objects.all(),
                    'form': form,
                    'error': 'Grid exceeds floorplan boundaries!'
                })

            if is_overlapping(x, y, width, height):
                return render(request, 'grids/index.html', {
                    'grids': Grid.objects.all(),
                    'form': form,
                    'error': 'Grid overlaps with existing one!'
                })

            form.save()
    return redirect('index')

@csrf_exempt
@require_POST
def update_grid(request, grid_id):
    try:
        grid = Grid.objects.get(pk=grid_id)
        data = json.loads(request.body)

        new_x = data.get('x', grid.x)
        new_y = data.get('y', grid.y)
        new_w = data.get('width', grid.width)
        new_h = data.get('height', grid.height)

        if is_overlapping(new_x, new_y, new_w, new_h, exclude_id=grid.id):
            return JsonResponse({'status': 'error', 'message': 'Overlap detected'}, status=400)

        grid.x = new_x
        grid.y = new_y
        grid.width = new_w
        grid.height = new_h
        grid.save()

        return JsonResponse({'status': 'success'})
    except Grid.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Grid not found'}, status=404)

def delete_grid(request, grid_id):
    try:
        grid = Grid.objects.get(pk=grid_id)
        grid.delete()
        return JsonResponse({'status': 'deleted'})
    except Grid.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Grid not found'}, status=404)

def is_overlapping(new_x, new_y, new_w, new_h, exclude_id=None):
    from django.db.models import Q
    overlapping_grids = Grid.objects.exclude(id=exclude_id).filter(
        Q(x__lt=new_x + new_w) & Q(x__gte=new_x - Grid.objects.values('width').first()['width']) &
        Q(y__lt=new_y + new_h) & Q(y__gte=new_y - Grid.objects.values('height').first()['height'])
    )

    for grid in overlapping_grids:
        if (new_x < grid.x + grid.width and new_x + new_w > grid.x and
            new_y < grid.y + grid.height and new_y + new_h > grid.y):
            return True
    return False

