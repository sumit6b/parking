from django.shortcuts import render

def parkingapp(request):
	context={}
	context["refrenceImageUrl"] = "/static/images/pngimages/base0.png"
	context["processedImageUrl"] = "/static/images/pngimages/base0.png"
	context["nextImageIndex"] = 1
	context["nextProcessedImageNumber"] = 1
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