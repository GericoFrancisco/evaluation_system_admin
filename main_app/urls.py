from django.urls import path
from . import views

urlpatterns = [
# path('login_404/', views.login_error, name='login_403'),
# path('home_404/', views.home_error, name='home_403'),
path('', views.login, name='login'),
# path('register/', views.register, name='register'),
path('manage_seminar/', views.manage_seminar, name='manage_seminar'),
path('dashboard/', views.dashboard, name='dashboard'),
path('manage_facilitator', views.manage_facilitator, name='manage_facilitator'),
path('manage_evaluator/', views.manage_evaluator, name='manage_evaluator'),
path('report/', views.report, name='report'),
path('postsignIn/', views.postsignIn, name="post_sign"),
path('postsignUp/', views.postsignUp),
path('', views.logout, name="logout"),
path('total_evaluations/', views.total_evaluations, name="total_evaluations"),
path('total_evaluators/', views.total_evaluators, name="total_evaluators"),
path('total_facilitators/', views.total_facilitators, name="total_facilitators"),
path('total_seminars/', views.total_seminars, name="total_seminars"),
path('report_view_evaluation_info/', views.report_view_evaluation_info, name="report_view_evaluation_info"),
path('report_view_evaluator/', views.report_view_evaluator, name="report_view_evaluator"),
path('forgot_password', views.forgot_password , name = 'forgot_password'),
path('forgot_password_func/', views.forgot_password_func , name = 'forgot_password_func'),
path('add_seminar/', views.add_seminar , name = 'add_seminar'),
path('edit_seminar/', views.edit_seminar , name = 'edit_seminar'),
path('edit_facilitator/', views.edit_facilitator , name = 'edit_facilitator'),
path('edit_evaluator/', views.edit_evaluator , name = 'edit_evaluator'),
path('add_facilitator/', views.add_facilitator , name = 'add_facilitator'),
path('add_evaluator/', views.add_evaluator , name = 'add_evaluator'),
path('view_seminar_information', views.view_seminar_information , name = 'view_seminar_information'),
path('post_add_seminar/', views.post_add_seminar , name = 'post_add_seminar'),
path('post_edit_seminar/', views.post_edit_seminar),
path('post_edit_evaluator/', views.post_edit_evaluator),
path('post_start_seminar/', views.post_start_seminar),
path('post_view_seminar_actions/', views.post_view_seminar_actions),
path('post_add_facilitator/', views.post_add_facilitator , name = 'post_add_facilitator'),
path('post_add_evaluator/', views.post_add_evaluator , name = 'post_add_evaluator'),
path('export_evaluation/', views.export_evaluation, name = 'export_evaluation'),
path('delete_seminar/',  views.delete_seminar, name="delete_seminar"),
path('delete_facilitator/',  views.delete_facilitator),
path('delete_evaluator/',  views.delete_evaluator),
path('view_seminar/', views.view_seminar, name = 'view_seminar'),
path('generate_evaluator/',views.generate_evaluator),
path('generate_seminar/',views.generate_seminar),
path('post_delete_facilitator/', views.post_delete_facilitator),
path('post_edit_facilitator/', views.post_edit_facilitator),
path('report_view_evaluation_info/pdf/', views.save_summary),
]
