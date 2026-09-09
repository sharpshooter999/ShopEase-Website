from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from .models import Contact

from django.shortcuts import render
from .models import Product

import hashlib
from django.shortcuts import render, redirect
# from .forms import ContactForm

from django.views.decorators.csrf import csrf_exempt
# from pymongo import MongoClient
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
import os
import uuid

from django.shortcuts import render, get_object_or_404
  # Assuming you have a Product model

import random
from django.http import JsonResponse
from django.conf import settings
from django.db import transaction
import json
import re
from io import BytesIO
from datetime import datetime, timedelta
# from datetime import datetime
# from twilio.rest import Client

def project2_view(request):
    return render(request, 'keyur/project2.html')

def admin(request):
    return render(request, 'keyur/admin.html')

def contactus(request):
    return render(request, 'keyur/contactus.html')

def user(request):
    if "user_id" not in request.session:
        return redirect("login")

    user_id = request.session["user_id"]
    user_data = settings.USERS_COLLECTION.find_one({"_id": ObjectId(user_id)}) or {}

    if request.method == "POST":
        profile_photo = request.FILES.get("profile_photo")
        if not profile_photo:
            messages.error(request, "Please choose a photo to upload.")
        elif profile_photo.content_type not in {"image/jpeg", "image/png", "image/webp"}:
            messages.error(request, "Please upload a JPG, PNG, or WebP image.")
        elif profile_photo.size > 5 * 1024 * 1024:
            messages.error(request, "Your profile photo must be smaller than 5 MB.")
        else:
            filename = f"profile_photos/{user_id}_{uuid.uuid4().hex}{os.path.splitext(profile_photo.name)[1].lower()}"
            photo_path = default_storage.save(filename, profile_photo)
            settings.USERS_COLLECTION.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {"profile_photo": photo_path}},
            )
            user_data["profile_photo"] = photo_path
            messages.success(request, "Profile photo updated.")

    address_data = settings.DELIVERY_COLLECTION.find_one(
        {"user_id": user_id},
        sort=[("_id", -1)]
    )
    return render(request, "keyur/user.html", {
        "user_data": user_data,
        "profile_photo_url": settings.MEDIA_URL + user_data["profile_photo"] if user_data.get("profile_photo") else "",
        "address_data": address_data or {},
    })

def frontend(request):
    return render(request, "keyur/frontend.html", {"username": request.session.get("username")})


def normalize_product_text(value):
    if not value:
        return ""
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def get_product_family_key(value):
    text = normalize_product_text(value)
    if not text:
        return "general"

    if any(word in text for word in ["watch", "wrist", "timepiece", "strap"]):
        return "watch"
    if any(word in text for word in ["shoe", "sneaker", "running", "boots"]):
        return "shoe"
    if any(word in text for word in ["shirt", "tshirt", "t-shirt", "tee", "top"]):
        return "shirt"
    if any(word in text for word in ["dress", "women", "female", "gown"]):
        return "dress"
    if any(word in text for word in ["combo", "fashion", "cloth", "jacket", "coat"]):
        return "fashion"
    if any(word in text for word in ["mens", "men", "male"]):
        return "mens"
    return "general"


def get_related_products(product):
    return list(
        product.recommended_products
        .exclude(id=product.id)
        .all()
    )

# def shop(request):
#     return render(request, 'keyur/shop.html')
def shop(request):
    products = Product.objects.all().order_by('id')

    return render(request, 'keyur/shop.html', {
        'products': products,
    })

# MONGO_CLIENT = settings.client
# db = settings.db
# collection = db["contacts"]  # Collection where data will be stored

# @csrf_exempt  # Disable CSRF for testing (Enable in production with CSRF tokens)
# def contactus(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             data = {
#                 "first_name": form.cleaned_data["first_name"],
#                 "last_name": form.cleaned_data["last_name"],
#                 "email": form.cleaned_data["email"],
#                 "mobile": form.cleaned_data["mobile"],
#                 "message": form.cleaned_data["message"],
#             }
#             collection.insert_one(data)  # Save data to MongoDB
#             return redirect("keyur/contactus")  # Redirect to a success page

#     else:
#         form = ContactForm()

#     return render(request, "keyur/contactus.html", {"form": form})

def cart(request):
    return render(request, 'keyur/cart.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = get_related_products(product)
    return render(request, 'keyur/product_detail.html', {
        'product': product,
        'related_products': related_products,
        'show_recommendations': bool(related_products),
    })

def product1(request):
    return render(request, 'keyur/product1.html')

def product2(request):
    return render(request, 'keyur/product2.html')

def product3(request):
    return render(request, 'keyur/product3.html')

def product4(request):
    return render(request, 'keyur/product4.html')

def product5(request):
    return render(request, 'keyur/product5.html')

def product6(request):
    return render(request, 'keyur/product6.html')

def product7(request):
    return render(request, 'keyur/product7.html')

def product8(request):
    return render(request, 'keyur/product8.html')

def product9(request):
    return render(request, 'keyur/product9.html')

def product10(request):
    return render(request, 'keyur/product10.html')

def product11(request):
    return render(request, 'keyur/product11.html')

def product12(request):
    return render(request, 'keyur/product12.html')

def product13(request):
    return render(request, 'keyur/product13.html')

def product14(request):
    return render(request, 'keyur/product14.html')

def product15(request):
    return render(request, 'keyur/product15.html')

def product16(request):
    return render(request, 'keyur/product16.html')

def product17(request):
    return render(request, 'keyur/product17.html')

def product18(request):
    return render(request, 'keyur/product18.html')

def product19(request):
    return render(request, 'keyur/product19.html')

def product20(request):
    return render(request, 'keyur/product20.html')

def product21(request):
    return render(request, 'keyur/product21.html')

def product22(request):
    return render(request, 'keyur/product22.html')

def product23(request):
    return render(request, 'keyur/product23.html')

def product24(request):
    return render(request, 'keyur/product24.html')

def address(request):
    if "user_id" not in request.session:
        return redirect("login")

    user_id = request.session["user_id"]
    addresses = list(settings.DELIVERY_COLLECTION.find(
        {"user_id": user_id}
    ).sort("created_at", -1))
    for saved_address in addresses:
        saved_address["id"] = str(saved_address["_id"])

    selected_address_id = request.GET.get("address_id") or request.session.get("selected_address_id")
    selected_address = next(
        (item for item in addresses if item["id"] == selected_address_id),
        addresses[0] if addresses else {},
    )
    if selected_address:
        request.session["selected_address_id"] = selected_address["id"]

    edit_id = request.GET.get("edit")
    edit_address = next(
        (item for item in addresses if item["id"] == edit_id),
        {},
    )
    return render(request, "keyur/Address.html", {
        "addresses": addresses,
        "address_data": edit_address,
        "selected_address_id": selected_address.get("id", ""),
    })

def payment(request):
    if "user_id" not in request.session:
        return redirect("login")

    selected_address_id = request.GET.get("address_id") or request.session.get("selected_address_id")
    selected_address = {}
    if selected_address_id:
        selected_address = settings.DELIVERY_COLLECTION.find_one({
            "_id": ObjectId(selected_address_id),
            "user_id": request.session["user_id"],
        }) or {}
        if selected_address:
            request.session["selected_address_id"] = selected_address_id

    if request.method == "POST":
        payment_method = request.POST.get("payment_method", "").strip()
        coupon_code = request.POST.get("applied_coupon_code", "").strip().upper()
        allowed_methods = {"card", "upi", "net_banking", "cod"}
        if payment_method not in allowed_methods:
            messages.error(request, "Please select a payment method.")
        else:
            try:
                items = json.loads(request.POST.get("cart_items", "[]"))
            except (TypeError, ValueError):
                items = []

            if not items:
                messages.error(request, "Your cart is empty.")
                return redirect("cart")

            coupons = {
                "SHOPEASE10": ("percent", 10),
                "WELCOME5": ("percent", 5),
                "SAVE200": ("flat", 200),
            }
            if coupon_code and coupon_code not in coupons:
                messages.error(request, "That coupon code is not valid.")
                return render(request, "keyur/payment.html", {
                    "selected_address": selected_address,
                    "coupon_code": coupon_code,
                })

            quantities = {}
            cart_lines = []
            for item in items:
                try:
                    product_id = int(item.get("product_id"))
                except (TypeError, ValueError):
                    product_id = None
                if product_id is None:
                    messages.error(request, "Your cart contains an outdated product. Please add it again.")
                    return redirect("cart")
                try:
                    quantity = max(1, int(item.get("quantity", 1)))
                except (TypeError, ValueError):
                    quantity = 1
                cart_lines.append({
                    "product_id": product_id,
                    "size": str(item.get("size", "One Size"))[:20],
                    "quantity": quantity,
                })
                quantities[product_id] = quantities.get(product_id, 0) + quantity

            order_items = []
            total = 0
            with transaction.atomic():
                products = {
                    product.id: product
                    for product in Product.objects.select_for_update().filter(id__in=quantities)
                }
                for product_id, quantity in quantities.items():
                    product = products.get(product_id)
                    if not product or product.stock < quantity:
                        product_name = product.name if product else "That product"
                        available = product.stock if product else 0
                        messages.error(
                            request,
                            f"{product_name} has only {available} left in stock. Please update your cart.",
                        )
                        return redirect("cart")

                for product_id, quantity in quantities.items():
                    product = products[product_id]
                    product.stock -= quantity
                    product.save(update_fields=["stock"])

                for line in cart_lines:
                    product = products[line["product_id"]]
                    price = float(product.price)
                    order_items.append({
                        "product_id": product.id,
                        "name": product.name,
                        "price": price,
                        "quantity": line["quantity"],
                        "size": line["size"],
                        "image": product.image.url if product.image else "",
                    })
                    total += price * line["quantity"]

            discount = 0
            if coupon_code:
                coupon = coupons.get(coupon_code)
                if not coupon:
                    messages.error(request, "That coupon code is not valid.")
                    return render(request, "keyur/payment.html", {
                        "selected_address": selected_address,
                        "coupon_code": coupon_code,
                    })
                discount = total * coupon[1] / 100 if coupon[0] == "percent" else min(total, coupon[1])
            final_total = max(total - discount, 0)

            order = {
                "user_id": request.session["user_id"],
                "items": order_items,
                "subtotal": total,
                "discount": discount,
                "total": final_total,
                "coupon_code": coupon_code,
                "payment_method": payment_method,
                "payment_status": "Paid",
                "address": selected_address,
                "status": "Processing",
                "tracking_number": f"SE{datetime.utcnow().strftime('%Y%m%d')}{uuid.uuid4().hex[:6].upper()}",
                "expected_delivery": datetime.utcnow() + timedelta(days=5),
                "created_at": datetime.utcnow(),
            }
            saved_order = settings.ORDERS_COLLECTION.insert_one(order)
            order_id = str(saved_order.inserted_id)
            messages.success(request, "Payment method selected successfully.")
            return render(request, "keyur/payment.html", {
                "selected_method": payment_method,
                "selected_address": selected_address,
                "coupon_code": coupon_code,
                "discount": discount,
                "total": final_total,
                "order_id": order_id,
                "cart_storage_key": f"cart_{request.session['user_id']}",
                "payment_complete": True,
            })

    return render(request, "keyur/payment.html", {
        "selected_address": selected_address,
    })


def orders(request):
    if "user_id" not in request.session:
        return redirect("login")

    user_orders = list(settings.ORDERS_COLLECTION.find(
        {"user_id": request.session["user_id"]}
    ).sort("created_at", -1))
    for order in user_orders:
        order["id"] = str(order["_id"])
        returned_items = set(order.get("returned_items", []))
        order["items"] = [
            {**item, "return_requested": index in returned_items}
            for index, item in enumerate(order.get("items", []))
        ]
    return render(request, "keyur/orders.html", {"orders": user_orders})


def cancel_order(request, order_id):
    if "user_id" not in request.session:
        return redirect("login")

    if request.method == "POST":
        try:
            result = settings.ORDERS_COLLECTION.update_one(
                {
                    "_id": ObjectId(order_id),
                    "user_id": request.session["user_id"],
                    "status": {"$in": ["Processing", "Packed", "Shipped", "Out for delivery"]},
                },
                {"$set": {"status": "Cancelled", "cancelled_at": datetime.utcnow()}},
            )
        except Exception:
            result = None
        messages.success(request, "Order cancelled successfully." if result and result.modified_count else "This order can no longer be cancelled.")
    return redirect("orders")


def return_order_item(request, order_id, item_index):
    if "user_id" not in request.session:
        return redirect("login")

    if request.method == "POST":
        try:
            order = settings.ORDERS_COLLECTION.find_one({
                "_id": ObjectId(order_id),
                "user_id": request.session["user_id"],
            })
            if order and order.get("status") != "Cancelled":
                items = order.get("items", [])
                returned_items = set(order.get("returned_items", []))
                if 0 <= item_index < len(items) and item_index not in returned_items:
                    returned_items.add(item_index)
                    settings.ORDERS_COLLECTION.update_one(
                        {"_id": ObjectId(order_id), "user_id": request.session["user_id"]},
                        {"$set": {"returned_items": list(returned_items), "status": "Return requested", "return_requested_at": datetime.utcnow()}},
                    )
                    messages.success(request, f"Return requested for {items[item_index].get('name', 'product')}.")
                else:
                    messages.info(request, "This product has already been requested for return.")
            else:
                messages.error(request, "This order is not eligible for a return.")
        except Exception:
            messages.error(request, "We could not process the return request.")
    return redirect("orders")


def track_order(request, order_id):
    if "user_id" not in request.session:
        return redirect("login")

    try:
        order = settings.ORDERS_COLLECTION.find_one({
            "_id": ObjectId(order_id),
            "user_id": request.session["user_id"],
        })
    except Exception:
        order = None
    if not order:
        return HttpResponse("Order not found", status=404)

    order["id"] = str(order["_id"])
    tracking_steps = ["Processing", "Packed", "Shipped", "Out for delivery", "Delivered"]
    current_step = tracking_steps.index(order.get("status", "Processing")) if order.get("status") in tracking_steps else 0
    return render(request, "keyur/track_order.html", {
        "order": order,
        "tracking_steps": tracking_steps,
        "current_step": current_step,
    })


def download_invoice(request, order_id):
    if "user_id" not in request.session:
        return redirect("login")

    try:
        order = settings.ORDERS_COLLECTION.find_one({
            "_id": ObjectId(order_id),
            "user_id": request.session["user_id"],
        })
    except Exception:
        order = None
    if not order:
        return HttpResponse("Order not found", status=404)

    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 52
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, y, "SHOPEASE - INVOICE")
    pdf.setStrokeColor(colors.HexColor("#e36f4d"))
    pdf.setLineWidth(2)
    pdf.line(50, y - 10, width - 50, y - 10)
    y -= 34
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, y, f"Order ID: {order_id}")
    created_at = order.get("created_at")
    invoice_date = created_at.strftime("%d %b %Y") if created_at else datetime.utcnow().strftime("%d %b %Y")
    pdf.drawRightString(width - 50, y, f"Invoice date: {invoice_date}")
    y -= 16
    pdf.drawString(50, y, f"Payment: {order.get('payment_method', '').replace('_', ' ').title()} ({order.get('payment_status', 'Paid')})")
    y -= 30
    address_data = order.get("address", {})
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(50, y, "Bill to / Delivery address")
    y -= 16
    pdf.setFont("Helvetica", 10)
    address_line = f"{address_data.get('address', '')}, {address_data.get('city', '')}, {address_data.get('state', '')} {address_data.get('zip_code', '')}, {address_data.get('country', '')}"
    for line in [address_data.get("full_name", ""), address_line, address_data.get("phone", ""), address_data.get("email", "")]:
        pdf.drawString(50, y, line[:110])
        y -= 14
    y -= 16
    pdf.setFillColor(colors.HexColor("#f3f3f0"))
    pdf.rect(50, y - 6, width - 100, 22, fill=1, stroke=0)
    pdf.setFillColor(colors.black)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(60, y, "Item")
    pdf.drawRightString(width - 60, y, "Amount")
    y -= 26
    pdf.setFont("Helvetica", 10)
    for item in order.get("items", []):
        pdf.drawString(60, y, item.get("name", "Product")[:75])
        pdf.drawRightString(width - 60, y, f"Rs. {float(item.get('price', 0)):.2f}")
        pdf.setStrokeColor(colors.HexColor("#dddddd"))
        pdf.line(60, y - 6, width - 60, y - 6)
        y -= 16
    y -= 12
    pdf.setFont("Helvetica", 10)
    pdf.drawRightString(width - 150, y, "Subtotal")
    pdf.drawRightString(width - 60, y, f"Rs. {float(order.get('subtotal', order.get('total', 0))):.2f}")
    y -= 20
    if float(order.get("discount", 0)):
        pdf.setFont("Helvetica", 10)
        pdf.setFillColor(colors.HexColor("#2f8f46"))
        pdf.drawRightString(width - 150, y, f"Coupon ({order.get('coupon_code', '')})")
        pdf.drawRightString(width - 60, y, f"- Rs. {float(order.get('discount', 0)):.2f}")
        y -= 20
        pdf.setFillColor(colors.black)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawRightString(width - 150, y, "Total")
    pdf.drawRightString(width - 60, y, f"Rs. {float(order.get('total', 0)):.2f}")
    y -= 34
    pdf.setFont("Helvetica-Oblique", 9)
    pdf.setFillColor(colors.HexColor("#666666"))
    pdf.drawString(50, y, "Thank you for shopping with ShopEase.")
    pdf.save()
    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="invoice-{order_id}.pdf"'
    return response

from django.shortcuts import render, get_object_or_404
from .models import Product  # Import your Product model

# from .database import users_collection  # Use absolute import






def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hashing password for security

        users_collection = settings.USERS_COLLECTION

        # Check if user already exists
        if users_collection.find_one({"email": email}):
            messages.error(request, "Email already exists!")
            return redirect("register")

        # Insert user data into MongoDB
        user_data = {
            "username": username,
            "email": email,
            "password": hashed_password,  # Store hashed password
        }
        users_collection.insert_one(user_data)
        messages.success(request, "Registration successful! You can now log in.")
        return redirect("login")
    
    return render(request, "keyur/register.html")
     

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash password

        users_collection = settings.USERS_COLLECTION

        user = users_collection.find_one({"email": email, "password": hashed_password})

        if user:
            request.session["user_id"] = str(user["_id"])  # Store user ID in session
            request.session["username"] = user["username"]
            request.session["email"] = user.get("email", "")
            request.session["phone"] = user.get("phone", "")
            return redirect("frontend")  # Redirect to a dashboard or home page
        else:
            messages.error(request, "Invalid credentials!")
            return redirect("login")

    return render(request, "keyur/login.html")

def logout(request):
    request.session.flush()  # Clear the session
    messages.success(request, "Logged out successfully!")
    return redirect("login")

from django.shortcuts import redirect

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if "user_id" not in request.session:
            return redirect("login")  # Redirect if not logged in
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def dashboard(request):
    return render(request, "dashboard.html", {"username": request.session.get("username")})





# # Function to generate OTP
# def generate_otp():
#     return str(random.randint(100000, 999999))

# # Function to send OTP via Twilio
# def send_otp(phone, otp):
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     message = client.messages.create(
#         body=f"Your password reset OTP is {otp}",
#         from_=settings.TWILIO_PHONE_NUMBER,
#         to=phone
#     )
#     return message.sid

# from django.conf import settings
# from pymongo import MongoClient

# # Initialize MongoDB connection
# MONGO_URI = "mongodb://localhost:27017/"
# MONGO_DB_NAME = "your_database_name"

# client = MongoClient(MONGO_URI)
# db = client[MONGO_DB_NAME]
# USERS_COLLECTION = db["users"]  # This is your users collection

# import random
# from django.http import JsonResponse


# from django.views.decorators.csrf import csrf_exempt
# from .twilio_helper import send_sms
# # from .settings import USERS_COLLECTION

# @csrf_exempt
# def request_password_reset(request):
#     """Handles password reset request via SMS"""
#     if request.method == "POST":
#         phone = request.POST.get("phone")
#         users_collection = settings.USERS_COLLECTION

#         if not phone:
#             return JsonResponse({"error": "Phone number is required"}, status=400)

#         # Check if user exists
#         user = users_collection.find_one({"phone": phone})
#         if not user:
#             return JsonResponse({"error": "User not found"}, status=404)

#         # Generate 6-digit OTP
#         otp = str(random.randint(100000, 999999))

#         # Store OTP in MongoDB (overwrite if already exists)
#         USERS_COLLECTION.update_one(
#             {"phone": phone},
#             {"$set": {"reset_otp": otp}},
#             upsert=True
#         )

#         # Send OTP via SMS
#         sms_status = send_sms(phone, f"Your password reset code is: {otp}")

#         if sms_status:
#             return JsonResponse({"message": "OTP sent successfully."})
#         else:
#             return JsonResponse({"error": "Failed to send SMS."}, status=500)

#     return JsonResponse({"error": "Invalid request method"}, status=405)

# # Function to generate OTP
# def generate_otp():
#     return str(random.randint(100000, 999999))

# @csrf_exempt
# def verify_otp(request):
#     """Verifies the OTP entered by the user"""
#     if request.method == "POST":
#         phone = request.POST.get("phone")
#         otp = request.POST.get("otp")
#         users_collection = settings.USERS_COLLECTION

#         if not phone or not otp:
#             return JsonResponse({"error": "Phone and OTP are required"}, status=400)

#         user = users_collection.find_one({"phone": phone})

#         if not user or user.get("reset_otp") != otp:
#             return JsonResponse({"error": "Invalid OTP"}, status=400)

#         return JsonResponse({"message": "OTP verified. Proceed to reset password."})

#     return JsonResponse({"error": "Invalid request method"}, status=405)

# import bcrypt

# @csrf_exempt
# def reset_password(request):
#     """Allows user to reset password after OTP verification"""
#     if request.method == "POST":
#         phone = request.POST.get("phone")
#         new_password = request.POST.get("new_password")
#         users_collection = settings.USERS_COLLECTION

#         if not phone or not new_password:
#             return JsonResponse({"error": "Phone and new password are required"}, status=400)

#         user = users_collection.find_one({"phone": phone})

#         if not user:
#             return JsonResponse({"error": "User not found"}, status=404)

#         # Hash the new password
#         hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())

#         # Update password in MongoDB
#         USERS_COLLECTION.update_one(
#             {"phone": phone},
#             {"$set": {"password": hashed_password}, "$unset": {"reset_otp": 1}}
#         )

#         return JsonResponse({"message": "Password reset successfully."})

#     return JsonResponse({"error": "Invalid request method"}, status=405)


import secrets
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator

def request_password_reset(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))

            # Send the reset link via email (or SMS if needed)
            send_mail(
                "Password Reset Request",
                f"Click the link to reset your password: {reset_link}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return JsonResponse({"message": "Password reset link sent to your email!"})
        except User.DoesNotExist:
            return JsonResponse({"error": "User with this email does not exist."}, status=400)
    return render(request, "keyur/password_reset_request.html")

from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode

def reset_password_confirm(request, uidb64, token):
    if request.method == "POST":
        new_password = request.POST.get("password")
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model().objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                return JsonResponse({"message": "Password has been reset successfully!"})
            else:
                return JsonResponse({"error": "Invalid token!"}, status=400)
        except (User.DoesNotExist, ValueError, TypeError):
            return JsonResponse({"error": "Invalid request!"}, status=400)

    return render(request, "keyur/password_reset_form.html")


collection = settings.MONGO_DB["contacts"]
@csrf_exempt
def contactus(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile", "").strip()
        message = request.POST.get("message")

        if not re.fullmatch(r"\d{10}", mobile):
            return render(request, "keyur/contactus.html", {
                "contact_error": "Mobile number must contain exactly 10 digits."
            })

        # Store in MongoDB
        contact_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "mobile": mobile,
            "message": message
        }
        collection.insert_one(contact_data)
        # return HttpResponse("Message Sent Successfully")

    return render(request, "keyur/contactus.html")


from django.shortcuts import render, redirect
from .db import get_all_products, insert_product, delete_product
from django.contrib.auth.decorators import login_required
from bson.objectid import ObjectId
from .models import Product

product_collection = settings.MONGO_DB["products"]

def admin_dashboard(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image_url = request.POST.get("image_url")

        product = {
            "name": name,
            "price": price,
            "description": description,
            "image_url": image_url
        }
        product_collection.insert_one(product)
        return redirect("admin_dashboard")

    return render(request, "keyur/admin_dashboard.html")

def get_products(request):
    products = list(product_collection.find({}, {"_id": 0}))  # Fetch all products
    return JsonResponse({"products": products})


def add_product(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        image = request.FILES.get("image")

        products = Product(name=name, price=price, stock=stock, image=image)
        products.save()
        messages.success(request, "Product added successfully!")
        return redirect("admin_dashboard")

    return render(request, "keyur/add_product.html")

@login_required
def delete_product_view(request, product_id):
    delete_product(ObjectId(product_id))  # Convert string ID to ObjectId
    return redirect("admin_dashboard")

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


import bcrypt
from django.shortcuts import render, redirect
from pymongo import MongoClient

# Connect to MongoDB

def update_password(request):
    if request.method == "POST":
        email = request.POST.get("email")  # Get email from form
        new_password = request.POST.get("new_password")  # Get new password
        
        if not email or not new_password:
            messages.error(request, "Email and new password are required!")
            return redirect("update_password")

        # Hash the new password
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()

        # Connect to MongoDB collection
        users_collection = settings.USERS_COLLECTION

        # Check if user exists
        user = users_collection.find_one({"email": email})

        if user:
            # Update the user's password
            users_collection.update_one(
                {"_id": ObjectId(user["_id"])},
                {"$set": {"password": hashed_password}}
            )
            messages.success(request, "Password updated successfully!")
            return redirect("login")  # Redirect to login after update
        else:
            messages.error(request, "User with this email does not exist!")
            return redirect("update_password")

    return render(request, "keyur/update_password.html")



def save_delivery_address(request):
    if "user_id" not in request.session:
        return redirect("login")

    if request.method == "POST":
        country_code = request.POST.get("country_code", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()

        if not country_code or not phone_number.isdigit():
            messages.error(request, "Please enter a valid phone number.")
            return redirect("address")

        user_id = request.session["user_id"]
        address_data = {
            "user_id": user_id,
            "full_name": request.POST.get("fullName", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "country_code": country_code,
            "phone_number": phone_number,
            "phone": f"{country_code} {phone_number}",
            "address": request.POST.get("address", "").strip(),
            "city": request.POST.get("city", "").strip(),
            "state": request.POST.get("state", "").strip(),
            "zip_code": request.POST.get("zip", "").strip(),
            "country": request.POST.get("country", "").strip(),
        }
        required_fields = ("full_name", "email", "address", "city", "state", "zip_code", "country")
        if any(not address_data[field] for field in required_fields):
            messages.error(request, "Please complete all address fields.")
            return redirect("address")

        address_id = request.POST.get("address_id", "").strip()
        if address_id:
            settings.DELIVERY_COLLECTION.update_one(
                {"_id": ObjectId(address_id), "user_id": user_id},
                {"$set": address_data},
            )
        else:
            from datetime import datetime
            address_data["created_at"] = datetime.utcnow()
            inserted = settings.DELIVERY_COLLECTION.insert_one(address_data)
            address_id = str(inserted.inserted_id)

        request.session["selected_address_id"] = address_id

        messages.success(request, "Address saved successfully.")
        return redirect("address")

    return render(request, "keyur/Address.html") 


def delete_delivery_address(request, address_id):
    if "user_id" not in request.session:
        return redirect("login")

    if request.method == "POST":
        settings.DELIVERY_COLLECTION.delete_one({
            "_id": ObjectId(address_id),
            "user_id": request.session["user_id"],
        })
        if request.session.get("selected_address_id") == address_id:
            request.session.pop("selected_address_id", None)
        messages.success(request, "Address deleted successfully.")
    return redirect("address")

products_collection = settings.MONGO_DB["products"]

def search_products(request):
    query = request.GET.get("q", "").strip()
    if not query:
        return JsonResponse({"error": "Empty search query"}, status=400)

    # Search for products by name (case-insensitive)
    results = list(products_collection.find({"product_name": {"$regex": query, "$options": "i"}}))

    # Convert ObjectId to string for JSON response
    for result in results:
        result["_id"] = str(result["_id"])

    return JsonResponse({"products": results}, status=200)