from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

from .views import (
	index,
	about_us,
	branches,
	contact_us,
	csr,
	services,
	profile,
	history,
	team,
	board,
    savings,
    loans,
    impact,
    money_transfers,
    tractor,
    agency_services,
    customer_support,
    ordinary_savings,
    infant_account,
    fixed_deposit_account,
    joint_account,
    group_account,
    salary_loan,
    school_fees_loan,
    farmer_loan,
    motorcycle_loan,
    asset_commercial_loan,
    emergency_loan
	)


app_name = "koboko_sacco"

urlpatterns= [
    path('',index, name ='index'),
    path('about_us',about_us,name='about_us'),
    path('about_us',about_us,name='about_us'),
    path('branches',branches,name='branches'),
    path('contact_us',contact_us,name='contact_us'),
    path('cooperate_social_responsibility',csr,name='cooperate_social_responsibility'),
    path('services',services,name='services'),
    path('company_profile',profile,name='company_profile'),
    path('our_history',history,name='our_history'),
    path('meet_our_team',team,name='meet_our_team'),
    path('impact',impact,name='impact'),
    path('KUSACCO_board',board,name='KUSACCO_board'),
    path('savings',savings,name='savings'),
    path('loans',loans,name='loans'),
    path('money_transfers',money_transfers,name='money_transfers'),
    path('tractor',tractor,name='tractor'),
    path('agency_services',agency_services,name='agency_services'),
    path('customer_support',customer_support,name='customer_support'),
    path('ordinary_savings_account',ordinary_savings,name='ordinary_savings_account'),
    path('infant_savings_account',infant_account,name='infant_savings_account'),
    path('fixed_deposit_account',fixed_deposit_account,name='fixed_deposit_account'),
    path('joint_account',joint_account,name='joint_account'),
    path('group_account',group_account,name='group_account'),
    path('salary_loan',salary_loan,name='salary_loan'),
    path('school_fees_loan',school_fees_loan,name='school_fees_loan'),
    path('farmer_loan',farmer_loan,name='farmer_loan'),
    path('motorcycle_loan',motorcycle_loan,name='motorcycle_loan'),
    path('asset_commercial_loan',asset_commercial_loan,name='asset_commercial_loan'),
    path('emergency_loan',emergency_loan,name='emergency_loan'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)