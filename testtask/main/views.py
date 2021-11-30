import io, csv
from django.shortcuts import render
from .models import Csv
from django.core.files.storage import FileSystemStorage


def index(request):
    datatest = Csv.objects.values()
    uploaded_file = 'text.csv'
    if request.method == 'POST':
        if request.FILES['document'].content_type != 'application/vnd.ms-excel':
            return render(request, 'main/index.html', {'errorMessage': 'Error, this is not a .csv file'})
        else:
            fs = FileSystemStorage()
            fs.save(request.FILES['document'].name, request.FILES['document'])
            uploaded_file = request.FILES['document'].name
    filePath = 'media/' + uploaded_file
    f = io.open(filePath, 'r', encoding="UTF-8")
    contents = f.readlines()
    colums = len(contents)
    for i in range(colums):
        culumsArr = contents[i].split(';')
        _, created = Csv.objects.get_or_create(
                    code = culumsArr[0],
                    Name = culumsArr[1],
                    Lvl1 = culumsArr[2],
                    Lvl2 = culumsArr[3],
                    Lvl3 = culumsArr[4],
                    Cost = culumsArr[5],
                    CostSP = culumsArr[6],
                    Count = culumsArr[7],
                    FieldProp = culumsArr[8],
                    Purch = culumsArr[9],
                    Unit = culumsArr[10],
                    Img = culumsArr[11],
                    Display = culumsArr[12],
                    Desc = culumsArr[13],
                    )
    return render(request, 'main/index.html', {'datatest': datatest})

