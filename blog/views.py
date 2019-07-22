from django.shortcuts import render

def principal(request):
    return render(request, 'blog/principal.html', {})

def prueba(request):
	return render(request, 'blog/prueba.html')

def defensora(request):
	return render(request, 'blog/defensora.html')

def defensoria(request):
	return render(request, 'blog/defensoria.html')

def derechos(request):
	return render(request, 'blog/derechos.html')

def quedicelaaudiencia(request):
	return render(request, 'blog/quedicelaaudiencia.html')

def comunicate(request):
	return render(request, 'blog/comunicate.html')

def interes(request):
	return render(request, 'blog/interes.html')

def normatividad(request):
	return render(request, 'blog/normatividad.html')


#def defensora(request):
	#return render(request, 'blog/defensora.html', {})
   
# Create your views here.
