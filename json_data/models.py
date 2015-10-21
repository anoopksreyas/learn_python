# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

# class AuthGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=80)
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
# 
# class AuthGroupPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group = models.ForeignKey(AuthGroup)
#     permission = models.ForeignKey('AuthPermission')
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
# 
# class AuthPermission(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     content_type = models.ForeignKey('DjangoContentType')
#     codename = models.CharField(max_length=100)
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
# 
# class AuthUser(models.Model):
#     id = models.IntegerField(primary_key=True)
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField()
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=75)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
# 
# class AuthUserGroups(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(AuthUser)
#     group = models.ForeignKey(AuthGroup)
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
# 
# class AuthUserUserPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(AuthUser)
#     permission = models.ForeignKey(AuthPermission)
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
# 
# class DjangoAdminLog(models.Model):
#     id = models.IntegerField(primary_key=True)
#     action_time = models.DateTimeField()
#     user = models.ForeignKey(AuthUser)
#     content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
#     object_id = models.TextField(blank=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.IntegerField()
#     change_message = models.TextField()
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
# 
# class DjangoContentType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
# 
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#     class Meta:
#         managed = False
#         db_table = 'django_session'

class SnpsCardRelation(models.Model):
    on = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    open = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    state = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    column = models.IntegerField(blank=True, null=True) # Field name made lowercase.
    row = models.IntegerField(blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'snps_card_relation'


class SnpsObjectsType(models.Model):
    object_id = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    is_data = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'snps_objects_type'


class SnpsFontType(models.Model):
    font_id = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    font_family = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    font_weight = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    font_posture = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    font_size = models.IntegerField(blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    font_color = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    character_spacing = models.IntegerField(blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    class Meta:
        db_table = 'snps_font_type'

class SnpsTextAreaType(models.Model):
    text_area_id = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    text_direction = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    ta_width = models.IntegerField(blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    ta_height = models.IntegerField(blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    margin_left = models.IntegerField(blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    marjin_right = models.IntegerField(blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    marjin_top = models.IntegerField(blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    marjin_bottom = models.IntegerField(blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    alignment_j_c_r_l_field = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    line_spacing = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    motion_v_h_field = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rows = models.IntegerField(blank=True, null=True) # Field name made lowercase.
    case_c_u_l_t_o_field = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    class Meta:
        db_table = 'snps_text_area_type'

class SnpsDesignObjects(models.Model):
    specification_id = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    object = models.ForeignKey(SnpsObjectsType)
    description = models.CharField( max_length=255, blank=True) # Field name made lowercase.
    color = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    width = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    height = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    upper_left = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    lower_left = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    upper_right = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    lower_right = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    radius = models.CharField(max_length=255, blank=True)
    stroke_size = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    stroke_color = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    font_id = models.ForeignKey(SnpsFontType, null=True)
    txt_id = models.ForeignKey(SnpsTextAreaType, null=True)
    message = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    sample = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    tarih = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'snps_design_objects'

class SnpsMessageList(models.Model):
    code = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    module = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    submodule = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    msgtype = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    body_en_field = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    class Meta:
        db_table = 'snps_message_list'

class SnpsDesignedCards(models.Model):
    code = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    order = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    type = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    icon = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    operation = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    state = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    object = models.ForeignKey(SnpsDesignObjects, null = True) # Field name made lowercase.
    plane_type = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    column = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    row = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    message = models.ForeignKey(SnpsMessageList, null = True) # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    sample = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    relation = models.ForeignKey(SnpsCardRelation, null = True)
    class Meta:
        db_table = 'snps_designed_cards'

class SnpsOperations(models.Model):
    operation_constant = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'snps_operations'

class SnpsStates(models.Model):
    state_type = models.CharField(max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'snps_states'

STYLE = {
        'font-family':''
         
         }


class Style(object):
    position=''
    top=''
    left=''
    background_color ='' 
    width = ''
    height = ''
    color=''
    font_family=''
    font_weight=''
    font_style=''
    font_size=''
    font_spacing=''
    direction=''
    margin_left=''
    margin_right=''
    margin_top=''
    margin_bottom=''
    text_align = ''
    text_transform=''
    
    border=''
    border_top_left_radius=''
    border_top_right_radius=''
    border_bottom_left_radius=''
    border_bottom_right_radius=''
    
    border_color=''
    border_width = ''
    border_style = ''
    
    
    def __init__(self,top, left):
        self.top=top
        self.left=left
        self.position='absolute'

class CardObject(object):
    type=''
    css=''
    order=''
    onclick=''
    placeholder=''
    html=''
    def __init__(self, type):
        self.type=type
        
    
class CardModel(object):
    type=''
    class1=''
    id1 = ''
    css =  ''
    html = []
    
    def __init__(self, type):
        self.type=type
        self.html=[]
        