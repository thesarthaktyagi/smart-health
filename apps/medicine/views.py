from django.shortcuts import render, get_object_or_404
from .models import Medicine, Order
from apps.hospital.models import Hospital


def showMedicines(request, hospital_pk):
    medicines = Medicine.objects.filter(hospital__pk=hospital_pk)
    hospital = get_object_or_404(Hospital, pk=hospital_pk)
    return render(request, 'medicine/medicines.html', {'medicines': medicines, 'hospital': hospital})


def order(request, hospital_pk, medicine_pk):
    medicine = get_object_or_404(Medicine, pk=medicine_pk)
    hospital = get_object_or_404(Hospital, pk=hospital_pk)
    return render(request, 'medicine/order.html', {'medicine': medicine, 'hospital': hospital})


def postorder(request, hospital_pk, medicine_pk):
    medicine = get_object_or_404(Medicine, pk=medicine_pk)
    hospital = get_object_or_404(Hospital, pk=hospital_pk)
    if request.method == 'POST':
        name = medicine.name
        hospital = hospital.name
        quantity = request.POST.get('quantity')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        prescription = request.POST.get('url')

        # creating object
        entry = Order()
        entry.name = name
        entry.hospital = hospital
        entry.quantity = quantity
        entry.address = address
        entry.mobile = mobile
        entry.prescription = prescription
        entry.save()
    return render(request, 'medicine/post-order.html', {'medicine': medicine, 'hospital': hospital})
