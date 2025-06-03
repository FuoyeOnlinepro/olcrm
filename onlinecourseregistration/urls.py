from django.urls import path
from .views import (
    HomeView,
    landing_page,
    change_password,
    password_change_done,
    login,
    signup,
    notification,
    FAQ,
    transaction,
    marketplace,
    market,  # Import your marketplace view here
    initiate_payment,
    kyc,
    courses,
    courseregistrationform,
    adminpage,
    available_courses,
    upload_course,
    register_course,
    registration_success,
    user_profile,
    registration_history,
    get_private_key,
    allreg,
    logout_view,
    
)

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Landing page
    path('home/', HomeView.as_view(), name='home'),  # Home view
    path('login/', login, name='login'),  # Login view
   
    path('signup/', signup, name='signup'),  # Signup view
    path('change_password/', change_password, name='change_password'),  # Change password
    path('password_change_done/', password_change_done, name='password_change_done'),  # Password change done
    path('notification/', notification, name='notification'),  # Notification view
    path('FAQ/', FAQ, name='FAQ'),  # FAQ view
    path('transaction/', transaction, name='transaction'),  # Transaction view
    path('marketplace/', marketplace, name='marketplace'),  # Marketplace view
    path('market/', market, name='market'),
    path('initiate_payment/', initiate_payment, name='initiate_payment'),
    path('kyc/', kyc, name='kyc'),
    path('courses/', courses, name='courses'),
    path('courseregistrationform/', courseregistrationform, name='courseregistrationform'),
    path('adminpage/', adminpage, name='adminpage'),
    path('admin/upload-course/', upload_course, name='upload_course'),
    path('student/available-courses/', available_courses, name='available_courses'),
    path('register-course/<int:course_id>/', register_course, name='register_course'),
    path('registration-success/', registration_success, name='registration_success'),
    path('profile/', user_profile, name='user_profile'),
    path('registration-history/', registration_history, name='registration_history'),
    path('allreg/', allreg, name='allreg' ),
    path('get-private-key/', get_private_key, name='get_private_key'),
    path('logout/', logout_view, name='logout'),
]
