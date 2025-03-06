from django.http.response import HttpResponse, JsonResponse, FileResponse
import os
product = {
    "name": "example",
    "quantity": 10,
    "price":3000
}
def info_response(request):
    return JsonResponse(product)
def terms_response(request):
    file = os.path.join("./a.pdf")
    return FileResponse(open(file,"rb"), as_attachment=True)
def buy_response(request, quantity:int = 0):
    if quantity>product["quantity"]:
        return HttpResponse(f"not enough product(max: {product['quantity']})")
    else:
        product["quantity"] -= quantity
        return HttpResponse(f"final price: {quantity * product['price']}$ for {quantity} products, remaining: {product['quantity']}")
    