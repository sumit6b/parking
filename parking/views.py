from django.shortcuts import render

def parkingapp(request):
	context={}
	import pdb;pdb.set_trace()
	

	if request.GET and request.GET.get("nextImageIndex"):
		n = int(request.GET.get("nextImageindex"))%22
		context["refrenceImageUrl"] = "/static/images/pngimages/base"+str(n)+".png"
		context["processedImageUrl"] = "/static/images/processedimages/base"+str(n)+".png"

		context["nextImageindex"] = int(request.GET.get('nextImageindex','1')) + 1
		if context["nextImageindex"] > 22:
			context["nextImageindex"] = 0
		context['activetabid'] = request.GET.get('activetabid','tab1')
	else:
		context["refrenceImageUrl"] = "/static/images/pngimages/base0.png"
		context["processedImageUrl"] = "/static/images/processedimages/base0.png"
		context["nextImageIndex"] = 1
		context["activetabid"] = 'tab1'
	return render(request, "home.html", context)


def refrence_image(request):
	next_image_index = request.GET.get("nextImageindex")
	next_processed_imagenumber = request.GET.get("nextprocessedimagenumber")
	context = {}
	if next_image_index and next_processed_imagenumber:
		context["nextImageindex"] = next_image_index + 1
		context["nextprocessedimagenumber"] = next_processed_imagenumber
		context["refrenceImageUrl"] = "static/images/pngimages/base"+next_image_index+".png"
		context["processedImageUrl"] = "static/images/processedimages/"+str(next_image_index)+"/base"+processed_image_index+".png"
	return HttpResponse(json.dumps(context), content_type="application/json")


def processed_image(request):
	next_image_index = request.GET.get("nextImageindex")
	next_processed_imagenumber = request.GET.get("nextprocessedimagenumber")
	context = {}
	if next_image_index and next_processed_imagenumber:
		context["nextImageindex"] = next_image_index
		context["nextprocessedimagenumber"] = next_processed_imagenumber + 1
		context["refrenceImageUrl"] = "static/images/pngimages/base"+image_index+".png"
		context["processedImageUrl"] = "static/images/processedimages/"+str(next_image_index)+"/base"+image_index+".png"
	return HttpResponse(json.dumps(context), content_type="application/json")