from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.frontpage, name='frontpage'),
    url(r'^frontpage.html$', views.frontpage, name='frontpage'),

    url(r'^caterers_list.html$', views.caterers_list, name='caterers_list'),
    url(r'^caterers_indian.html$', views.caterers_indian, name='caterers_indian'),
    url(r'caterers_continental.html$', views.caterers_continental, name='caterers_continental'),
    url(r'caterers_mexican.html$', views.caterers_mexican, name='caterers_mexican'),
    url(r'^caterers_italian.html$', views.caterers_italian, name='caterers_italian'),
    url(r'^caterers_chinese.html$', views.caterers_chinese, name='caterers_chinese'),

    url(r'^photographers_list.html$', views.photographers_list, name='photographers_list'),
    url(r'^candid.html$', views.candid, name='candid'),
    url(r'^hdr.html$', views.hdr, name='hdr'),

    url(r'^entertainers_list.html$', views.entertainers_list, name='entertainers_list'),
    url(r'^entertainers_dj.html$', views.entertainers_dj, name='entertainers_dj'),
    url(r'^entertainers_musicians.html$', views.entertainers_musicians, name='entertainers_musicians'),
    url(r'^entertainers_dance.html$', views.entertainers_dance, name='entertainers_dance'),
    url(r'^entertainers_comedians.html$', views.entertainers_comedians, name='entertainers_comedians'),

    url(r'^themes_list.html$', views.themes_list, name='themes_list'),
    url(r'^themes_birthday.html$', views.themes_birthday, name='themes_birthday'),
    url(r'^themes_corporate_event.html$', views.themes_corporate_event, name='themes_corporate_event'),
    url(r'^themes_wedding.html$', views.themes_wedding, name='themes_wedding'),
    url(r'^themes_get_together.html$', views.themes_get_together, name='themes_get_together'),

    url(r'^venue_list.html$', views.venue_list, name='venue_list'),
    url(r'^venue_banquet_hall.html$', views.venue_banquet_hall, name='venue_banquet_hall'),
    url(r'^venue_roof_top.html$', views.venue_roof_top, name='venue_roof_top'),
    url(r'^venue_poolside.html$', views.venue_poolside, name='venue_poolside'),
    url(r'^venue_conference_center.html$', views.venue_conference_center, name='venue_conference_center'),
    url(r'^venue_open_space.html$', views.venue_open_space, name='venue_open_space'),
    url(r'^venue_hotel.html$', views.venue_hotel, name='venue_hotel'),
   

    url(r'^accomodations_nearby.html$', views.accomodations_nearby, name='accomodations_nearby'),

    url(r'^accomodations.html$', views.accomodations, name='accomodations'),
    url(r'^service_apartments.html$', views.service_apartments, name='service_apartments'),
    url(r'^accomodation_hotel.html$', views.accomodation_hotel, name='accomodation_hotel'),

   url(r'^decorators.html$', views.decorators, name='decorators'),
]


