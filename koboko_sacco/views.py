from django.shortcuts import render

# Create your views here.
def index (request):
    context={
        'home':'active',
    }
    return render(request,'index.html',context)
    
def about_us (request):
    context={
        'about_us':'active',
    }
    return render(request,'about_us.html',context)

def branches(request):
    context={
        'branches':'active',
    }
    return render(request,'branches.html',context)

def contact_us(request):
    context={
        'contact_us':'active',
    }
    return render(request,'contact_us.html',context)

def csr(request):
    context={
        'csr':'active',
    }
    return render(request, 'csr.html',context)

def services(request):
    context={
        'services':'active',
    }
    return render(request,'services.html',context)


def profile(request):
    context={
        'about_us':'active',
    }
    return render(request,'profile.html',context)

def history(request):
    context={
        'about_us':'active',
    }
    return render(request,'history.html',context)

def team(request):
    context={
        'about_us':'active',
    }
    return render(request,'team.html',context)


def board(request):
    context={
        'about_us':'active',
    }
    return render(request,'board.html',context)


def impact(request):
    context={
        'impact':'active',
    }
    return render(request,'impact.html',context)


def savings(request):
    context={
        'services':'active',
    }
    return render(request,'savings.html',context)


def loans(request):
    context={
        'services':'active',
    }
    return render(request,'loans.html',context)

def money_transfers(request):
    context={
        'services':'active',
    }
    return render(request,'money_transfers.html',context)

def tractor(request):
    context={
        'services':'active',
    }
    return render(request,'tractor.html',context)

def agency_services(request):
    context={
        'services':'active',
    }
    return render(request,'agency_services.html',context)

def customer_support(request):
    context={
        'services':'active',
    }
    return render(request,'customer_support.html',context)

def ordinary_savings(request):
    context={
        'services':'active',
    }
    return render(request,'ordinary_savings.html',context)

def infant_account(request):
    context={
        'services':'active',
    }
    return render(request,'infant_account.html',context)

def fixed_deposit_account(request):
    context={
        'services':'active',
    }
    return render(request,'fixed_deposit_account.html',context)

def joint_account(request):
    context={
        'services':'active',
    }
    return render(request,'joint_account.html',context)

def group_account(request):
    context={
        'services':'active',
    }
    return render(request,'group_account.html',context)

def salary_loan(request):
    context={
        'services':'active',
    }
    return render(request,'salary_loan.html',context)

def school_fees_loan(request):
    context={
        'services':'active',
    }
    return render(request,'school_fees_loan.html',context)

def farmer_loan(request):
    context={
        'services':'active',
    }
    return render(request,'farmer_loan.html',context)

def motorcycle_loan(request):
    context={
        'services':'active',
    }
    return render(request,'motorcycle_loan.html',context)

def asset_commercial_loan(request):
    context={
        'services':'active',
    }
    return render(request,'asset_commercial_loan.html',context)

def emergency_loan(request):
    context={
        'services':'active',
    }
    return render(request,'emergency_loan.html',context)