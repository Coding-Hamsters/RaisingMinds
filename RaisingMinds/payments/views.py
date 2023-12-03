from django.shortcuts import render
from post.models import Post
from django.conf import settings
import uuid
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def checkout(request,post_id):

    post = Post.objects.get(id = post_id)

     # get the domain name
    host = request.get_host()

    donate_amount1 = 0

    if request.method == 'POST':
        donate_amount = request.POST.get('amount')
        donate_amount1 = donate_amount
    #     request.session.modified = True
    # elif request.method == 'GET':
    #     # clear the session variable when the page is refreshed
    #     request.session.pop('donate_amount1', None)

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': donate_amount1,
        'item_name': post.title,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs = {'post_id': post.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs = {'post_id': post.id})}",
    }

    # session for store amount
    request.session['donate_amount1'] = donate_amount1
    request.session.modified = True

    paypal_donation = PayPalPaymentsForm(initial=paypal_checkout)

    return render(request,'payments/payment_checkout.html',{'post':post,'paypal':paypal_donation,'donate':donate_amount1})

@login_required(login_url='login')
def paymentSuccess(request,post_id):

    post = Post.objects.get(id = post_id)

    donate_amount = 0

    # if request.session == True:
    #     donate_amount = request.session['donate_amount1']

    # post.current_amount = post.current_amount + int(donate_amount)
    # post.save()
    # del request.session['donate_amount1']

    # Check if 'donate_amount1' exists in the session
    if 'donate_amount1' in request.session:

        donate_amount = request.session['donate_amount1']
        post.current_amount += int(donate_amount)
        post.save()

        # end the session
        del request.session['donate_amount1']

    return render(request,'payments/payment_success.html',{'post':post})

@login_required(login_url='login')
def paymentFail(request,post_id):

    post = Post.objects.get(id = post_id)
    return render(request,'payments/payment_failed.html',{'post':post})

