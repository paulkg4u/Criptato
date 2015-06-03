from django.conf.urls import patterns, url
from ssapp import views
urlpatterns=patterns('',
	url(r'^$', views.index),
	url(r'^index/',views.index,name = 'index'),
	url(r'^new_sheet/',views.new_sheet,name='new-sheet'),
	url(r'^new_group/',views.new_group,name='new-group'),
	url(r'^edit_sheet/', views.edit_sheet,name='edit-sheet'),
	url(r'^delete-table/(?P<table_id>[\w\-]+)/$',views.delete_table,name='delete-table'),
	url(r'^delete-group-table/(?P<table_id>[\w\-]+)/$',views.delete_group_table,name='delete-group-table'),
	url(r'^save-new-table/',views.save_new_table,name='save-new-table'),
	url(r'^save-new-group-table/',views.save_new_group_table,name='save-new-group-table-table'),
	url(r'^edit-table/(?P<t_id>[\w\-]+)/$',views.edit_sheet,name='edit-table'),
	url(r'^save-edited-table/(?P<t_id>[\w\-]+)/$',views.save_edited_table,name='save-edited-table'),
	url(r'^create-new-group/',views.create_new_group,name = 'create-new-group'),
	url(r'^manage-group/(?P<group_id>[\w\-]+)/$',views.manage_group,name='manage-group'),
	url(r'^new-sheet-group/(?P<group_id>[\w\-]+)/$',views.new_sheet_group,name='new-sheet-group'),
	url(r'^add-member/(?P<group_id>[\w\-]+)$',views.add_member,name='add-member'),
	url(r'^add-new-member/',views.add_new_member,name='add-new-member'),
	url(r'^about/',views.about_us,name = 'about-us'),
	url(r'^how/',views.how_it_works,name='how-it-works'),



	

	
	)