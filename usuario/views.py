from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from usuario.models import Gasto, Jubilacion
from django.db.models import Sum
from django.contrib import messages
from .forms import GastoForm
from django.db.models import Q



class view_detalle(DetailView):
    model = Gasto
    template_name = "pages/detalle.html"


@login_required
def view_home(request):
    jubilacion = Jubilacion.objects.all()
    jubilacion_int = Jubilacion.objects.aggregate(total=Sum("total"))["total"]

    gastos2 = Gasto.objects.filter(cuenta='J')
    total_gastos2 = gastos2.aggregate(total=Sum("monto"))["total"]

    gastos = Gasto.objects.all()
    total_gastos = Gasto.objects.aggregate(total=Sum("monto"))["total"]

    if request.method == "POST":
        mes_seleccionado = request.POST.get("mes")

        return redirect("/home/{}".format(mes_seleccionado))

    if total_gastos == None:
        total_gastos = 0

    if total_gastos2 == None:
        total_gastos2 = 0

    if jubilacion_int == None:
        jubilacion_int = 0

    jubilacion_restante = jubilacion_int - total_gastos2
    gastos_jubilacion = total_gastos2
    ajenos = total_gastos - total_gastos2


    return render(
        request,
        "templates/pages/home.html",
        {
            "gastos_total": total_gastos,
            "gastos": gastos,
            "jub_mes": jubilacion_int,
            "jubilacion": gastos_jubilacion,
            "restante": jubilacion_restante,
            "ajenos":ajenos
        },
    )


@login_required
def view_home2(request, mes):
    gastos_mes = Gasto.objects.filter(mes=mes)
    total_gastos_mes = gastos_mes.aggregate(total=Sum("monto"))["total"]

    gastos_mes2 = Gasto.objects.filter(Q(mes=mes) & Q(cuenta='J'))
    total_gastos_mes2 = gastos_mes2.aggregate(total=Sum("monto"))["total"]

    jubilacion = Jubilacion.objects.all()
    jubilacion_mes = Jubilacion.objects.filter(mes=mes)
    jubilacion_int = jubilacion_mes.aggregate(total=Sum("total"))["total"]

    if request.method == "POST":
        mes_seleccionado = request.POST.get("mes")

        return redirect("/home/{}".format(mes_seleccionado))

    if total_gastos_mes == None:
        total_gastos_mes = 0

    if total_gastos_mes2 == None:
        total_gastos_mes = 0

    if jubilacion_int == None:
        jubilacion_int = 0

    restante = jubilacion_int - total_gastos_mes2
    gastos_jubilacion = total_gastos_mes2
    ajenos = total_gastos_mes - total_gastos_mes2

    return render(
        request,
        "templates/pages/home2.html",
        {
            "gastos_total": total_gastos_mes,
            "gastos": gastos_mes,
            "jubilacion": jubilacion,
            "restante": restante,
            "jub_mes": jubilacion_int,
            "gasto_mes": mes,
            "gasto2": gastos_mes2,
            "ajenos": ajenos,
            "gastos_jubilacion": gastos_jubilacion
        },
    )

@login_required
def eliminar_gasto(request, pk):
    gasto = Gasto.objects.get(pk=pk)
    gasto.delete()

    return redirect("home")


class editar_gasto(UpdateView):
    template_name = "editar_gasto.html"
    queryset = Gasto.objects.all()
    fields = ["nombre", "monto", "categoria", "cuenta", "mes", "comprobante"]
    success_url = "./"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "¡Se ha editado correctamente!")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "¡Ha ocurrido un error al editer el gasto!")
        return response


class agregar_gasto(CreateView):
    template_name = "agregar_gasto.html"
    queryset = Gasto.objects.all()
    fields = ["nombre", "monto", "categoria", "cuenta", "mes", "comprobante"]
    success_url = "./"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "¡Se ha agregado correctamente!")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "¡Ha ocurrido un error al agregar el gasto!")
        return response


def error_404(request, exception):
    return render(request, 'erorrs/404.html', status=404)
