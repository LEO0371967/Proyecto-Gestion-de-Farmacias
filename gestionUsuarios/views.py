from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# vistas basadas en clases
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, View

from gestionUsuarios.models import Usuarios, Recetas

from gestionUsuarios.forms import FormularioCrearUsuario, Formulario_nueva_receta, FormularioEditarUsuario, Formulario_receta_usuario




class ListaDeUsuarios(ListView):
        model = Usuarios

        template_name = 'lista_de_usuarios.html'
        
        def get_queryset(self) :
                #return self.objects.filter(usuario_activo=True)
                #print(self.model.objects.filter(usuario_activo=True))
                return self.model.objects.filter(usuario_activo=True)

class RegistrarUsuario(CreateView):
        model = Usuarios
        form_class = FormularioCrearUsuario

        template_name = 'registrar_usuario.html'
        success_url = reverse_lazy('lista_de_usuarios')






# =======================================================================
# Editar Usuario ===========================================================
# =======================================================================
class EditarUsuario(UpdateView):
        model = Usuarios
        form_class = FormularioEditarUsuario

        template_name = 'editar_usuario.html'
        success_url = reverse_lazy('lista_de_usuarios')






# =======================================================================
# Listar Recetas =========================================================
# ======================================================================
class ListarRecetas(View):
    model = Recetas
    form_class = Formulario_nueva_receta
    template_name = 'recetas.html'
    #busqueda_por_farmacias = Lotes.objects.filter(ubicacion="miFarmacia")
    #busqueda_por_farmacias = Lotes.objects.filter(ubicacion__icontains="miFarmacia")

    # este metodo devuelve la consulta principal de la vista
    def get_queryset(self):
        return Recetas.objects.all()
    
    # este metodo devuelve el diccionario de contexto(los datos) que va a ser enviado al template
    def get_context_data(self, **kwargs):
        diccionario_de_contexto = {}
        diccionario_de_contexto["recetas_list"] = self.get_queryset()

        #formulario_nuevo_stock
        diccionario_de_contexto["formulario_nueva_receta"] = self.form_class
        return diccionario_de_contexto
    
    # este metodo devuelve toda la informacion cuando se hagan este tipo de peticiones
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    

    def post(self,request, *args, **kwargs):
        formulario_nueva_receta = self.form_class(request.POST)

        if formulario_nueva_receta.is_valid():
            formulario_nueva_receta.save()
            return redirect('recetas')
        


# =======================================================================
# Editar Receta ===========================================================
# =======================================================================
class EditarReceta(UpdateView):
    model = Recetas
    form_class = Formulario_nueva_receta
    template_name = 'editar_receta.html'

    success_url = reverse_lazy('recetas')



class UsuarioReceta(ListView):

    #model = Usuarios
    model = Recetas
    form_class = Formulario_receta_usuario
    template_name = 'mis_recetas.html'


    def get_queryset(self):
        cedula_del_user= self.request.user.cedula_de_identidad
        queryset_mis_receta = Recetas.objects.filter(paciente=cedula_del_user)
        mi_receta = queryset_mis_receta[0]
        return  queryset_mis_receta


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cedula_del_user = self.request.user.cedula_de_identidad

        #context['Recetas'] = Recetas.objects.all()
        #context['Usuarios'] = str(type(Usuarios.objects.filter(Usuarios='Nombre')))

       

       


        return context         


