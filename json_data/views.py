import json

from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json_data.models import SnpsDesignedCards, CardModel, Style, CardObject
# Create your views here.

def jdefault(o):
    return o.__dict__

@csrf_exempt
def index(request, card_id):
    cards = SnpsDesignedCards.objects.filter(code=card_id)
    cm = CardModel('div')
    for card in cards:
        if card.order == '0':
            #if card_id.strip() != 'CRD04':
            #    co = CardObject('div')
            #    co.class1='card'
            continue
        elif card.order == '1':
            if card.relation:
                sty = Style(card.relation.row, card.relation.column)
            else:
                sty = Style(card.row, card.column)
                                    
            sty.background_color = card.object.color
            sty.width=card.object.width
            sty.height=card.object.height
            
            sty.border_top_left_radius=str(card.object.upper_left)+'px'
            sty.border_top_right_radius=str(card.object.upper_right)+'px'
            sty.border_bottom_left_radius=str(card.object.lower_left)+'px'
            sty.border_bottom_right_radius=str(card.object.lower_right)+'px'
            
            cm = CardModel('div')
            if card_id.strip() != 'CRD04':
                cm.class1='card'                                
            cm.css = sty
            
            continue
        else:
            co = CardObject('div')
            co.order=card.order
            sty = Style(card.row, card.column)
            if (card.type).lower()=='shape':
                sty.background_color = card.object.color
                sty.width=card.object.width
                sty.height=card.object.height
                
                if card.object.stroke_size != None :
                    sty.border_style = 'solid'
                    sty.border_color = card.object.stroke_color
                    sty.border_width=str(card.object.stroke_size)+'px'
                co.css = sty
                cm.html.append(co)
            elif (card.type).lower()=='text':
                co.type='span'
                sty.color=card.object.font_id.font_color
                sty.font_family=card.object.font_id.font_family
                if (card.object.font_id.font_weight).lower() == 'regular':
                    sty.font_weight='normal'
                elif (card.object.font_id.font_weight).lower() == 'semibold':
                    sty.font_weight='bold'
                else:
                    sty.font_weight=card.object.font_id.font_weight
                sty.font_style=card.object.font_id.font_posture
                
                sty.font_size=card.object.font_id.font_size
                sty.font_spacing=card.object.font_id.character_spacing
                    
                sty.direction=card.object.txt_id.text_direction
                sty.width=card.object.txt_id.ta_width
                sty.height=card.object.txt_id.ta_height
                
                sty.margin_left=card.object.txt_id.margin_left
                sty.margin_right=card.object.txt_id.marjin_right
                sty.margin_top=card.object.txt_id.marjin_top
                sty.margin_bottom=card.object.txt_id.marjin_bottom
                
                if card.object.txt_id.alignment_j_c_r_l_field.lower().strip()=='centered':
                    sty.text_align = "center"
                elif card.object.txt_id.alignment_j_c_r_l_field.lower().strip()=='left alligned':
                    sty.text_align = "left"
                if card.object.txt_id.case_c_u_l_t_o_field.lower().strip() == 'upper case':
                    sty.text_transform="uppercase"
                co.css=sty
                if card.message.body_en_field.lower().strip() == 'hello <input>':
                    co.html='hello &ltinput&gt'
                else:
                    co.html=card.message.body_en_field
                cm.html.append(co)
                
            elif (card.type).lower()=='button':
                el = None
                #el = next(x for x in cm.html if (x.order==card.order and x.type=='button'))
                for x in cm.html:
                    if (x.order.strip()==card.order.strip() and x.type.strip()=='button'):
                        el = x
                        break
                
                if el is not None:
                    if card.url != None:
                        el.onclick=str(card.state)+'(this,\''+str(card.url)+'\')'
                    else:
                        el.onclick=str(card.state)+'(this)'
                    continue
                else:
                    co.type='button'
                    sty.background_color = card.object.color
                    sty.width=card.object.width
                    sty.height=card.object.height
                    
                    if card.message is not None:
                        co.html = card.message.body_en_field
                        
                    co.css = sty
                    cm.html.append(co)
                                    
            elif (card.type).lower()=='input area':
                co.type='input'
                co.placeholder=card.message.body_en_field
                sty.color=card.object.font_id.font_color
                sty.font_family=card.object.font_id.font_family
                if (card.object.font_id.font_weight).lower() == 'regular':
                    sty.font_weight='normal'
                elif (card.object.font_id.font_weight).lower() == 'semibold':
                    sty.font_weight='bold'
                else:
                    sty.font_weight=card.object.font_id.font_weight
                sty.font_style=card.object.font_id.font_posture
                
                sty.font_size=card.object.font_id.font_size
                sty.font_spacing=card.object.font_id.character_spacing
                
                
                sty.direction=card.object.txt_id.text_direction
                sty.width=card.object.txt_id.ta_width
                sty.height=card.object.txt_id.ta_height
                sty.margin_left=card.object.txt_id.margin_left
                sty.margin_right=card.object.txt_id.marjin_right
                sty.margin_top=card.object.txt_id.marjin_top
                sty.margin_bottom=card.object.txt_id.marjin_bottom
                if card.object.txt_id.alignment_j_c_r_l_field.lower().strip()=='centered':
                    sty.text_align = "center"
                elif card.object.txt_id.alignment_j_c_r_l_field.lower().strip()=='left alligned':
                    sty.text_align = "left"
                if card.object.txt_id.case_c_u_l_t_o_field.lower().strip() == 'upper case':
                    sty.text_transform="uppercase"
                co.css=sty
                cm.html.append(co)
                                
            #elif card.type.lower()=='card':
                
            # this is for kulakcik
            else:
                sty.background_color = card.object.color
                sty.width=card.object.width
                sty.height=card.object.height
                
                co.css = sty
                cm.html.append(co)
                
    dumps = json.dumps(cm,default=jdefault)
    
    dumps = convertToHtmlAttributeNames(dumps)
    
    return HttpResponse(dumps, content_type='application/json')
    #return render(request,'index.html',locals())

def convertToHtmlAttributeNames(dumps):
    dumps = dumps.replace('background_color', 'background-color')
    dumps = dumps.replace('font_style', 'font-style')
    dumps = dumps.replace('font_size', 'font-size')
    dumps = dumps.replace('font_spacing', 'font-spacing')
    dumps = dumps.replace('margin_right', 'margin_right')
    dumps = dumps.replace('text_align', 'text-align')
    dumps = dumps.replace('font_weight', 'font-weight')
    dumps = dumps.replace('text_transform', 'text-transform')
    dumps = dumps.replace('margin_top', 'margin-top')
    dumps = dumps.replace('margin_left', 'margin-left')
    dumps = dumps.replace('margin_bottom', 'margin-bottom')
    dumps = dumps.replace('font_family', 'font-family')
    dumps = dumps.replace('border_radius', 'border-radius')
    dumps = dumps.replace('border_top_left_radius', 'border-top-left-radius')
    dumps = dumps.replace('border_top_right_radius', 'border-top-right-radius')
    dumps = dumps.replace('border_bottom_left_radius', 'border-bottom-left-radius')
    dumps = dumps.replace('border_bottom_right_radius', 'border-bottom-right-radius')
    dumps = dumps.replace('border_color', 'border-color')
    dumps = dumps.replace('border_width', 'border-width')
    dumps = dumps.replace('border_style', 'border-style')
    dumps = dumps.replace('class1', 'class')
    return dumps
    
@csrf_exempt
def home(request):
    return render(request,'index.html',locals())